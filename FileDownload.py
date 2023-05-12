import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Drivers/chromedriver.exe")

    preferences = {"download.default_directory": location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:/Drivers/msedgedriver.exe")

    preferences = {"download.default_directory": location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:/Drivers/geckodriver.exe")
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.download.folderList",2)
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver


my_driver = firefox_setup()
my_driver.implicitly_wait(10)
my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
my_driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").send_keys(Keys.ENTER)
