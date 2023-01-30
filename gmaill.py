from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

print("sample test started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.delete_all_cookies()

driver.get("https://www.gmail.com/")

driver.find_element(By.CLASS_NAME, "whs0nd").send_keys("binod66560@gmail.com")

time.sleep(2)

driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()

time.sleep(3)

driver.find_element(By.CLASS_NAME, "whsOnd zHQkBf").send_keys("Been0dadka")

time.sleep(3)

driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")

time.sleep(3)

driver.close()

print("testing completed")