import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


driver.find_element(By.XPATH, "//input[@id='departon']").click()

month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
month.select_by_visible_text("Sep")

# time.sleep(2)
yr = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
yr.select_by_visible_text("2023")

alldates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for date in alldates:
    if date.text == '30':
        date.click()
        break


print(driver.find_element(By.XPATH, "//input[@id='departon']").get_attribute("value"))
time.sleep(2)





# driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

time.sleep(5)