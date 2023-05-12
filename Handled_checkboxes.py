import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://itera-qa.azurewebsites.net/home/automation")

weeks = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")

for i in weeks:
    i.click()
# for i in range(len(weeks)):
#     if weeks[i].text =='monday':
#         weeks[i].click()
#         print(weeks[i].get_attribute("id"))


# for i in weeks:
#     weekend = i.get_attribute('id')
#     if weekend == 'monday' or weekend == 'sunday':
#         i.click()
#         print(i.get_attribute('id'))

# for i in weeks[5:]:
#     i.click()
#     print(i.get_attribute('id'))

# for i in range(len(weeks)):
#     if i < 3:
#         weeks[i].click()
time .sleep(3)
for i in weeks:
    if i.is_selected():
        i.click()



time.sleep(2)
