from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")

def scroll_down(driver, pixels):
    driver.execute_script(f"window.scrollBy(0, {pixels});")
# URL base do diretório de documentos
url = 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html'

try:
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()  
    driver.get(url)
    driver.maximize_window()

    folder_access_internet = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular')))
    folder_access_internet.click()
    print("chegou aqui")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'Acesso_a_internet_e_posse_celular/2015')))

    folder_2015 = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015')
    folder_2015.click()
    print("chegou aqui2")

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados')))

    folder_tables = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados')
    folder_tables.click()
    print("chegou aqui3")
    
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx')))
 
    
    folder_xlsx = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx')
    folder_xlsx.click()
    print("chegou aqui4")

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade')))
    
    folder_persons = driver.find_element(By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade')
    # driver.execute_script("arguments[0].scrollIntoView();",folder_xlsx)
    folder_persons.click()
    print("chegou aqui5")
    
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade')))
    print("consegiu")
    
    scroll_down(driver, 200)
    
    try: 
        link_files = driver.find_elements(By.TAG_NAME, 'a')
        link_file = driver.find_elements(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div/div[2]/ul/li/ul/li[1]/ul/li[6]/ul/li[2]/ul/li[2]/ul/li[1]/ul/li[1]/div')
        for link in link_files:
            if link.get_attribute('href') and link.get_attribute('href').endswith('.xlsx'):
                print('Link encontrado:', link.get_attribute('href'))
            else:
                print('Nada encontrado')
        print(link_file)
    except Exception as e:
        print(f"Erro ao encontrar links: {str(e)}")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    driver.quit()
# try:
#     driver.get(url)
    
#     try:
#         # btn_prosseguir = driver.find_element(By.ID,'cookie-btn')
#         # btn_prosseguir.click()
#         folder_access_internet = driver.find_element(By.ID,'Acesso_a_internet_e_posse_celular')
#         folder_access_internet.click()
#         print("opa")
#         # time.sleep(2)
    
#         folder_2015 = driver.find_element(By.ID,'Acesso_a_internet_e_posse_celular/2015')
#         folder_2015.click()
    
       
    
#         print("opa2")
#         # print(btn_prosseguir)
#         # btn_prosseguir = WebDriverWait(driver, 10).until(
#         #     EC.element_to_be_clickable((By.ID, 'cookie-btn')))
#         # btn_prosseguir.click()
#     except:
#         print("Não foi possível encontrar ou clicar no botão 'Prosseguir'")

#     # # folder_access_internet = driver.find_element(By.LINK_TEXT,'Acesso_a_internet_e_posse_celular')
#     # # folder_access_internet.click()
#     # pasta_acesso_internet = WebDriverWait(driver, 10).until(
#     #     EC.visibility_of_element_located((By.LINK_TEXT, 'Acesso_a_internet_e_posse_celular')))
#     # pasta_acesso_internet.click()
    
#     # time.sleep(2)
    
#     # # folder_2015 = driver.find_element(By.LINK_TEXT,'2015')
#     # # folder_2015.click()
#     # pasta_2015 = WebDriverWait(driver, 10).until(
#     #     EC.visibility_of_element_located((By.LINK_TEXT, '2015')))
#     # pasta_2015.click()
    
#     # time.sleep(2)
    
#     # pasta_tabelas_resultados = WebDriverWait(driver, 10).until(
#     #     EC.visibility_of_element_located((By.LINK_TEXT, 'Tabelas_de_Resultados')))
#     # pasta_tabelas_resultados.click()
#     # # folder_tables = driver.find_element(By.LINK_TEXT,'Tabelas_de_Resultados')
#     # # folder_tables.click()
    
#     # time.sleep(2)
    
#     # # folder_xslx = driver.find_element(By.LINK_TEXT,'xslx')
#     # # folder_xslx.click()
#     # pasta_xlsx = WebDriverWait(driver, 10).until(
#     #     EC.visibility_of_element_located((By.LINK_TEXT, 'xlsx')))
#     # pasta_xlsx.click()
    
#     # time.sleep(2)
    
#     # # folder_persons = driver.find_element(By.LINK_TEXT,'01_Pessoas_de_10_Anos_ou_Mais_de_Idade')
#     # # folder_persons.click()
#     # folder_persons = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'01_Pessoas_de_10_Anos_ou_Mais_de_Idade')))
#     # folder_persons.click()
#     # time.sleep(2)
    
#     # link_files = driver.find_elements(By.TAG_NAME,'a')
    
#     # for link in link_files:
#     #     if link.get_attribute('href').endswith('.xslx'):
#     #         print('Link encontrado:', link.get_attribute('href'))
# finally:
#     driver.quit()
# # Conteúdo HTML da estrutura fornecida
# html_content = """
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
# """

# # Chama a função para extrair links e realizar downloads
