from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import os
import time
import pandas as pd
import sys
from eda.convert_xlsx import convert_xlsx


class WebScraper:
    
    #constructor
    def __init__(self, url, download_dir):
        self.url = url
        self.download_dir = download_dir
        self.driver = self._initialize_driver()

    #settings driver
    def _initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {
            'download.default_directory': self.download_dir,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        })
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    #scroll to fit element on screen
    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    #click the PROSSEGUIR button to accept cookies
    def accept_cookies(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            
            #checks that the container is visible and acessible through the active class
            cookie_container = wait.until(EC.presence_of_element_located((By.ID, "cookie-container")))
            wait.until(lambda driver: "active" in cookie_container.get_attribute("class"))
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "cookie-btn")))
            
             #check if the button is visible
            wait.until(EC.visibility_of(cookie_button))
            self.driver.execute_script("arguments[0].click();", cookie_button)
            print("Cookie aceito!")

        except TimeoutException:
            print("O tempo de espera terminou e o botão não estava disponível.")
        except Exception as e:
            print(f"Erro ao tentar clicar no botão: {e}")

    #navigating between folders
    def navigate_to_folder(self, folder_id):
        try:
            folder_element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, folder_id)))
            folder_element.click()
            print(f"Navegando para: {folder_id}")
            time.sleep(5)
        except Exception as e:
            print(f"Erro ao tentar navegar para a pasta: {folder_id}, {e}")


    def convert_xlsx(self, xlsx_file, csv_file,filename):
        try:
            base_dir = self.download_dir
            csv_dir = os.path.join(base_dir,'converted', filename)
            if not os.path.exists(csv_dir):
                os.makedirs(csv_dir)

           
            # Upload the XLSX file
            xls = pd.ExcelFile(xlsx_file)

            
            # Iterate over the sheets in the XLSX file
            for sheet_name in xls.sheet_names:
                #Read spreadsheet as DataFrame
                df = pd.read_excel(xls, sheet_name=sheet_name)

                #CSV file name
                csv_file = os.path.join(csv_dir, f"{sheet_name}.csv")

                #Save the DataFrame as CSV
                df.to_csv(csv_file, index=False)
                print(f"Convertido: {sheet_name} para {csv_file}")
        except Exception as e:
            print(f"Erro ao converter arquivo: {e}")
            
            
    def download_files(self, download_links):
        try:
            for link_info in download_links:
                link_id, file_name = link_info  # Obtem o ID do link e o nome do arquivo
                
                link_element = self.driver.find_element(By.ID, link_id)
                link_element.click()
                print(f"Baixando arquivo: {file_name}")
                time.sleep(2)  # Wait a bit to ensure the download starts
                
                xlsx_filename = f"{file_name}.xlsx"
                xlsx_path = os.path.join(self.download_dir, xlsx_filename)
                csv_filename = f"{file_name}.csv"
                csv_path = os.path.join(self.download_dir, csv_filename)
                
                self.convert_xlsx(xlsx_path, csv_path,file_name)
                
            print("Todos os links foram clicados e os downloads devem ter iniciado.")
        except Exception as e:
            print(f"Erro ao tentar baixar os arquivos: {e}")
            
    #operating flow
    def start(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)

            # accept cookies
            self.accept_cookies()

            # Navigate to the desired folders
            self.navigate_to_folder('Acesso_a_internet_e_posse_celular')
            self.navigate_to_folder('Acesso_a_internet_e_posse_celular/2015')
            self.navigate_to_folder('Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados')
            self.scroll_down(200)
            self.navigate_to_folder('Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx')
            self.navigate_to_folder('Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade')

            # css_selectors links
            download_links = [
            ('j1_745_anchor', '01_Utilizacao_da_Internet'),
            ('j1_746_anchor', '02_Equipamento_Utlizado_para_Acessar_a_Internet'),
            ('j1_747_anchor', '03_Posse_de_Telefone_Movel_Celular')
    ]
            self.download_files(download_links)

        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")

        finally:
            self.driver.quit()


