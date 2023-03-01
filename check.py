from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

driver.maximize_window()
driver.find_element_by_name("q").send_keys("LinkedIn Login")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

driver.find_element_by_partial_link_text("LinkedIn Login").click()
driver.find_element_by_id("username").send_keys("donib.irakihda@gmail.com")
driver.find_element_by_id("password").send_keys("Been0dadkaa")
driver.find_element_by_tag_name("button").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.close()
