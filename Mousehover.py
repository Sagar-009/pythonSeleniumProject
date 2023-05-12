import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj,options=option)
driver.implicitly_wait(10)
driver.get("https://www.magicbricks.com/")
time.sleep(2)
buy = driver.find_element(By.XPATH, "//div[@id='tabBUY']")
rent = driver.find_element(By.XPATH, "//div[@id='tabRENT']")
# rent.click()
act = ActionChains(driver)

act.move_to_element(buy).move_to_element(rent).click().perform()

time.sleep(5)