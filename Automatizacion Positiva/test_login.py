from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Admin/Documents/GitHub/Proyecto Automatizado/Crud/index.html")

time.sleep(2)


driver.save_screenshot("screenshots/login_01_vacio.png")

driver.find_element(By.ID, "usuario").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")

time.sleep(1)


driver.save_screenshot("screenshots/login_02_escrito.png")


driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)


driver.save_screenshot("screenshots/login_03_exitoso.png")

driver.quit()