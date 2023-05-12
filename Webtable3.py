import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://money.rediff.com/gainers")

rows = driver.find_elements(By.XPATH,"//table[@class='dataTable']//tbody/tr")
print(len(rows))

cols = driver.find_elements(By.XPATH,"//table[@class='dataTable']/thead/tr/th")
print(len(cols ))

count = 0
for r in range(2, len(rows)+1):
    group = driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr["+str(r)+"]/td[2]").text
    if group == "X":
        company = driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[" + str(r) + "]/td[1]").text
        print(company, group)
        count += 1

print("NO of x group company", count)
print("NO of remain group company", (len(rows)-count))