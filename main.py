import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# TODO: Clean Code.
class SwagLabsWTD(unittest.TestCase):
    valid_user = "standard_user"
    valid_password = "secret_sauce"

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_password_and_user(self, valid_user=valid_user, valid_password=valid_password):
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
            select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
            select.select_by_value("hilo")
            assert "PRICE (HIGH TO LOW)"

    def test_add_multiple_items(self, valid_user=valid_user, valid_password=valid_password):
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
            driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
            driver.find_element(By.NAME, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
            driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
            shop_bag = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert shop_bag.text == "3"

    def test_add_specific_item(self, valid_user=valid_user, valid_password=valid_password):
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
            driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
            driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
            inventory_text = driver.find_element(By.CLASS_NAME, "inventory_item_name")
            assert inventory_text.text == "Sauce Labs Onesie"

    def test_complete_purchase(self, valid_user=valid_user, valid_password=valid_password):
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
            driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
            driver.find_element(By.NAME, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
            driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
            driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
            driver.find_element(by="name", value="checkout").click()
            driver.find_element(by="name", value="firstName").send_keys("Luis")
            driver.find_element(by="name", value="lastName").send_keys("Romo")
            driver.find_element(by="name", value="postalCode").send_keys("45079")
            driver.find_element(by="name", value="continue").click()
            driver.find_element(by="name", value="finish").click()
            final_order = driver.find_element(By.CLASS_NAME, "complete-header")
            assert final_order.text == "THANK YOU FOR YOUR ORDER"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
