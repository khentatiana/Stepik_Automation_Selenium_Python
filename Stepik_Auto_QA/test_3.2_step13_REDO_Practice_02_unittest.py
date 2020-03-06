from selenium import webdriver
import unittest
import time

class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def fill_form(self, link):







    def tearDown(self):
        self.browser.quit()
