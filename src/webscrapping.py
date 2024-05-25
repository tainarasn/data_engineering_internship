import requests
import os

# URL base do diretório de documentos
url_base = 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html'

# Lista de nomes dos documentos (exemplo)
# documentos = ['01_Utilizacao_da_Internet.xlsx', '02_Equipamento_Utlizado_para_Acessar_a_Internet.xlsx', '03_Posse_de_Telefone_Movel_Celular.xlsx']

# # Diretório onde os documentos serão salvos localmente
# diretorio_destino = './'

# # Itera sobre cada documento na lista
# for documento in documentos:
#     url = base_url + documento
    
#     # Faz a requisição GET para o URL do documento
#     response = requests.get(url)
    
#     # Verifica se a requisição foi bem-sucedida
#     if response.status_code == 200:
#         # Define o caminho completo do arquivo local
#         caminho_arquivo = os.path.join(diretorio_destino, documento)
        
#         # Salva o conteúdo do response no arquivo local
#         with open(caminho_arquivo, 'wb') as f:
#             f.write(response.content)
        
#         print(f'Download do arquivo {documento} concluído.')
#     else:
#         print(f'Falha ao baixar o arquivo {documento}. Status code: {response.status_code}')
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def download_arquivo(url_arquivo, nome_arquivo):
    # Faz a requisição GET para o URL do arquivo
    response = requests.get(url_arquivo, stream=True)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Define o caminho completo do arquivo local
        caminho_arquivo = os.path.join('.', nome_arquivo)
        
        # Salva o conteúdo do response no arquivo local
        with open(caminho_arquivo, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        
        print(f'Download do arquivo {nome_arquivo} concluído.')
    else:
        print(f'Falha ao baixar o arquivo {nome_arquivo}. Status code: {response.status_code}')

def extrair_links_e_downloads(url_base, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', class_='jstree-anchor')

    for link in links:
        nome_arquivo = link.text.strip()
        url_arquivo = urljoin(url_base, link['href'])
        
        # Verifica se o link é para um arquivo .xlsx
        if url_arquivo.endswith('.xlsx'):
            download_arquivo(url_arquivo, nome_arquivo)


# Conteúdo HTML da estrutura fornecida
html_content = """
<li role="treeitem" aria-selected="false" aria-level="6" aria-labelledby="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade_anchor" aria-expanded="true" id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade" class="jstree-node jstree-open">
    <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
    <i class="jstree-icon jstree-ocl" role="presentation"></i>
    <a class="jstree-anchor" href="#" tabindex="-1" id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade_anchor">
        <i class="jstree-icon jstree-themeicon" role="presentation"></i>01_Pessoas_de_10_Anos_ou_Mais_de_Idade
    </a>
    <ul role="group" class="jstree-children">
        <li role="treeitem" aria-selected="false" aria-level="7" aria-labelledby="j1_745_anchor" id="j1_745" class="jstree-node jstree-leaf">
            <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
            <i class="jstree-icon jstree-ocl" role="presentation"></i>
            <a class="jstree-anchor" href="/html_dev/arvoreJS/01_Utilizacao_da_Internet.xlsx" tabindex="-1" id="j1_745_anchor">
                <i class="jstree-icon jstree-themeicon jstree-themeicon-custom" role="presentation" style="background-image: url(&quot;/html_dev/arvoreJS/download.png&quot;); background-position: center center; background-size: auto;"></i>01_Utilizacao_da_Internet.xlsx
            </a>
        </li>
        <li role="treeitem" aria-selected="false" aria-level="7" aria-labelledby="j1_746_anchor" id="j1_746" class="jstree-node jstree-leaf">
            <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
            <i class="jstree-icon jstree-ocl" role="presentation"></i>
            <a class="jstree-anchor" href="/html_dev/arvoreJS/02_Equipamento_Utlizado_para_Acessar_a_Internet.xlsx" tabindex="-1" id="j1_746_anchor">
                <i class="jstree-icon jstree-themeicon jstree-themeicon-custom" role="presentation" style="background-image: url(&quot;/html_dev/arvoreJS/download.png&quot;); background-position: center center; background-size: auto;"></i>02_Equipamento_Utlizado_para_Acessar_a_Internet.xlsx
            </a>
        </li>
        <li role="treeitem" aria-selected="false" aria-level="7" aria-labelledby="j1_747_anchor" id="j1_747" class="jstree-node jstree-leaf jstree-last">
            <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
            <i class="jstree-icon jstree-ocl" role="presentation"></i>
            <a class="jstree-anchor" href="/html_dev/arvoreJS/03_Posse_de_Telefone_Movel_Celular.xlsx" tabindex="-1" id="j1_747_anchor">
                <i class="jstree-icon jstree-themeicon jstree-themeicon-custom" role="presentation" style="background-image: url(&quot;/html_dev/arvoreJS/download.png&quot;); background-position: center center; background-size: auto;"></i>03_Posse_de_Telefone_Movel_Celular.xlsx
            </a>
        </li>
    </ul>
</li>
"""

# Chama a função para extrair links e realizar downloads
extrair_links_e_downloads(url_base, html_content)
