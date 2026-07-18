from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.demoblaze.com")

wait = WebDriverWait(driver, 20)

# click first product (you can change index or name)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
)).click()

# wait for product page load
time.sleep(2)

# click Add to cart
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[text()='Add to cart']")
)).click()

# handle alert popup
alert = wait.until(EC.alert_is_present())
alert.accept()

print("Product added to cart")

# go to cart page
driver.find_element(By.ID, "cartur").click()

time.sleep(3)

print("Cart page opened")

driver.quit()