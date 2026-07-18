from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Start Browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Wait object
wait = WebDriverWait(driver, 10)

# Open Website
driver.get("https://www.saucedemo.com/")

# ---------------- LOGIN ----------------
wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Verify Login
wait.until(EC.url_contains("inventory.html"))

# ---------------- ADD TO CART ----------------
wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
).click()

# Open Cart
wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
).click()

# Verify Cart Page
wait.until(EC.url_contains("cart.html"))

# ---------------- CHECKOUT ----------------
wait.until(
    EC.element_to_be_clickable((By.ID, "checkout"))
).click()

# Verify Checkout Page
wait.until(EC.url_contains("checkout-step-one.html"))

# Fill Customer Information
wait.until(
    EC.visibility_of_element_located((By.ID, "first-name"))
).send_keys("John")

driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("44600")

driver.find_element(By.ID, "continue").click()

# Verify Overview Page
wait.until(EC.url_contains("checkout-step-two.html"))

# ---------------- FINISH ORDER ----------------
wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
).click()

# Verify Complete Page
wait.until(EC.url_contains("checkout-complete.html"))

message = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
).text

print("Order Status:", message)

driver.quit()