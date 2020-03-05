from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"
def calc(x, y):
      return x + y

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
x = int(num1.text)

num2 = browser.find_element_by_id("num2")
y = int(num2.text)

sum = str(x + y)
print(sum)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(sum)

submitbtn = browser.find_element_by_class_name("btn.btn-default")
submitbtn.click()

time.sleep(5)
browser.quit()