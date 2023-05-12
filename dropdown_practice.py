import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://testautomationpractice.blogspot.com/")

# speed_ele = driver.find_element(By.XPATH, "//select[@id='speed']")
speed_ele = Select(driver.find_element(By.XPATH, "//select[@id='products']"))

# time.sleep(2)
# speed_ele.select_by_index(0)

# time.sleep(2)
speed_ele.select_by_value("Microsoft")

time.sleep(2)
# speed_ele.select_by_visible_text("Iphone")
# time.sleep(2)

speed = speed_ele.options
print(len(speed))
