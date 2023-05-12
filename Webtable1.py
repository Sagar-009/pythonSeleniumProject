from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
cols = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
# print("no of rows:",rows,"no of cols:",cols)

data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# for r in range(2,len(rows)+1):
#     for c in range(1,len(cols)+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(f"{data}",end="     ")
#     print()


for r in range(2,len(rows)):
    author = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author == 'Mukesh':
        bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookname, author, price)