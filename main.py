import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# TODO: Clean Code.
class SwagLabsWTD(unittest.TestCase):
    valid_user = "standard_user"
    valid_password = "secret_sauce"

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title

    def test_valid_password_and_user(self, valid_user=valid_user, valid_password=valid_password):
        user_name_input = self.driver.find_element(by="name", value="user-name")
        password_input = self.driver.find_element(by="name", value="password")
        user_name_input.send_keys(valid_user)
        password_input.send_keys(valid_password)
        password_input.send_keys(Keys.RETURN)
        assert "PRODUCTS"

    def test_wrong_user(self, valid_user=valid_user):
        user_name_input = self.driver.find_element(by="name", value="user-name")
        password_input = self.driver.find_element(by="name", value="password")
        user_name_input.send_keys(valid_user)
        password_input.send_keys("secretsauce")
        password_input.send_keys(Keys.RETURN)
        assert "Epic sadface: Password is required"

    def test_login_logout(self, valid_user=valid_user, valid_password=valid_password):
        try:
            user_name_input = self.driver.find_element(by="name", value="user-name")
            password_input = self.driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            menu_btn = self.driver.find_element(by="id", value="react-burger-menu-btn")
            assert menu_btn.is_displayed()
            menu_btn.click()
            logout_btn = self.driver.find_element(by="id", value="logout_sidebar_link")
            assert logout_btn.is_displayed()
            logout_btn.click()

    def test_sort_products_by_price_lohi(self, valid_user=valid_user, valid_password=valid_password):
        try:
            user_name_input = self.driver.find_element(by="name", value="user-name")
            password_input = self.driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
            select.select_by_value("lohi")
            assert "PRICE (LOW TO HIGH)"

    def test_sort_products_by_price_hilo(self, valid_user=valid_user, valid_password=valid_password):
        try:
            user_name_input = self.driver.find_element(by="name", value="user-name")
            password_input = self.driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
            select.select_by_value("hilo")
            assert "PRICE (HIGH TO LOW)"

    def test_add_multiple_items(self, valid_user=valid_user, valid_password=valid_password):
        try:
            user_name_input = self.driver.find_element(by="name", value="user-name")
            password_input = self.driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
            self.driver.find_element(By.NAME, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
            self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
            shop_bag = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert shop_bag.text == "3"

    def test_add_specific_item(self, valid_user=valid_user, valid_password=valid_password):
        try:
            user_name_input = self.driver.find_element(by="name", value="user-name")
            password_input = self.driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
            self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
            inventory_text = self.driver.find_element(By.CLASS_NAME, "inventory_item_name")
            assert inventory_text.text == "Sauce Labs Onesie"

    def test_complete_purchase(self, valid_user=valid_user, valid_password=valid_password):
        try:
            user_name_input = self.driver.find_element(by="name", value="user-name")
            password_input = self.driver.find_element(by="name", value="password")
            user_name_input.send_keys(valid_user)
            password_input.send_keys(valid_password)
            password_input.send_keys(Keys.RETURN)
        finally:
            self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
            self.driver.find_element(By.NAME, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
            self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
            self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
            self.driver.find_element(by="name", value="checkout").click()
            self.driver.find_element(by="name", value="firstName").send_keys("Luis")
            self.driver.find_element(by="name", value="lastName").send_keys("Romo")
            self.driver.find_element(by="name", value="postalCode").send_keys("45079")
            self.driver.find_element(by="name", value="continue").click()
            self.driver.find_element(by="name", value="finish").click()
            final_order = self.driver.find_element(By.CLASS_NAME, "complete-header")
            assert final_order.text == "THANK YOU FOR YOUR ORDER"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
