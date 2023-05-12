import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("05/11/2023")
# time.sleep(5)

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

year = "2022"
month = 'June'

while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and year==yr:
        break
    else:
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()   # next arrow
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click() # previous arrow

dt = "15"

alldates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
print(len(alldates))
for date in alldates:
    if date.text == dt:
        date.click()
        break



time.sleep(5)