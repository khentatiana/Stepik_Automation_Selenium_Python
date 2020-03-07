from selenium import webdriver
import unittest
import time

class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element_by_class_name("form-control.first").send_keys("Tanya")
        browser.find_element_by_class_name("form-control.second").send_keys("Khen")
        browser.find_element_by_class_name("form-control.third").send_keys("tkhen@gmail.com")

        button = browser.find_element_by_class_name("btn.btn-default").click()

        # ждем загрузки страницы, not necessary because browser.implicitly_wait(5) in line 11 already exist
        time.sleep(1)

        welcome_text_elem = browser.find_elements_by_tag_name("h1")
        welcome_text = welcome_text_elem[0].text
        return welcome_text

    def test_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_failed(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
   unittest.main()
