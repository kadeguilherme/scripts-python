def print_opcoes():
    print("Opção 1 - Upgrade_eks_control_plane step 7 - step 8.1")
    print("Opção 2 - Upgrade eks nodes control step 8.1 - step 9")
    print("Opção 3 - Change more configurations in the Terragrunt file step 9 step 10")

def option(num):
    if num == 1:
        print(upgrade_eks_control_plane())
    elif num == 2:
        print(upgrade_worker_node_group())
    elif num == 3:
        print(remove_the_unnecessary_lines())
    else:
        print("Opção inválida")

def upgrade_eks_control_plane():
    with open('terragrunt.hcl', 'r+') as arquivo:
        linhas = arquivo.readlines()
        for i,linha in enumerate(linhas):
            if 'cluster_name' in linha and 'local.cluster_name' in linha and "cluster_version" not in linhas[i+1]:
                partes = linha.split('=')
                if 'cluster_name' in partes[0] and 'local.cluster_name' in partes[1]:
                    linhas.insert(i + 1, 'cluster_version = "1.24"\n')
            if 'dependency "api_platform_policy"' in linha:
                linhas.remove(linha)
                linhas.insert(i, "dependency \"security_group\" {\n")
                linhas.insert(i + 1, '\tconfig_path = \"../../network/security-group/internal-traffic/\"\n')
            if "dependency.api_platform_policy.outputs.arn" in linha:
                linhas.pop(i)
            if "install_discovery_tool" in linha and "\tinstall_aws_efs_csi_driver\t\t\t\t\t= false\n" not in linhas:
                linhas.insert(i+1, "\tinstall_aws_efs_csi_driver"+"\t"*5+"= false\n")           
            if 'capacity_type = \"SPOT\"' in linha and '\t\tcluster_version = "1.23"\n' not in linhas :
                linhas.insert(i + 1, '\t\tcluster_version = "1.23"\n')
                if('\t\t\tcluster_version = "1.24"\n' in linhas):
                    linhas.remove('\t\t\tcluster_version = "1.24"\n')
            if 'capacity_type = "ON_DEMAND"' in linha and '\t\tcluster_version = "1.23"\n' not in linhas[i+1]: 
                linhas.insert(i +1, '\t\tcluster_version = "1.23"\n')
                if('\t\t\tcluster_version = "1.24"\n' in linhas):
                    linhas.remove('\t\t\tcluster_version = "1.24"\n')
        arquivo.seek(0)
        arquivo.writelines(linhas) 
        arquivo.truncate()
        arquivo.close()
        print("="*150)
        return ("\t"*5 + "\033[1;32mAgora aplicar o terragrunt apply para fazer o Upgrade EKS managed node groups\033[0m\n" + "="*150 + "\n")
    
def upgrade_worker_node_group():
    with open('terragrunt.hcl', 'r+') as arquivo:
        linhas = arquivo.readlines()
        for i,linha in enumerate(linhas):
            if '\t\tcluster_version = "1.23"\n' in linha:
                linhas.remove(linha)
                linhas.insert(i + 1, '\t\t\tcluster_version = "1.24"\n')
                linhas.insert(i + 2, '\t\t\tcreate_security_group = false\n')
            if 'associate_public_ip_address = false' in linha and '\t\t\tvpc_security_group_ids = [dependency.security_group.outputs.id]\n' not in linhas:
                linhas.insert(i + 3, '\n\t\t\tvpc_security_group_ids = [dependency.security_group.outputs.id]\n')
        arquivo.seek(0)
        arquivo.writelines(linhas) 
        arquivo.truncate()
        arquivo.close()
        print("="*150)
        return ("\t"*5 + "\033[1;32mAgora aplicar o terragrunt apply para fazer o Upgrade EKS control plane\033[0m\n" + "="*150 + "\n")


def remove_the_unnecessary_lines():
    with open('terragrunt.hcl', 'r+') as arquivo:
        linhas = arquivo.readlines()
        for i,linha in enumerate(linhas):
            if '../../../../../../../modules/aws/commons//kubernetes-1-23/' in linha:
                linhas.remove(linha)
                linhas.insert(i, '\tsource = \"${get_repo_root()}/terraform/modules/aws/commons/kubernetes-1-24///\"\n')
            if 'cluster_version = "1.24"' in linha:
                linhas.remove(linha)
                linhas.remove(linhas[i])
            if  'cluster_encryption_config' in linha:
                linhas.insert(i + 1, '\tcluster_encryption_config = {\n')
                linhas.remove(linhas[i])
                for j in range(i+1,120):
                    if "]" in linhas[j] and "[" not in linhas[j]:
                        linhas.remove(linhas[j])
            if 'cluster_endpoint_private_access' in linha: 
                if "create_kms_key" not in linhas[i+1]:
                    linhas.insert(i+1,'\tcreate_kms_key = false\n')
                    break

            if 'iam_role_additional_policies' in linha and '\t\t\t\tiam_role_additional_policies = {\n' not in linhas:
                linhas.insert(i + 1, '\t\t\t\tiam_role_additional_policies = {\n')
                linhas.remove(linhas[i])
                for j in range(i+1,i+5):
                        #linhas.insert(i + 2, '\t\t"\"AmazonSSMManagedInstanceCore\" = \"arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore\",\n')
                    if "]" in linhas[j] and "[" not in linhas[j]:
                        linhas.pop(j)
                        break
            if 'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess' in linha and "\t"*5 + "\"AmazonEC2ReadOnlyAccess\"" + "\t"*4 + "= \"arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess\",\n" not in linhas:
                linhas.remove(linha)
                linhas.insert(i,"\t"*5 + "\"AmazonEC2ReadOnlyAccess\"" + "\t"*4 + "= \"arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess\",\n")
            if 'arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore' in linha and "\t"*5 + "\"AmazonSSMManagedInstanceCore\"\t= \"arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore\",\n" not in linhas:
                linhas.remove(linha)
                linhas.insert(i,"\t"*5 + "\"AmazonSSMManagedInstanceCore\"\t= \"arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore\",\n")
            if 'volume_type' in linha and "encrypted" not in linhas[i+1]:
                linhas.insert(i+1,"\t"*6+"encrypted    = true\n")
        arquivo.seek(0)
        arquivo.writelines(linhas) 
        arquivo.truncate()
        arquivo.close()
        print("="*150)
        return ("\t"*5 + "\033[1;32mAgora aplicar o terragrunt apply para fazer o Upgrade EKS control plane\033[0m\n" + "="*150 + "\n")

while True:
    print_opcoes()
    opcao = int(input("Escolha uma opção: "))
    option(opcao)

