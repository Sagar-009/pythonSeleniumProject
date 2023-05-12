import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")

alllinks = driver.find_elements(By.TAG_NAME, 'a')
# print(len(alllinks))

count = 0

for link in alllinks:
    try:
        url = link.get_attribute('href')
    except:
        None

    res = requests.get(url)
    if res.status_code >= 400:
        print(url, "link is dead")
        count += 1
    else:
        print('link is valid')

print("total brokens links is : ", count)

