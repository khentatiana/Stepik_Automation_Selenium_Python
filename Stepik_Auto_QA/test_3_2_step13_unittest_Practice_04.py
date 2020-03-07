from selenium import webdriver
import unittest
import time

#unittest does not work without "self". I deleted from here all "self"
class TestRegistragionPage(unittest.TestCase):

    def setUp():
        browser = webdriver.Chrome()

    def fill_form(link):
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element_by_class_name("form-control.first").send_keys("Tanya")
        browser.find_element_by_class_name("form-control.second").send_keys("Khen")
        browser.find_element_by_class_name("form-control.third").send_keys("t@gmail.com")
        time.sleep(3)
        button = browser.find_element_by_class_name("btn.btn-default").click()

        welcome_text_elem = browser.find_elements_by_tag_name("h1")
        welcome_text = welcome_text_elem[0].text
        return welcome_text

    def test_registration_positive():
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = fill_form(link)

        assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_negative():
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = fill_form(link)

        assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown():
        browser.quit()

if __name__ == "__main__":
    unittest.main()
