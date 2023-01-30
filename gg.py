from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# create a new Firefox browser instance
driver = webdriver.Chrome()

# navigate to the Gmail login page
driver.get("https://gmail.com")

# find the email field and enter the email address
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys("binod66560@gmail.com")
email_field.send_keys(Keys.RETURN)

# find the password field and enter the password
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys("Been0dadka")
password_field.send_keys(Keys.RETURN)

