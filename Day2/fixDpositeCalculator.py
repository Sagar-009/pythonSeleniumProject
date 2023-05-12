from Day2 import XLUtils
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("")

file = "C:/Users/Shrisha/OneDrive/data.xlsx"
sheetName = 'Sheet1'


my_sheet = XLUtils.writeData(file, sheetName, 2, 1, "Selenium")
print(my_sheet)