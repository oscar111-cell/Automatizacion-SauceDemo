from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_BANNER = (By.CSS_SELECTOR, "div.error-message-container.error")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_username(self, username: str):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def set_password(self, password: str):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        self.set_username(username)
        self.set_password(password)
        self.submit()

    def get_error_text(self) -> str:
        try:
            return self.driver.find_element(*self.ERROR_BANNER).text.strip()
        except NoSuchElementException:
            return ""