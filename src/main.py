from models.webscraper import WebScraper
import os

if __name__ ==  "__main__":

    #Base URL
    url = 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html'
    download_dir = os.path.join(os.getcwd(), 'data') #directory downloads

    #Initialize the scraper and get started 
    scraper = WebScraper(url, download_dir)
    scraper.start()