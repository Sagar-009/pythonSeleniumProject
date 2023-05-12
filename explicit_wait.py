import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

search = driver.find_element(By.NAME, "q")
search.send_keys("selenium")
search.submit()

wait=WebDriverWait(driver,10)
ele = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
# time.sleep(2)
ele.click()
