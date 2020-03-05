from selenium import webdriver

link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

#Также можно проскролить всю страницу целиком на строго
#заданное количество пикселей. Эта команда проскроллит страницу
#на 100 пикселей вниз:
#browser.execute_script("window.scrollBy(0, 100);")

#В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:
button = browser.find_element_by_class_name("btn.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

browser.quit()
