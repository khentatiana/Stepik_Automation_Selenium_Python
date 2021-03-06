from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\n1.start browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\n1.quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")
        print("\n #1 test_guest_should_see_login_link is done")
        time.sleep(10)

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

        print("\n #2 est_guest_should_see_basket_link_on_the_main_page "
              "ink is done")
        time.sleep(10)

class TestMainPage2():

    def setup_method(self):
        print("\n2.1 start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\n2.2 quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")