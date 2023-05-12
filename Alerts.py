import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()

alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys('selenium')
time.sleep(7)
# alert_window.accept() # Result :  You entered: selenium
alert_window.dismiss() # Result :  You entered: null
time.sleep(2)


result_text = driver.find_element(By.XPATH, "//p[@id='result']")
print("Result : ", result_text.text)
