from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Tanya")

input2 = browser.find_element_by_xpath("//*[@placeholder = 'Enter last name']")
input2.send_keys("Kh")

input3 = browser.find_element_by_name("email")
input3.send_keys("tkh@gmail.com")

file_to_upload = browser.find_element_by_name("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла.
                                                            # Place file in the same folder as current script

file_to_upload.send_keys(file_path)

submit = browser.find_element_by_class_name("btn.btn-primary")
submit.click()


time.sleep(30)
browser.quit()
