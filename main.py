import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SwagLabsWTD(unittest.TestCase):
    valid_user = "standard_user"
    valid_password = "secret_sauce"

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_password_and_user(self, valid_user=valid_user, valid_password=valid_password):
        # TODO: Valid password and user login
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
        user_name_input = driver.find_element(by="name", value="user-name")
        password_input = driver.find_element(by="name", value="password")
        user_name_input.send_keys(valid_user)
        password_input.send_keys(valid_password)
        password_input.send_keys(Keys.RETURN)
        assert "PRODUCTS"

    def test_wrong_user(self, valid_user=valid_user):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
        user_name_input = driver.find_element(by="name", value="user-name")
        password_input = driver.find_element(by="name", value="password")
        user_name_input.send_keys(valid_user)
        password_input.send_keys("secretsauce")
        password_input.send_keys(Keys.RETURN)
        assert "Epic sadface: Password is required"

    def test_login_logout(self, valid_user=valid_user, valid_password=valid_password):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
        user_name_input = driver.find_element(by="name", value="user-name")
        password_input = driver.find_element(by="name", value="password")
        user_name_input.send_keys(valid_user)
        password_input.send_keys(valid_password)
        password_input.send_keys(Keys.RETURN)
        menu_btn = driver.find_element(by="id", value="react-burger-menu-btn")
        assert menu_btn.is_displayed()
        menu_btn.click()
        logout_btn = driver.find_element(by="id", value="logout_sidebar_link")
        assert logout_btn.is_displayed()
        logout_btn.click()

    def test_sort_products_by_price_lohi(self, valid_user=valid_user, valid_password=valid_password):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
        try:
            user_name_input = driver.find_element(by="name", value="user-name")
            password_input = driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            # TODO: Select Price from low to high
            select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
            select.select_by_value("lohi")
            assert "PRICE (LOW TO HIGH)"

    def test_sort_products_by_price_hilo(self, valid_user=valid_user, valid_password=valid_password):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
        try:
            user_name_input = driver.find_element(by="name", value="user-name")
            password_input = driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            # TODO: Select Price from low to high
            select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
            select.select_by_value("hilo")
            assert "PRICE (HIGH TO LOW)"

        # TODO: Add multiple items to the shopping cart

        # TODO: Add the specific product ‘Sauce Labs Onesie’ to the shopping cart

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
