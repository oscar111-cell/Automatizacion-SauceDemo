from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("que abro la página de inicio de sesión")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('inicio sesión con usuario "{username}" y contraseña "{password}"')
def step_login_with_credentials(context, username, password):
    context.login_page.login(username, password)


@when("intento iniciar sesión sin usuario ni contraseña")
def step_login_without_credentials(context):
    # Hacer click directo en Login para disparar validaciones
    context.login_page.submit()


@then("debo ver el inventario")
def step_should_see_inventory(context):
    inv = InventoryPage(context.driver)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    assert inv.is_loaded(), "El inventario no se cargó correctamente tras iniciar sesión."


@then('debo ver el mensaje de error "{expected}"')
def step_should_see_error_message(context, expected):
    # Esperar a que aparezca el contenedor de error
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.error-message-container.error"))
    )
    actual = context.login_page.get_error_text()
    assert expected == actual, f"Mensaje de error esperado: '{expected}', obtenido: '{actual}'"