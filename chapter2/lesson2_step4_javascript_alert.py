import time

from selenium import webdriver
browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';alert('Robots at work');")


time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()