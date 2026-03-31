from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Admin/Documents/GitHub/Proyecto Automatizado/Crud/index.html")

time.sleep(2)

driver.find_element(By.ID, "usuario").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")

time.sleep(1)

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

driver.find_element(By.ID, "nombre").clear()

time.sleep(1)
driver.save_screenshot("screenshots/vacio_01_campo_vacio.png")

driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()

time.sleep(2)
driver.save_screenshot("screenshots/vacio_02_error_visible.png")

driver.quit()