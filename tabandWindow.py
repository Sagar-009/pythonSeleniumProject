import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import os

from selenium.webdriver.common.by import By

serv_obj = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)


# register = Keys.CONTROL+Keys.ENTER
# driver.find_element(By.LINK_TEXT, "Register").send_keys(register)
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://demo.nopcommerce.com/")

# open a new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://demo.nopcommerce.com/")

time.sleep(5)