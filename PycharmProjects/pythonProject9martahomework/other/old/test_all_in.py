import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


class SeleniumAction:
    def __init__(self, driver):
        self.driver = driver

    def action_click_element(self, locator, timeout=10):  # нажатие на элемент
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Ошибка нажатия на элемент {locator}: {e}")

    def action_wait_on_page(self, milliseconds):  # ожидание
        seconds = milliseconds / 1000
        time.sleep(seconds)
        print(f"Ожидание завершено после {seconds:.2f} секунд")

    def action_fill_input(self, locator, text, timeout=10):  # заполнение поля ввода текстом
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Ошибка ввода в элемент {locator} текста '{text}': {e}")

    def action_select_dropdown_option(self, locator, option_text):  # выбор опции из выпадабщего списка
        try:
            select_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            select = Select(select_element)
            select.select_by_visible_text(option_text)
        except Exception as e:
            print(f"Ошибка выбора опции '{option_text}' из списка {locator}: {e}")

    def action_close_current_window(self): # закрытие текущего окна барузера
        try:
            self.driver.close()
        except Exception as e:
            print(f"Ошибка при закрытии активного окна: {e}")

    def action_get_attribute(self, locator, attribute, timeout=10):  # получение значения атрибута элемента
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.get_attribute(attribute)
        except Exception as e:
            print(f"Ошибка получения атрибута '{attribute}' из формы {locator}: {e}")
            return None

class TestLocators:
    # локаторы логина
    locator_field_user_name = (By.XPATH, '//*[@id="user-name"]')
    locator_field_user_pass = (By.XPATH, '//*[@id="password"]')
    locator_button_login = (By.XPATH, '//*[@id="login-button"]')
    # локаторы меню и выхода
    locator_button_menu = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    locator_button_logout = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    # локаторы сортировки
    locator_sort = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    locator_sort_az = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]')
    locator_sort_za = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
    locator_sort_low = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]')
    locator_sort_high = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]')
    # локаторы продукта
    locator_sort_first_prod = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]//a')
    locator_add_cart_product_1 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    locator_add_cart_product_2 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    # локатор корзины
    locator_shopping_cart = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    # локаторы покупки
    locator_button_checkout = (By.XPATH, '//*[@id="checkout"]')
    locator_field_first_name = (By.XPATH, '//*[@id="first-name"]')
    locator_field_last_name = (By.XPATH, '//*[@id="last-name"]')
    locator_field_postal_code = (By.XPATH, '//*[@id="postal-code"]')
    locator_button_submit = (By.XPATH, '//*[@id="continue"]')
    locator_button_finish = (By.XPATH, '//*[@id="finish"]')

class TestData:
    # адрес
    data_web_adres = "https://www.saucedemo.com/"
    # юзеры
    data_standard_user = "standard_user"
    data_locked_out_user = "locked_out_user"
    data_problem_user = "problem_user"
    data_performance_glitch_user = "performance_glitch_user"
    data_error_user = "error_user"
    data_visual_user = "visual_user"
    # пароль
    data_password = "secret_sauce"
    # данные для покупки
    data_first_name = "Tommy"
    data_last_name = "Gun"
    data_zip_code = "60088"
    # опция выпадающего списка сортировки
    data_sort_option_low = "Price (low to high)"

@pytest.fixture
def browser():
    gecko_path = r"geckodriver.exe"
    web_service = Service(gecko_path)
    driver = webdriver.Firefox(service=web_service)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action

@pytest.fixture
def login(browser, selenium_action):
    def login_function():
        selenium_action.action_fill_input(TestLocators.locator_field_user_name, TestData.data_standard_user)
        selenium_action.action_fill_input(TestLocators.locator_field_user_pass, TestData.data_password)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(TestLocators.locator_button_login)
    return login_function

@pytest.fixture
def logout(browser, selenium_action):
    def logout_function():
        selenium_action.action_click_element(TestLocators.locator_button_menu)
        selenium_action.action_click_element(TestLocators.locator_button_logout)
    yield logout_function

@pytest.fixture
def sort_products(browser, selenium_action):
    def sort_products_function():
        selenium_action.action_select_dropdown_option(TestLocators.locator_sort, TestData.data_sort_option_low)
    yield sort_products_function

@pytest.fixture
def get_product(browser, selenium_action):
    def get_product_function():
        selenium_action.action_click_element(TestLocators.locator_add_cart_product_1)
        selenium_action.action_click_element(TestLocators.locator_add_cart_product_2)
        selenium_action.action_click_element(TestLocators.locator_shopping_cart)
        selenium_action.action_click_element(TestLocators.locator_button_checkout)
        selenium_action.action_fill_input(TestLocators.locator_field_first_name, TestData.data_first_name)
        selenium_action.action_fill_input(TestLocators.locator_field_last_name, TestData.data_last_name)
        selenium_action.action_fill_input(TestLocators.locator_field_postal_code, TestData.data_zip_code)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(TestLocators.locator_button_submit)
        selenium_action.action_click_element(TestLocators.locator_button_finish)
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
        first_product_id = selenium_action.action_get_attribute(TestLocators.locator_sort_first_prod, "id")
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
