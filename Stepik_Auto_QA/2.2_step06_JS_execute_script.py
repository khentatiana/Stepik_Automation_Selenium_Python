from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

input = browser.find_element_by_id("answer")
input.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radiobtn = browser.find_element_by_id("robotsRule")
radiobtn.click()

#Если мы столкнулись с такой ситуацией, мы можем заставить браузер
# дополнительно проскролить нужный элемент, чтобы он точно стал видимым.
#Делается это с помощью следующего скрипта:
#"return arguments[0].scrollIntoView(true);"

submitbtn = browser.find_element_by_class_name("btn.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", submitbtn)
submitbtn.click()

time.sleep(10)
browser.quit()