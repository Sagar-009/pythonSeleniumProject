import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# windowid=driver.current_window_handle
# print("current window id is : ", windowid)   # current window id is :  104FF95472A3D9BEFFAD7099CADA07FC
                                            # current window id is :  1613CF3D8D50B887F0FBA301A9BFF6D9

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

windowIDs = driver.window_handles

# parent_window_id = windowIDs[0]
# child_window_id = windowIDs[1]

# driver.switch_to.window(child_window_id)
# print(driver.title)
#
# driver.switch_to.window(parent_window_id)
# print(driver.title)

# print(parent_window_id, child_window_id)

# for windid in windowIDs:
#     driver.switch_to.window(windid)
#     print(driver.title)


for windid in windowIDs:
    driver.switch_to.window(windid)
    if driver.title == "OrangeHRM":
        driver.close()