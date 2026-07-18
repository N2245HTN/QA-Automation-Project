from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open webpage
driver.get("https://the-internet.herokuapp.com/login")

# Locate elements by IDa
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

# Examples of CSS Selectors (for learning)
username_css1 = driver.find_element(By.CSS_SELECTOR, "#username")
username_css2 = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
username_css3 = driver.find_element(By.CSS_SELECTOR, "form#login input:first-of-type")

# Login button
btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

# Find all links on the page
links = driver.find_elements(By.CSS_SELECTOR, "a")

# Print link text and URL
for link in links:
    print(link.text, "->", link.get_attribute("href"))

driver.quit()