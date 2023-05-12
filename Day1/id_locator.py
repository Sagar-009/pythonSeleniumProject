import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\\Application\\Softwares\\WebDriver\\Chrome\\chromewebdriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.pl/index.php")
driver.implicitly_wait(5)

# ID and NAME
# driver.find_element(By.ID, "search_query_top").send_keys("T-SHIRTS")
# driver.find_element(By.NAME, "submit_search").click()

# Linktext / Partial link text
# driver.find_element(By.LINK_TEXT,"Sign in").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Sign").click()

# classname
slider = driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(slider))

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for link in links:
    print(link.text)
    



time.sleep(2)