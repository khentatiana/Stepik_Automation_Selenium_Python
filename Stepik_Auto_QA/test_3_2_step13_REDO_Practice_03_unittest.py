from selenium import webdriver
import unittest
import time

class TestRegistragionPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def fillout_form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element_by_class_name("form-control.first").send_keys("Tanya")
        browser.find_element_by_class_name("form-control.second").send_keys("Khen")
        browser.find_element_by_class_name("form-control.third").send_keys("t@gmail.com")
        time.sleep(11)
        button = browser.find_element_by_class_name("btn.btn-default").click()

        time.sleep(1)

        welcome_text_elem = browser.find_elements_by_tag_name("h1")
        welcome_text = welcome_text_elem[0].text
        return welcome_text

        print(welcome_text)

     def test_registration_positive(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fillout_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_negative(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fillout_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
