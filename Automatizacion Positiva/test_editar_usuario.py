from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver.get("file:///C:/Users/Admin/Documents/GitHub/Proyecto Automatizado/Crud/index.html")

time.sleep(2)

driver.find_element(By.ID, "usuario").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)
driver.find_element(By.ID, "nombre").send_keys("Luis")


driver.save_screenshot("screenshots/editar_01_escrito.png")

driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()

time.sleep(2)


driver.save_screenshot("screenshots/editar_02_creado.png")


driver.find_element(By.XPATH, "//button[contains(text(),'Editar')]").click()

time.sleep(1)


driver.save_screenshot("screenshots/editar_03_modo_edicion.png")


campo = driver.find_element(By.ID, "nombre")
campo.clear()
campo.send_keys("Jonathan")

driver.save_screenshot("screenshots/editar_04_nombre_modificado.png")

driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()

time.sleep(3)

driver.save_screenshot("screenshots/editar_05_usuario_editado.png")

driver.quit()