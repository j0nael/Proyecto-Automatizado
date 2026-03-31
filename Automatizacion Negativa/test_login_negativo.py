from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Admin/Documents/GitHub/Proyecto Automatizado/Crud/index.html")

driver.save_screenshot("screenshots/login_negativo_01_inicio.png")

driver.find_element(By.ID, "usuario").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("mal123")

driver.save_screenshot("screenshots/login_negativo_02_escrito.png")

driver.find_element(By.TAG_NAME, "button").click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "mensajeLogin"), "Credenciales incorrectas")
)

driver.save_screenshot("screenshots/login_negativo_03_error.png")

driver.quit()