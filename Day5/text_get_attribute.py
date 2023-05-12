import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/maps")
driver.implicitly_wait(10)

search_box = driver.find_element(By.XPATH, "//input[@id='searchboxinput']")
search_box.send_keys("Pune")

search_box_button = driver.find_element(By.XPATH, "//button[@id='searchbox-searchbutton']")
search_box_button.click()
time.sleep(2)

mh = driver.find_element(By.XPATH, "//span[text()='Maharashtra']")
print('result value text : ', mh.text)
print('result value text : ', mh.get_attribute("value"))
print("text result :", search_box.text)
print("text result :", search_box.get_attribute("value"))

time.sleep(7)