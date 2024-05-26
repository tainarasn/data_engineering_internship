from eda.models.webscraper import WebScraper
from eda.convert_xlsx import convert_xlsx
import os
import sys

if __name__ ==  "__main__":

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("../eda"))))
    #Base URL
    url = 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html'
    download_dir = os.path.join(os.getcwd(), 'data') #directory downloads

    #Initialize the scraper and get started 
    scraper = WebScraper(url, download_dir)
    scraper.start()