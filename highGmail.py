from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome browser driver and navigate to the Gmail login page
driver = webdriver.Chrome()
driver.get("https://www.gmail.com")

# Enter the email address and click on the Next button
email_input = driver.find_element_by_name("identifier")
email_input.send_keys("on.screen.keyboards@gmail.com")
email_input.send_keys(Keys.ENTER)

# Wait for the page to load and enter the password
password_input = driver.find_element_by_name("password")
password_input.send_keys("Been0dadkaa")
password_input.send_keys(Keys.ENTER)

# Wait for the page to load and verify that the user has been logged in successfully
assert "Inbox" in driver.title

# Close the browser window
driver.close()

