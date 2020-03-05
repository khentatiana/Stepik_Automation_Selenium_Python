from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

flying_button = browser.find_element_by_class_name("trollface.btn.btn-primary")
flying_button.click()

redirect_page = browser.window_handles[1]
assert True

time.sleep(30)
browser.quit()
