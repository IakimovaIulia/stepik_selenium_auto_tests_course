import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()