from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.demoblaze.com")

wait = WebDriverWait(driver, 20)

# wait & click login button
wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

# wait for modal fields properly
wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))

# input username/password
driver.find_element(By.ID, "loginusername").send_keys("testuser")
driver.find_element(By.ID, "loginpassword").send_keys("testpass")

# small delay (important for modal rendering)
time.sleep(1)

# click login button inside modal
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Log in')]")
)).click()

time.sleep(5)

print("Login attempt done")

driver.quit()