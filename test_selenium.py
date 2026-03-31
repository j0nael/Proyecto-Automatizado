import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

URL = "file:///C:/Users/Admin/Documents/GitHub/Proyecto Automatizado/Crud/index.html"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    yield driver
    driver.quit()

# 🔐 LOGIN EXITOSO
def test_login_exitoso(driver):
    driver.get(URL)
    time.sleep(2)

    driver.save_screenshot("screenshots/login_01_vacio.png")

    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")

    driver.save_screenshot("screenshots/login_02_escrito.png")

    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    driver.save_screenshot("screenshots/login_03_exitoso.png")

    assert "CRUD de Usuarios" in driver.page_source

# ❌ LOGIN NEGATIVO
def test_login_negativo(driver):
    driver.get(URL)

    driver.save_screenshot("screenshots/login_negativo_01_inicio.png")

    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("mal123")

    driver.save_screenshot("screenshots/login_negativo_02_escrito.png")

    driver.find_element(By.TAG_NAME, "button").click()

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "mensajeLogin"), "Credenciales incorrectas")
    )

    driver.save_screenshot("screenshots/login_negativo_03_error.png")

    assert "Credenciales incorrectas" in driver.page_source

# ➕ CREAR USUARIO
def test_crear_usuario(driver):
    driver.get(URL)
    time.sleep(2)

    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    driver.save_screenshot("screenshots/crear_01_vacio.png")

    driver.find_element(By.ID, "nombre").send_keys("Juan")

    driver.save_screenshot("screenshots/crear_02_escrito.png")

    driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()
    time.sleep(2)

    driver.save_screenshot("screenshots/crear_03_creado.png")

    assert "Juan" in driver.page_source

# ✏️ EDITAR USUARIO
def test_editar_usuario(driver):
    driver.get(URL)
    time.sleep(2)

    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    driver.find_element(By.ID, "nombre").send_keys("Luis")
    driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()

    time.sleep(2)
    driver.save_screenshot("screenshots/editar_01_creado.png")

    driver.find_element(By.XPATH, "//button[contains(text(),'Editar')]").click()
    time.sleep(1)

    campo = driver.find_element(By.ID, "nombre")
    campo.clear()
    campo.send_keys("Jonathan")

    driver.save_screenshot("screenshots/editar_02_editando.png")

    driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()
    time.sleep(2)

    driver.save_screenshot("screenshots/editar_03_editado.png")

    assert "Jonathan" in driver.page_source

# 🗑️ ELIMINAR USUARIO
# 🗑️ ELIMINAR USUARIO
def test_eliminar_usuario(driver):
    driver.get(URL)
    time.sleep(2)

    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    driver.find_element(By.ID, "nombre").send_keys("Pedro")
    driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()

    time.sleep(2)
    driver.save_screenshot("screenshots/eliminar_01_creado.png")

    # click eliminar
    driver.find_element(By.XPATH, "//button[contains(text(),'Eliminar')]").click()
    time.sleep(1)

    # click botón "Sí"
    driver.find_element(By.XPATH, "//button[text()='Sí']").click()

    time.sleep(2)
    driver.save_screenshot("screenshots/eliminar_02_eliminado.png")

    assert "Pedro" not in driver.page_source
# 🚫 CAMPO VACÍO
def test_campo_vacio(driver):
    driver.get(URL)
    time.sleep(2)

    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    driver.find_element(By.ID, "nombre").clear()
    driver.save_screenshot("screenshots/vacio_01.png")

    driver.find_element(By.XPATH, "//button[contains(text(),'Agregar')]").click()
    time.sleep(2)

    driver.save_screenshot("screenshots/vacio_02.png")

    assert True  # solo validamos que no crashee