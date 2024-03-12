from config.config2 import * # изменённая строка
from test_bankxyz.locator import *
from test_bankxyz.data import *


@pytest.fixture
def login_bank_customer(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_customer_function():
        browser.get(data_web_adres) # добавлен
        selenium_action.action_click_element(locator_button_login_customer)
    yield login_bank_customer_function

@pytest.fixture
def login_bank_potter(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_potter_function():
        selenium_action.action_click_element(locator_button_your_name)
        selenium_action.action_click_element(locator_button_harry_potter)
        selenium_action.action_click_element(locator_button_your_name_login)
    yield login_bank_potter_function

@pytest.fixture
def login_bank_customer_hermoine(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_customer_hermoine_function():
        selenium_action.action_click_element(locator_select_hermoine)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(locator_select_login_button)
    yield login_bank_customer_hermoine_function

@pytest.fixture
def login_bank_weasly(browser, selenium_action):  # pytest -k login test_step.py
    def login_bank_weasly_function():
            selenium_action.action_click_element(locator_button_your_name)
            selenium_action.action_click_element(locator_button_ron_weasly)
            selenium_action.action_click_element(locator_button_your_name_login)
    yield login_bank_weasly_function

@pytest.fixture
def bank_home(browser, selenium_action):
    def bank_home_function():
            selenium_action.action_click_element(locator_button_bank_home)
    yield bank_home_function

@pytest.fixture
def logout_bank(browser, selenium_action):
    def logout_bank_function():
            selenium_action.action_click_element(locator_button_logout)
    yield logout_bank_function

@pytest.fixture
def deposit(browser, selenium_action):
    def deposit_function():
            selenium_action.action_click_element(locator_button_count_select)
            selenium_action.action_click_element(locator_count_1005)
            selenium_action.action_click_element(locator_button_deposit)
            selenium_action.action_click_element(locator_field_amount)
            selenium_action.action_fill_input(locator_field_amount, data_deposit)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_confirm_deposit)
    yield deposit_function

@pytest.fixture
def withdrawl(browser, selenium_action):
    def withdrawl_function():
            selenium_action.action_click_element(locator_button_count_select)
            selenium_action.action_click_element(locator_count_1005)
            selenium_action.action_click_element(locator_button_withdrawl)
            selenium_action.action_click_element(locator_field_amount)
            selenium_action.action_fill_input(locator_field_amount, data_withdrawl)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_confirm_withdrawl)
    yield withdrawl_function

@pytest.fixture
def transaction(browser, selenium_action):
    def transaction_function():
            selenium_action.action_click_element(locator_button_transactions)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_scroll_right)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_transactions_reset)
    yield transaction_function

@pytest.fixture
def login_bank_manager(browser, selenium_action):
    def login_bank_manager_function():
        browser.get(data_web_adres) # добавлен
        selenium_action.action_click_element(locator_button_login_bank_manager)
    yield login_bank_manager_function

@pytest.fixture
def add_customer(browser, selenium_action):
    def add_customer_function():
            selenium_action.action_click_element(locator_button_add_customer)
            selenium_action.action_fill_input(locator_first_name, data_first_name)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_fill_input(locator_last_name, data_last_name)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_fill_input(locator_post_code, data_post_code)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_button_add_customer_confirm)
            selenium_action.action_accept_alert()
    yield add_customer_function

@pytest.fixture
def open_account(browser, selenium_action):  # pytest -k login test_step.py
    def open_account_function():
        selenium_action.action_click_element(locator_button_open_account)
        selenium_action.action_click_element(locator_customer_name)
        selenium_action.action_click_element(locator_customer_potter)
        selenium_action.action_click_element(locator_currency)
        selenium_action.action_click_element(locator_currency_rupee)
        selenium_action.action_click_element(locator_button_process)
    yield open_account_function

@pytest.fixture
def list_customer(browser, selenium_action):
    def list_customer_function():
        selenium_action.action_click_element(locator_button_list_customer)
        selenium_action.action_wait_on_page(1000)
    yield list_customer_function
