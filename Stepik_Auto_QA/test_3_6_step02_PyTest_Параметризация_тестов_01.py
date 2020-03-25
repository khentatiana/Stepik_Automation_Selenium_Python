import pytest
from selenium import webdriver
import time

@pytest.fixture()
def browser():
    print("\nstart browser before test...")
    browser = webdriver.Chrome(executable_path="/Users/tatiana/Desktop/PROJECTS/chromedriver")
    yield browser
    time.sleep(2)
    print("\nclose browser after test...")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb", "ko"])
def test_login(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.maximize_window()
    browser.minimize_window()
    time.sleep(2)
    browser.find_element_by_id("login_link").click()
    print(browser.title)
    print(browser.current_url)
    print(browser.current_window_handle)




