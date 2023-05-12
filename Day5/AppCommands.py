from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\\Application\\Softwares\\WebDriver\\Chrome\\chromewebdriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

title = driver.title
print(f"Title is : {title}")

url = driver.current_url
print(f"url of webpage is : {url}")

page_source = driver.page_source
# print(f"page source is : {page_source}")


