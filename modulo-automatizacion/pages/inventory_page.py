from selenium.webdriver.common.by import By


class InventoryPage:
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self) -> bool:
        try:
            self.driver.find_element(*self.INVENTORY_CONTAINER)
            return "inventory.html" in self.driver.current_url
        except Exception:
            return False