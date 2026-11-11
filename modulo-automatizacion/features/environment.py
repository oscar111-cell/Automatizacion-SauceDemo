from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def before_scenario(context, scenario):
    options = Options()
    # options.add_argument("--headless=new")  # Descomenta para headless
    options.add_argument("--window-size=1280,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(5)


def after_scenario(context, scenario):
    # Espera breve para observar el estado final del escenario
    time.sleep(2)
    if getattr(context, "driver", None):
        context.driver.quit()