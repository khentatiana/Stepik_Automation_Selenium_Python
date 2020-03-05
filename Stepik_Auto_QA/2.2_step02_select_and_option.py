from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"


browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
x = int(num1.text)

num2 = browser.find_element_by_id("num2")
y = int(num2.text)
print (x + y)
sum = str(x + y)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(sum)

submit_btn = browser.find_element_by_class_name("btn.btn-default")
assert True
submit_btn.click()

time.sleep(30)
browser.quit()
