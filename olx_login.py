from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver_path = 'chromedriver.exe' 
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open OLX
driver.get("https://www.olx.com.pk/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
# Wait and click on Login
time.sleep(3)
login_btn = driver.find_element(By.XPATH, '//span[text()="Login"]')
login_btn.click()

# Wait for modal to load
time.sleep(3)
google_btn = driver.find_element(By.XPATH, '//span[text()="Login with Google"]')
google_btn.click()

# Wait for Google login popup
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))

# Send your email
email_input.send_keys("osamaiq347@gmail.com")
time.sleep(5)

next_btn = driver.find_element(By.XPATH, '//span[text()="Next"]')
next_btn.click()
time.sleep(5)