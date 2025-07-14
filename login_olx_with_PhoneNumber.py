from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

driver_path = 'chromedriver.exe' 
service = Service(driver_path)
driver = uc.Chrome(service=service)

# Step 1: Open OLX
driver.get("https://www.olx.com.pk/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Step 2: Click on Login
time.sleep(3)
login_btn = driver.find_element(By.XPATH, '//span[text()="Login"]')
login_btn.click()

# Step 3: Click on "Login with Phone"
time.sleep(3)
phone_btn = driver.find_element(By.XPATH, '//span[text()="Login with Phone"]')
phone_btn.click()

# Step 4: Wait for phone number input and send number
time.sleep(3)
actions = ActionChains(driver)
phone_input = wait.until(EC.presence_of_element_located((By.ID, "phone")))
for char in "3475356933":
    actions.send_keys(char)
    actions.perform()
    time.sleep(0.2)

# Step 5: Enter password
time.sleep(3)
psd_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
psd_input.send_keys("Osama@1122")

# Step 6: Click on Log In button
time.sleep(3)
login_submit_btn = driver.find_element(By.XPATH, '//span[text()="Log In"]')
login_submit_btn.click()

time.sleep(10)
driver.quit()
