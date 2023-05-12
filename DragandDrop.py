import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")



act = ActionChains(driver)
# act.drag_and_drop(src,trg).perform()
time.sleep(2)


for i in range(1,8):
    src = driver.find_element(By.ID, f"box{i}")
    trg = driver.find_element(By.ID, f"box10{i}")
    act.drag_and_drop(src,trg).perform()