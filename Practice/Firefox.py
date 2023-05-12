from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
serv_obj = Service("C:/Drivers/geckodriver.exe")

driver = webdriver.Firefox(service=serv_obj)
# driver.get("https://www.google.co.in/")
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
btn = driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]")
btn.send_keys(Keys.ENTER)

