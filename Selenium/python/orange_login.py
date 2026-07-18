from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 20)

# Enter username
wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
).send_keys("Admin")

# Enter password
driver.find_element(By.NAME, "password").send_keys("admin123")

# Click login button
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
).click()

# Verify dashboard page
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
)

# Final check (URL verification)
assert "dashboard" in driver.current_url

print("Login Test Passed ✅")

driver.quit()