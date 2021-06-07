from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.implicitly_wait(2)
browser.get(link)

'''Find element with id = robotCheckbox'''
checkbox = browser.find_element_by_id("robotCheckbox")
'''Save attribute "required" to  "checkbox_required"'''
checkbox_required = checkbox.get_attribute("required")
'''Assert that  attribute "required" is exists'''
assert checkbox_required == "true", "Required is NOT present"

people_rule = browser.find_element_by_id("peopleRule")
people_checked = people_rule.get_attribute("checked")

assert people_checked is not None, "People rule is not checked"

robots_rule = browser.find_element_by_id("robotsRule")
robots_checked = robots_rule.get_attribute("checked")

assert robots_checked is None, "Robots rule is not checked"

time.sleep(100)
browser.quit()
