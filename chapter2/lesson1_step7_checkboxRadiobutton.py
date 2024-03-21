from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)

    answer_element = browser.find_element(By.ID, "robotCheckbox")
    answer_element.click()

    answer_element = browser.find_element(By.ID, "robotsRule")
    answer_element.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
