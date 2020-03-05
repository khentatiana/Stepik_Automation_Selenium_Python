from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element_by_class_name("btn.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

browser.quit()

