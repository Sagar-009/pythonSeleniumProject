import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://mypage.rediff.com/login/dologin")

driver.find_element(By.XPATH, "//input[@value='Login']").click()

myalert = driver.switch_to.alert
print(myalert.text)
myalert.accept()
time.sleep(5)