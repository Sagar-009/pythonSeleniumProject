
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")

cookies=driver.get_cookies()
print(len(cookies))

for cookie in cookies:
    print(cookie)


driver.add_cookie({"name":"xyz",'value':"1234"})

cookies=driver.get_cookies()
print(len(cookies))

# for cookie in cookies:
#     print(cookie)

driver.delete_cookie("xyz")
cookies=driver.get_cookies()
print("after delete cookie :",len(cookies))

# for cookie in cookies:
#     print(cookie)

driver.delete_all_cookies()
cookies=driver.get_cookies()
print("after delete cookie :",len(cookies))
# for cookie in cookies:
#     print(cookie)
