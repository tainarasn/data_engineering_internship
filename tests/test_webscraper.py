# tests/test_scraper.py

import os
import unittest
from src.modules.webscraper import WebScraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html'
        self.download_dir = os.path.join(os.getcwd(), 'downloads')
        self.scraper = WebScraper(self.url, self.download_dir)

    def tearDown(self):
        #Cleaning after each test, if necessary
        self.scraper.driver.quit()

    def test_start(self):
        #Tests whether the start method executes without errors
        try:
            self.scraper.start()
        except Exception as e:
            self.fail(f"O método start falhou com exceção: {str(e)}")

if __name__ == "__main__":
    unittest.main()
