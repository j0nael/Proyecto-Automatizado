from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()


if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver.get("file:///C:/Users/Admin/Documents/GitHub/Proyecto Automatizado/Crud/index.html")

time.sleep(2)


driver.save_screenshot("screenshots/eliminar_01_inicio.png")


driver.find_element(By.ID, "usuario").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)


driver.save_screenshot("screenshots/eliminar_02_login.png")


driver.find_element(By.ID, "nombre").send_keys("Pedro")

time.sleep(1)


driver.save_screenshot("screenshots/eliminar_03_escrito.png")

driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()

time.sleep(2)


driver.save_screenshot("screenshots/eliminar_04_creado.png")


driver.find_element(By.XPATH, "//button[contains(text(),'Eliminar')]").click()

time.sleep(1)


driver.save_screenshot("screenshots/eliminar_05_modal.png")

driver.find_element(By.XPATH, "//button[text()='Sí']").click()

time.sleep(2)

driver.save_screenshot("screenshots/eliminar_06_eliminado.png")

driver.quit()