import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def stop(self):
        self.driver.quit()
