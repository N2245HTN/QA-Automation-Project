from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ── Setup Driver ─────────────────────────────
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

# ─────────────────────────────────────────────
# Example A: Hover Menu
# ─────────────────────────────────────────────
driver.get('https://the-internet.herokuapp.com/hovers')

figures = driver.find_elements(By.CSS_SELECTOR, '.figure')

for i, figure in enumerate(figures):
    actions.move_to_element(figure).perform()
    time.sleep(1)

    captions = driver.find_elements(By.CSS_SELECTOR, '.figcaption h5')
    if i < len(captions):
        print("Revealed:", captions[i].text)

# ─────────────────────────────────────────────
# Example B: Drag and Drop
# ─────────────────────────────────────────────
driver.get('https://the-internet.herokuapp.com/drag_and_drop')

source = driver.find_element(By.ID, 'column-a')
target = driver.find_element(By.ID, 'column-b')

actions.drag_and_drop(source, target).perform()
time.sleep(2)

print("Column A:", driver.find_element(By.ID, 'column-a').text)
print("Column B:", driver.find_element(By.ID, 'column-b').text)

# ─────────────────────────────────────────────
# Example C: Infinite Scroll
# ─────────────────────────────────────────────
driver.get('https://the-internet.herokuapp.com/infinite_scroll')

before = len(driver.find_elements(By.CSS_SELECTOR, '.jscroll-added'))

# Scroll down multiple times
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

after = len(driver.find_elements(By.CSS_SELECTOR, '.jscroll-added'))

print("New paragraphs loaded:", after - before)

# ── Close Browser ─────────────────────────────
driver.quit()