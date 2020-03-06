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

        time.sleep(5)

        button = browser.find_element_by_class_name("btn.btn-default").click()


    def test_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)




    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
   unittest.main()
