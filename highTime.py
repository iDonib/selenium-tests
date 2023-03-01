from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome browser driver and navigate to the login page
driver = webdriver.Chrome()
driver.get("https://www.example.com/login")

# Enter the login credentials and click on the Login button
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("your_username")
password.send_keys("your_password")

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Wait for the page to load and verify that the user has been logged in successfully
time.sleep(5)

welcome_message = driver.find_element_by_xpath("//h1[contains(text(), 'Welcome')]")
assert welcome_message.text == "Welcome, Your Name!"

# Close the browser window
driver.close()

