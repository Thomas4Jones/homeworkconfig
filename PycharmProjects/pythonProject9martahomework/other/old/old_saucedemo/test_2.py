import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config.action import SeleniumAction
from test_saucedemo.locator import *
from test_saucedemo.test_data import *


@pytest.fixture
def browser():
    gecko_path = r"../geckodriver.exe"
    web_service = Service(gecko_path)
    driver = webdriver.Firefox(service=web_service)
    driver.get("https://www.saucedemo.com/")
    yield driver
#    driver.quit()

@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action

@pytest.fixture
def login(browser, selenium_action):
    def login_function():
        selenium_action.action_fill_input(locator_field_user_name, data_standard_user)
        selenium_action.action_fill_input(locator_field_user_pass, data_password)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(locator_button_login)
    yield login_function

@pytest.fixture
def logout(browser, selenium_action):
    def logout_function():
        selenium_action.action_click_element(locator_button_menu)
        selenium_action.action_click_element(locator_button_logout)
    yield logout_function

@pytest.fixture
def sort_products(browser, selenium_action):
    def sort_products_function():
        selenium_action.action_click_element(locator_sort)
        selenium_action.action_select_dropdown_option(locator_sort, "Price (low to high)")
    yield sort_products_function

@pytest.fixture
def get_product(browser, selenium_action):
    def get_product_function():
        selenium_action.action_click_element(locator_add_cart_product_1)
        selenium_action.action_click_element(locator_add_cart_product_2)
        selenium_action.action_click_element(locator_shopping_cart)
        selenium_action.action_click_element(locator_button_checkout)
        selenium_action.action_fill_input(locator_field_first_name, data_first_name)
        selenium_action.action_fill_input(locator_field_last_name, data_last_name)
        selenium_action.action_fill_input(locator_field_postal_code, data_zip_code)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(locator_button_submit)
        selenium_action.action_click_element(locator_button_finish)
    yield get_product_function

class TestSaucedemo:
    def test_login_successful(self, browser, selenium_action, login, logout):
        login()
        """Проверка входа"""
        selenium_action.action_wait_on_page(1000)
        assert "https://www.saucedemo.com/inventory.html" in browser.current_url.lower()
        print('Вход успешный')
        logout()
        selenium_action.action_close_current_window()

    def test_logout_successful(self, browser, selenium_action, login, logout):
        """Проверка выхода"""
        login()
        selenium_action.action_wait_on_page(1000)
        logout()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.saucedemo.com/" in browser.current_url.lower()
        print('Выход успешный')
        selenium_action.action_close_current_window()

    def test_sort_products_successful(self, browser, selenium_action, login, logout, sort_products):
        """Проверка сортировки"""
        login()
        selenium_action.action_wait_on_page(1000)
        sort_products()
        selenium_action.action_wait_on_page(1000)
        first_product_id = selenium_action.action_get_attribute(locator_sort_first_prod, "id")
        selenium_action.action_wait_on_page(1000)
        assert first_product_id == "item_2_img_link"
        print('Сортировка успешна')
        logout()
        selenium_action.action_close_current_window()

    def test_get_product_successful(self, browser, selenium_action, login, logout, get_product):
        """Проверка покупки"""
        login()
        get_product()
        assert "https://www.saucedemo.com/checkout-complete.html" in browser.current_url.lower()
        print('Покупка успешна')
        logout()
        selenium_action.action_close_current_window()
