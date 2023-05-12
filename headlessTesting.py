import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Drivers/chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.add_argument('--headless=new')
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:/Drivers/msedgedriver.exe")
    ops=webdriver.EdgeOptions()
    ops.add_argument('--headless=new')
    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver

def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:/Drivers/geckodriver.exe")
    ops = webdriver.FirefoxOptions()
    ops.add_argument('-headless')
    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver


my_driver = headless_firefox()
my_driver.implicitly_wait(10)
my_driver.get("https://demo.nopcommerce.com/")
print(my_driver.title)
