from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("Sample test started")

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("donib")
time.sleep(3)

driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
time.sleep(3)

driver.close()

print("sample test completed")