from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\\Application\\Softwares\\WebDriver\\Chrome\\chromewebdriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.implicitly_wait(5)

# is_display
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("display status: ",search_box.is_displayed())


# is_enabled
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("enabled status: ",search_box.is_enabled())

# is_selected

gender_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
gender_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print(f"male gender is selected :{gender_male.is_selected()}")
print(f"female gender is selected :{gender_female.is_selected()}")

#after selecting male gender
print("after selecting male gender")
gender_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
gender_male.click()
gender_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print(f"male gender is selected :{gender_male.is_selected()}")
print(f"female gender is selected :{gender_female.is_selected()}")

# after selecting female gender
print("after selecting female gender")
gender_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
gender_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
gender_female.click()
print(f"male gender is selected :{gender_male.is_selected()}")
print(f"female gender is selected :{gender_female.is_selected()}")

