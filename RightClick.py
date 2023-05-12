import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

rightClick = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(rightClick).perform()

driver.find_element(By.XPATH, "//span[normalize-space()='Edit']").click()
myalert = driver.switch_to.alert
myalert.accept()
time.sleep(5)