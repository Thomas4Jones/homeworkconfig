import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from test_action_unittest import SeleniumAction
from test_locator_unittest import *
from test_data_unittest import *
from pathlib import Path

class TestSaucedemoChecks(unittest.TestCase):
    def setUp(self):
        """Настройка перед выполнением каждого теста"""
        current_dir = Path(__file__).resolve().parent
        project_root = current_dir.parent
        gecko_path = project_root / "config" / "geckodriver.exe"
        web_service = Service(gecko_path)
        self.browser = webdriver.Firefox(service=web_service)
        self.browser.get("https://www.saucedemo.com/")
        self.selenium_action = SeleniumAction(self.browser)

    def tearDown(self):
        """Метод для очистки после выполнения каждого теста"""
        self.browser.quit()

    def test_login_successful(self):
        """Проверка входа"""
        self.selenium_action.action_fill_input(locator_field_user_name, data_standard_user)
        self.selenium_action.action_fill_input(locator_field_user_pass, data_password)
        self.selenium_action.action_wait_on_page(2000)
        self.selenium_action.action_click_element(locator_button_login)
        self.selenium_action.action_wait_on_page(1000)
        self.assertIn("https://www.saucedemo.com/inventory.html", self.browser.current_url.lower(), "Ошибка при входе")

    def test_sort_products_successful(self):
        """Проверка сортировки"""
        self.test_login_successful()  # Предварительный вход
        self.selenium_action.action_click_element(locator_sort)
        self.selenium_action.action_select_dropdown_option(locator_sort, "Price (low to high)")
        first_product_id = self.selenium_action.action_get_attribute(locator_sort_first_prod, "id")
        self.selenium_action.action_wait_on_page(1000)
        self.assertEqual(first_product_id, "item_2_img_link", "Ошибка при сортировке")

    def test_buy_product_successful(self):
        """Проверка покупки"""
        self.test_login_successful()  # Предварительный вход
        self.selenium_action.action_click_element(locator_add_cart_product_1)
        self.selenium_action.action_click_element(locator_add_cart_product_2)
        self.selenium_action.action_click_element(locator_shopping_cart)
        self.selenium_action.action_click_element(locator_button_checkout)
        self.selenium_action.action_fill_input(locator_field_first_name, data_first_name)
        self.selenium_action.action_fill_input(locator_field_last_name, data_last_name)
        self.selenium_action.action_fill_input(locator_field_postal_code, data_zip_code)
        self.selenium_action.action_wait_on_page(2000)
        self.selenium_action.action_click_element(locator_button_submit)
        self.selenium_action.action_click_element(locator_button_finish)
        self.selenium_action.action_wait_on_page(1000)
        self.assertIn("https://www.saucedemo.com/checkout-complete.html", self.browser.current_url.lower(), "Ошибка при покупке")

    def test_logout_successful(self):
        """Проверка выхода"""
        self.test_login_successful()  # Предварительный вход
        self.selenium_action.action_click_element(locator_button_menu)
        self.selenium_action.action_click_element(locator_button_logout)
        self.selenium_action.action_wait_on_page(1000)
        self.assertIn("https://www.saucedemo.com/", self.browser.current_url.lower(), "Ошибка при выходе")

if __name__ == "__main__":
    unittest.main()