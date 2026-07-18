from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome
driver = webdriver.Chrome()

try:
    # Open page
    driver.get("https://the-internet.herokuapp.com/login")

    # Maximize window
    driver.maximize_window()

    # Wait until username field is visible
    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    password = driver.find_element(By.ID, "password")

    # Enter credentials
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    # Click login button
    login_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_btn.click()

    # Wait for success message
    flash_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    print("Login Result:")
    print(flash_message.text)

    input("Press Enter to close the browser...")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()