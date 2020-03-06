import unittest
from selenium import webdriver
import time


class RegistrationTests(unittest.TestCase):
    def test_positive(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        browser.find_element_by_xpath("//input[@placeholder='Input your last name']") \
            .send_keys("Petrov")
        browser.find_element_by_class_name("form-control.third").send_keys("ivan@gmail.com")

        button = browser.find_element_by_class_name("btn.btn-default")
        button.click()

        time.sleep(1)

        welcome_text_element = browser.find_elements_by_tag_name("h1")
        welcome_text = welcome_text_element[0].text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration is FAILED")
        browser.quit()

    def test_negative(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        input1 = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']")
        input2.send_keys("Simrnov")

        input3 = browser.find_element_by_class_name("form-control.third")
        input3.send_keys("email@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        welcome_text_element = browser.find_elements_by_tag_name("h1")
        welcome_text = welcome_text_element[0].text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration is FAILED")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
