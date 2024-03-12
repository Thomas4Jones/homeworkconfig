from config.config2 import * #изменённая строка
from test_saucedemo.locator import *
from test_saucedemo.test_data import *

"""ШАГИ"""

@pytest.fixture
def login(browser, selenium_action): # pytest -k login test_step.py
    def login_function():
        browser.get(data_web_adres)  # добавлен
        selenium_action.action_fill_input(locator_field_user_name, data_standard_user)
        selenium_action.action_fill_input(locator_field_user_pass, data_password)
        selenium_action.action_click_element(locator_button_login)
    yield login_function

@pytest.fixture
def logout(browser, selenium_action): # pytest -k logout test_step.py
    def logout_function():
        selenium_action.action_click_element(locator_button_menu)
        selenium_action.action_click_element(locator_button_logout)
    yield logout_function

@pytest.fixture
def sort_products(browser, selenium_action): # pytest -k sort_products test_step.py
    def sort_products_function():
        selenium_action.action_click_element(locator_sort)
        selenium_action.action_select_dropdown_option(locator_sort, data_sort_option_low)
    yield sort_products_function

@pytest.fixture
def get_product(browser, selenium_action): # pytest -k get_product test_step.py
    def get_product_function():
        selenium_action.action_click_element(locator_add_cart_product_1)
        selenium_action.action_click_element(locator_add_cart_product_2)
        selenium_action.action_click_element(locator_shopping_cart)
        selenium_action.action_click_element(locator_button_checkout)
        selenium_action.action_fill_input(locator_field_first_name, data_first_name)
        selenium_action.action_fill_input(locator_field_last_name, data_last_name)
        selenium_action.action_fill_input(locator_field_postal_code, data_zip_code)
        selenium_action.action_click_element(locator_button_submit)
        selenium_action.action_click_element(locator_button_finish)
    yield get_product_function

"""ПРОВЕРКИ"""

@pytest.fixture
def login_successful(browser):
    def test_login_successful_function():
        assert "https://www.saucedemo.com/inventory.html" in browser.current_url.lower()
        print('\n--- Вход успешный ---')
    yield test_login_successful_function

@pytest.fixture
def logout_successful(browser):
    def test_logout_successful_function():
        assert "https://www.saucedemo.com/" in browser.current_url.lower()
        print('\n--- Выход успешный ---')
    yield test_logout_successful_function

@pytest.fixture
def sort_products_successful(browser, selenium_action):
    def sort_products_successful_function():
        first_product_id = selenium_action.action_get_attribute(locator_sort_first_prod, "id")
        assert first_product_id == "item_2_img_link"
        print('\n--- Сортировка успешна ---')
    yield sort_products_successful_function

@pytest.fixture
def get_product_successful(browser):
    def get_product_successful_function():
        assert "https://www.saucedemo.com/checkout-complete.html" in browser.current_url.lower()
        print('\n--- Покупка успешна ---')
    yield get_product_successful_function