import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

serv_obj = Service("C:\Drivers\Chromedriver/")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://gotranscript.com/text-compare")

input1 = driver.find_element(By.XPATH, "//textarea[@placeholder='Paste one version of the text here.']")
input2 = driver.find_element(By.XPATH, "//textarea[@placeholder='Paste another version of the text here.']")

input1.send_keys("welcome")

act = ActionChains(driver)

# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# act.key_down(Keys.CONTROL)
# act.send_keys('c')
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()

# act.key_down(Keys.CONTROL)
# act.send_keys('v')
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_down(Keys.CONTROL).perform()

driver.find_element(By.XPATH, "//button[@id='recaptcha']").click()

time.sleep(10)