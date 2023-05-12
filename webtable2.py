import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(10)

driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
time.sleep(10)

no = driver.find_elements(By.XPATH, "//div[@role='rowgroup']/div")
print(len(no))