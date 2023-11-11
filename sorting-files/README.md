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