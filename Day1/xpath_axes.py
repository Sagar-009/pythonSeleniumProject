import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\\Application\\Softwares\\WebDriver\\Chrome\\chromewebdriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers")
driver.implicitly_wait(5)

# self
# s = driver.find_element(By.XPATH,"//a[contains(text(),'Prime Industries')]/self::a").text
# print(s)  # Prime Industries

# parent
# s = driver.find_element(By.XPATH,"//a[contains(text(),'Prime Industries')]/parent::td").text
# print(s)    # Prime Industries

# childs
# childs = driver.find_elements(By.XPATH," //a[contains(text(),'Prime Industries')]/ancestor::tr/child::td[2]")
# print(len(childs))  #5

# mylist = []
# for i in childs:
#     mylist.append(i.text)
# print(mylist)

# ancestor
# txt_msg = driver.find_element(By.XPATH,' //a[contains(text(),"Prime Industries")]/ancestor::tr').text
# print(txt_msg)

# descendant
# descedant = driver.find_elements(By.XPATH, ' //a[contains(text(),"Prime Industries")]/ancestor::tr/descendant::*')
# print("number of descedant : ",len(descedant))    # number of descedant :  7

# following
# following = driver.find_elements(By.XPATH, ' //a[contains(text(),"Prime Industries")]/ancestor::tr/following::*')
# print("number of following : ",len(following))  # number of following :  14463

# following-sibling
# following_sibling = driver.find_elements(By.XPATH, ' //a[contains(text(),"Prime Industries")]/ancestor::tr/following-sibling::*')
# print("number of following-sibling : ",len(following_sibling))  # number of following-sibling :  1788

# preceding
preceding = driver.find_elements(By.XPATH, ' //a[contains(text(),"Prime Industries")]/ancestor::tr/preceding::*')
print("number of preceding : ",len(preceding))  # number of preceding :  1798

# preceding-sibling
preceding_sibling = driver.find_elements(By.XPATH, ' //a[contains(text(),"Prime Industries")]/ancestor::tr/preceding-sibling::*')
print("number of preceding_sibling : ",len(preceding_sibling))  # number of preceding_sibling :  203


time.sleep(1)