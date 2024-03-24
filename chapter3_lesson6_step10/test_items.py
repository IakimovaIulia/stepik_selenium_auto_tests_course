import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_existence_add_to_basket_btn(browser):
    browser.get(link)
    time.sleep(15)
    add_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(add_button) == 1





