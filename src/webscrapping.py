from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--headless")

def scroll_down(driver, pixels):
    driver.execute_script(f"window.scrollBy(0, {pixels});")
    
# URL base do diretório de documentos
url = 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html'

download_dir = os.path.join(os.getcwd(), 'downloads')
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.maximize_window()
    driver.get(url)
    
    try:
        wait = WebDriverWait(driver, 20)  # Aumentei o tempo de espera para garantir que todos os scripts sejam carregados

        # Aguarde até que o contêiner de cookies esteja presente no DOM
        cookie_container = wait.until(EC.presence_of_element_located((By.ID, "cookie-container")))

        # Aguarde até que o contêiner de cookies tenha a classe "active"
        wait.until(lambda driver: "active" in cookie_container.get_attribute("class"))

        # Aguarde até que o botão dentro do contêiner esteja visível e clicável
        cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "cookie-btn")))

        # Verifique se o botão está visível na tela
        wait.until(EC.visibility_of(cookie_button))

        # Use JavaScript para clicar no botão
        driver.execute_script("arguments[0].click();", cookie_button)
        print("Cookie aceito!")
    except TimeoutException:
        print("O tempo de espera terminou e o botão não estava disponível.")
    except Exception as e:
        print(f"Erro ao tentar clicar no botão: {e}")
        
        
    folder_access_internet = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular')))
    folder_access_internet.click()
    print("Acesso_a_internet_e_posse_celular")
    time.sleep(5)
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'Acesso_a_internet_e_posse_celular/2015')))

    folder_2015 = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015')
    folder_2015.click()
    print("2015")
    time.sleep(5)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados')))

    folder_tables = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados')
    folder_tables.click()
    print("Tabelas_de_Resultados")
    time.sleep(5)
    scroll_down(driver, 300)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx')))
 
    
    folder_xlsx = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx')
    folder_xlsx.click()
    print("xlsx")
    time.sleep(5)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade')))
    
    folder_persons = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade')
    folder_persons.click()
    print("01_Pessoas_de_10_Anos_ou_Mais_de_Idade")
    time.sleep(5)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade')))
    print("consegiu")
    
    time.sleep(15)
    
    download_links = ['j1_745_anchor', 'j1_746_anchor', 'j1_747_anchor']

    for link_id in download_links:
        link_element = driver.find_element(By.ID, link_id)
        link_element.click()
        print(f"Baixando arquivo: {link_id}")
        time.sleep(2)  # Esperar um pouco para garantir que o download seja iniciado

    print("Todos os links foram clicados e os downloads devem ter iniciado.")
    

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    driver.quit()

# <li role="treeitem" aria-selected="false" aria-level="6" aria-labelledby="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade_anchor" aria-expanded="true" id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade" class="jstree-node jstree-open">
#     <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
#     <i class="jstree-icon jstree-ocl" role="presentation"></i>
#     <a class="jstree-anchor" href="#" tabindex="-1" id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade_anchor">
#         <i class="jstree-icon jstree-themeicon" role="presentation"></i>01_Pessoas_de_10_Anos_ou_Mais_de_Idade
#     </a>
#     <ul role="group" class="jstree-children">
#         <li role="treeitem" aria-selected="false" aria-level="7" aria-labelledby="j1_745_anchor" id="j1_745" class="jstree-node jstree-leaf">
#             <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
#             <i class="jstree-icon jstree-ocl" role="presentation"></i>
#             <a class="jstree-anchor" href="/html_dev/arvoreJS/01_Utilizacao_da_Internet.xlsx" tabindex="-1" id="j1_745_anchor">
#                 <i class="jstree-icon jstree-themeicon jstree-themeicon-custom" role="presentation" style="background-image: url(&quot;/html_dev/arvoreJS/download.png&quot;); background-position: center center; background-size: auto;"></i>01_Utilizacao_da_Internet.xlsx
#             </a>
#         </li>
#         <li role="treeitem" aria-selected="false" aria-level="7" aria-labelledby="j1_746_anchor" id="j1_746" class="jstree-node jstree-leaf">
#             <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
#             <i class="jstree-icon jstree-ocl" role="presentation"></i>
#             <a class="jstree-anchor" href="/html_dev/arvoreJS/02_Equipamento_Utlizado_para_Acessar_a_Internet.xlsx" tabindex="-1" id="j1_746_anchor">
#                 <i class="jstree-icon jstree-themeicon jstree-themeicon-custom" role="presentation" style="background-image: url(&quot;/html_dev/arvoreJS/download.png&quot;); background-position: center center; background-size: auto;"></i>02_Equipamento_Utlizado_para_Acessar_a_Internet.xlsx
#             </a>
#         </li>
#         <li role="treeitem" aria-selected="false" aria-level="7" aria-labelledby="j1_747_anchor" id="j1_747" class="jstree-node jstree-leaf jstree-last">
#             <div unselectable="on" role="presentation" class="jstree-wholerow">&nbsp;</div>
#             <i class="jstree-icon jstree-ocl" role="presentation"></i>
#             <a class="jstree-anchor" href="/html_dev/arvoreJS/03_Posse_de_Telefone_Movel_Celular.xlsx" tabindex="-1" id="j1_747_anchor">
#                 <i class="jstree-icon jstree-themeicon jstree-themeicon-custom" role="presentation" style="background-image: url(&quot;/html_dev/arvoreJS/download.png&quot;); background-position: center center; background-size: auto;"></i>03_Posse_de_Telefone_Movel_Celular.xlsx
#             </a>
#         </li>
#     </ul>
# </li>
