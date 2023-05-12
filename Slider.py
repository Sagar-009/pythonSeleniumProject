import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/span[1]")
max_slider = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/span[2]")

print("Location of slider before moving ----")
print(min_slider.location)
print(max_slider.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -112, 0).perform()
time.sleep(2)

print("Location of slider after moving ----")
print(min_slider.location)
print(max_slider.location)