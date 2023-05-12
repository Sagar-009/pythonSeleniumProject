from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("")

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

for link in links:
    print(link.text)