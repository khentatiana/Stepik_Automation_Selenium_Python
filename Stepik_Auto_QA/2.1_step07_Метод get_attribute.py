from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radiobtn = browser.find_element_by_id("robotsRule")
radiobtn.click()

submitbtn = browser.find_element_by_class_name("btn.btn-default")
submitbtn.click()

time.sleep(10)
browser.quit()
