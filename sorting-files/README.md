# Script de Ordenação de Arquivos em Python

## Descricão
Este script em Python foi desenvolvido para organizar os arquivos dentro de uma pasta com base em suas extensões. Ele percorre o diretorio especificado, identifica a extensão de cada arquivo e os move para subdiretorios correspondentes, criado automaticamente
    
## Requisitos
-  Python 3.10.12

## Uso
1. Certifique-se de ter o Python instlado em sua maquina.

2. Clona o repositorio

```bash
    git clone https://github.com/kadeguilherme/scripts-python.git
``````

3. Navegue até o diretorio do script

```bash
    cd sorting-files
``````

4. Execute o script, fornecendo o caminho do diretorio que deseja organizar
```bash
    cd sorting-files.py /path/of/your/directory
``````

## Exemplo
Suponha que tenha o seguinte diretorio:

    /diretorio_a_organizar
    ├── arquivo1.txt
    ├── arquivo2.py
    ├── arquivo3.txt
    ├── imagem1.jpg
    └── imagem2.png

Apos executar o script, o diretorio será organizado da seguinte maneira:


Aqui está a versão do README com a adição da versão do Python:

markdown
Copy code
# Script de Ordenação de Arquivos em Python

## Descrição
Este script em Python foi desenvolvido para organizar os arquivos dentro de uma pasta com base em suas extensões. Ele percorre o diretório especificado, identifica a extensão de cada arquivo e os move para subdiretórios correspondentes, criados automaticamente.

## Requisitos
- Python 3.10.12

## Uso
1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).
2. Clone ou faça o download deste repositório.

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

3. Navegue até o diretório do script.

    ```bash
    cd nome-do-repositorio
    ```

4. Execute o script, fornecendo o caminho do diretório que deseja organizar.

    ```bash
    python script_ordenacao.py /caminho/do/seu/diretorio
    ```

## Exemplo
Suponha que você tenha o seguinte diretório:

    /diretorio_a_organizar
    ├── arquivo1.txt
    ├── arquivo2.py
    ├── arquivo3.txt
    ├── imagem1.jpg
    └── imagem2.png

yaml
Copy code

Após executar o script, o diretório será organizado da seguinte maneira:

    /diretorio_a_organizar
    ├── txt
    | ├── arquivo1.txt
    | └── arquivo3.txt
    ├── py
    | └── arquivo2.py
    ├── jpg
    | └── imagem1.jpg
    └── png
    └── imagem2.png