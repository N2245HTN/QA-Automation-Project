from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')

driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]').click()

alert = wait.until(EC.alert_is_present())

print('Alert text:', alert.text)

alert.accept()

result = wait.until(
    EC.visibility_of_element_located((By.ID, "result"))
).text

print("Result:", result)

input("Press ENTER to close browser...")

driver.quit()