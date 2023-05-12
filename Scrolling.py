import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)", " ")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixel moved :", value)


# scroll down page till the element is visible
# flag = driver.find_element(By.XPATH, "//td[normalize-space()='India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print('Number of pixel moved :', value)

# scroll down page till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", '')
value = driver.execute_script("return window.pageYOffset;")
print('Number of pixel moved :', value)
time.sleep(2)

# scroll to starting position of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)", '')
value = driver.execute_script("return window.pageYOffset;")
print('Number of pixel moved :', value)
time.sleep(5)