from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/wait2.html"

browser = webdriver.Chrome()
browser.get(link)

hello = WebDriverWait(browser, 1).until(
       EC.text_to_be_present_in_element((By.ID,"container"), "Hello!")
)
button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
)

button.click()
message = browser.find_element_by_id("verify_message")

assert "Verification was successful!" in message.text

browser.quit()

