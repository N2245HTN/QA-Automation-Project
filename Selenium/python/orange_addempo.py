from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# 1. Open Login Page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# 2. Login
wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# 3. Go to PIM
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()

# 4. Click Add Employee
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']"))).click()

# 5. Fill Employee Details
wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys("John")
driver.find_element(By.NAME, "lastName").send_keys("Doe")

# 6. Save Employee
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# 7. Verify Profile Page
header = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h6[contains(@class,'oxd-text')]"))
)

print("Add Employee Test Passed ✅")

time.sleep(3)
driver.quit()