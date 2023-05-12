import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

parent_window = driver.current_window_handle

search = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
search.send_keys("selenium")
search.submit()

alllinks = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")
print(len(alllinks))

for link in alllinks:
    link.click()

driver.switch_to.window(parent_window)
time.sleep(2)
windowsIDs = driver.window_handles

s = []
for wind in windowsIDs:
    driver.switch_to.window(wind)
    s.append(wind)
    print(driver.title)
print(s)
quit()

time.sleep(5)