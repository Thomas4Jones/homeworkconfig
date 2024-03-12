import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config.action import SeleniumAction
from test_saucedemo.locator import *
from test_saucedemo.test_data import *

@pytest.fixture
def browser():
    gecko_path = r"../../../config/geckodriver.exe"
    web_service = Service(gecko_path)
    driver = webdriver.Firefox(service=web_service)
    yield driver

class TestSaucedemo:
    @pytest.fixture
    def login(self, browser):
        """Вход"""
        browser.get(data_web_adres)
        selenium_helper = SeleniumAction(browser)
        SeleniumAction.action_fill_input_static(browser, locator_field_user_name, data_standard_user)
#        input_field_user = browser.find_element(*locator_field_user_name)
#        input_field_user.send_keys(data_standard_user)
        input_field_password = browser.find_element(*locator_field_user_pass)
        input_field_password.send_keys(data_password)
        selenium_helper.action_wait_on_page(1000)
        selenium_helper.action_click_element(locator_button_login)
        print('Вход выполнен')
        return selenium_helper

    def test_login_successful(self, browser, login):
        """Проверка входа"""
        assert "https://www.saucedemo.com/inventory.html" in browser.current_url.lower()
        print('Вход успешный')
        SeleniumAction.action_close_other_windows_static(browser)

    def test_logout_successful(self, browser, login):
        """Проверка выхода"""
        self.logout(browser)
        assert "https://www.saucedemo.com/" in browser.current_url.lower()
        print('Выход успешный')
        selenium_helper = SeleniumAction(browser)
        selenium_helper.action_close_current_window()

    def test_sort_products_successful(self, browser, login):
        """Проверка сортировки"""
        self.sort_products(browser)
        first_product_id = browser.find_element(*locator_sort_first_prod).get_attribute("id")
        assert first_product_id == "item_3_img_link"
        print('Сортировка успешна')
        selenium_helper = SeleniumAction(browser)
        selenium_helper.action_close_current_window()

    def test_get_product_successful(self, browser, login):
        """Проверка покупки"""
        self.get_product(browser)
        assert "https://www.saucedemo.com/checkout-complete.html" in browser.current_url.lower()
        print('Покупка успешна')
        selenium_helper = SeleniumAction(browser)
        selenium_helper.action_close_current_window()

    def sort_products(self, browser):
        """Сортировка"""
        selenium_helper = SeleniumAction(browser)
        selenium_helper.action_click_element(locator_sort_za)
        print('Сортировка выполнена')

    def logout(self, browser):
        """Выход"""
        selenium_helper = SeleniumAction(browser)
        selenium_helper.action_click_element(locator_button_menu)
        selenium_helper.action_click_element(locator_button_logout)
        print('Выход выполнен')

    def get_product(self, browser):
        """Покупки"""
        selenium_helper = SeleniumAction(browser)
        selenium_helper.action_click_element(locator_add_cart_product_1)
        selenium_helper.action_click_element(locator_add_cart_product_2)
        selenium_helper.action_click_element(locator_shopping_cart)
        selenium_helper.action_click_element(locator_button_checkout)
        input_field_first_name = browser.find_element(*locator_field_first_name)
        input_field_first_name.send_keys(data_first_name)
        input_field_last_name = browser.find_element(*locator_field_last_name)
        input_field_last_name.send_keys(data_last_name)
        input_field_postal_code = browser.find_element(*locator_field_postal_code)
        input_field_postal_code.send_keys(data_zip_code)
        selenium_helper.action_wait_on_page(1000)
        selenium_helper.action_click_element(locator_button_submit)
        selenium_helper.action_click_element(locator_button_finish)
        print('Покупка выполнена')