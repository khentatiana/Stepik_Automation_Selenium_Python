from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

blue_btn = browser.find_element_by_class_name("btn.btn-primary")
blue_btn.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

submit = browser. find_element_by_class_name("btn.btn-primary")
submit.click()


time.sleep(50)
browser.quit()

