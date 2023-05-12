import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\\Application\\Softwares\\WebDriver\\Chrome\\chromewebdriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)


# self
# txt = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]/self::button").text
# print(txt)  # Log in

# parent
# txt = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]/parent::div").text
# print(txt)  # Log in

# ancestor
# ansestor = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]/ancestor::form").text
# print(ansestor)

# childs
# childs = driver.find_elements(By.XPATH, "//button[contains(text(),'Log in')]/ancestor::form/child::*")
#
# for x in childs:
#     print(x.text)

# preceding
# preceding = driver.find_elements(By.XPATH, "//input[@type='password']/ancestor::div/descendant::*")
# preceding.click()
# print(preceding)
# for x in preceding:
#     print(x.text)

# self
# txt = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]/self::button").text
# print(txt)  # Log in

# parent
# txt = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]/parent::div").text
# print(txt)  # Log in

# descendant
descendant = driver.find_elements(By.XPATH, "//button[contains(text(),'Log in')]/ancestor::form/descendant::*")

s = []
for txt in descendant:
    s.append(txt)
print(s)

s[7].send_keys("abc")
# time.sleep(1)
# descendant.send_keys('abs')

# s[5].send_keys("xyz")
time.sleep(3)

