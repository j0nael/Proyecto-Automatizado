from selenium import webdriver
import time
import os

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(2)

driver.save_screenshot("screenshots/google.png")

driver.quit()