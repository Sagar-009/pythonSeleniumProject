import time

from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)