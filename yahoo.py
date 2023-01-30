from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Initialize webdriver
driver = webdriver.Firefox()

#Navigate to website
driver.get("https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "Col1-1-HistoricalDataTable-Proxy")))

# Scrape the data from the website
data = driver.find_elements_by_xpath("//table[@id='Col1-1-HistoricalDataTable-Proxy']/tbody/tr")

# Extract the relevant information from the data
for row in data:
    date = row.find_elements_by_xpath(".//td[1]")[0].text
    close_price = row.find_elements_by_xpath(".//td[5]")[0].text
    print(date + " - " + close_price)

# Close the webdriver
driver.quit()

