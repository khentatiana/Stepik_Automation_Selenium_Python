from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("ivan@email.com")
    input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("1273435")
    input5 = browser.find_element(By.XPATH,"/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Москва")
    time.sleep(5)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)


    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()