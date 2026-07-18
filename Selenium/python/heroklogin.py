from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open login page
driver.get("https://the-internet.herokuapp.com/login")

# find username field
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# find password field
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# click login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# wait to see result
time.sleep(3)

# print result message
message = driver.find_element(By.ID, "flash").text
print("Login Result:", message)

# close browser
driver.quit()