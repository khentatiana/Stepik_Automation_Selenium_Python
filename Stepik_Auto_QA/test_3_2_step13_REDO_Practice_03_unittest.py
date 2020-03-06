from selenium import webdriver
import unittest
import time

class TestRegistragionPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

