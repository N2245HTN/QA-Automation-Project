from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

# Example A: iFrame
print("\n===== Example A: iFrame =====")

driver.get("https://the-internet.herokuapp.com/iframe")

iframe = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#mce_0_ifr"))
)

driver.switch_to.frame(iframe)

body = driver.find_element(By.ID, "tinymce")
print("Current text:", body.text)

driver.switch_to.default_content()

print("Page Heading:",
      driver.find_element(By.TAG_NAME, "h3").text)

# Example B: Multiple Windows
print("\n===== Example B: Multiple Windows =====")

driver.get("https://the-internet.herokuapp.com/windows")

original = driver.current_window_handle

print("Windows before click:", len(driver.window_handles))

driver.find_element(By.LINK_TEXT, "Click Here").click()

wait.until(EC.number_of_windows_to_be(2))

print("Windows after click:", len(driver.window_handles))

for handle in driver.window_handles:
    if handle != original:
        driver.switch_to.window(handle)
        break

print("New Window Title:", driver.title)
print("Heading:", driver.find_element(By.TAG_NAME, "h3").text)

driver.close()
driver.switch_to.window(original)

print("Back to Original Window:", driver.title)

# Example C: Nested Frames
print("\n===== Example C: Nested Frames =====")

driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")

driver.switch_to.frame("frame-left")
print("Left Frame:", driver.find_element(By.TAG_NAME, "body").text)

driver.switch_to.parent_frame()

driver.switch_to.frame("frame-middle")
print("Middle Frame:", driver.find_element(By.TAG_NAME, "body").text)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
print("Bottom Frame:", driver.find_element(By.TAG_NAME, "body").text)

driver.quit()