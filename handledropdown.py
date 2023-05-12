import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.geodatasource.com/software/country-region-dropdown-menu-demo")


# drpcountry_ele=driver.find_element(By.XPATH, "//select[@country-data-region-id='gds-cr-one']")


drp_country=Select(driver.find_element(By.XPATH, "//select[@country-data-region-id='gds-cr-one']"))
# drp_cnt.select_by_index(2)
# drp_cnt.select_by_value("American Samoa")
# drp_cnt.select_by_visible_text('Angola')
# drp_cnt.select_by_index(5)
# alloption=drp_country.options
# print(len(alloption))
#
# for option in alloption:
#     if option.text == "Argentina":
#         option.click()
#         break

time.sleep(2)