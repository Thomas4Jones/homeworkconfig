import pytest # Импорт библиотеки pytest для создания и запуска тестов
from selenium import webdriver # Импорт класса WebDriver из модуля selenium, который позволяет взаимодействовать с браузером
from selenium.webdriver.firefox.service import Service # Импорт сервиса для веб-драйвера Firefox
from config.action import SeleniumAction  # импорт класса SeleniumAction из action.py
from test_saucedemo.locator import * # импорт всех локаторов из locator.py
from test_saucedemo.test_data import * # импорт тестовых данных из test_data.py


@pytest.fixture # Фикстура для инициализации браузера перед выполнением тестов
def browser():
    gecko_path = r"../config/geckodriver.exe"  # местоположение вебдрайвера (фаерфокс)
#    gecko_path = GeckoDriverManager().install() # автоматическая загрузка вебдрайвера из сети (фаерфокс)
    service = Service(gecko_path) # создание сервиса для вебдрайвера
    driver = webdriver.Firefox(service=service) # инициализация веб-драйвера Firefox
    yield driver # возврат драйвера
#    wait = WebDriverWait(browser, 10) # ожидание 1 секунда
#    element = wait.until(EC.visibility_of_element_located((By.XPATH, 'xpath'))) # ожидание видимости XPATH
#    driver.quit() # закрытие окон после тестов

class TestSaucedemo: # Класс всего теста
    @pytest.fixture # Фикстура для входа в систему перед выполнением каждого теста
    def login(self, browser):
        """Вход"""
        browser.get(data_web_adres) # переход на страницу магазина
        selenium_helper = SeleniumAction(browser) # подгрузка методов действий из action.py
#        selenium_helper.click_element(locator_field_user_name) # нажатие на поле логина - НЕОБЯЗАТЕЛЬНО
#        input_locator_user = (locator_field_user_name) # переменная кортеж локатора логина - НЕОБЯЗАТЕЛЬНО
        input_field_user = browser.find_element(*locator_field_user_name) # поиск локатора поля логина
        input_field_user.send_keys(data_standard_user) # заполнение поля логина
        input_field_password = browser.find_element(*locator_field_user_pass) # поиск локатора поля пароля
        input_field_password.send_keys(data_password) # заполнение поля пароля
        selenium_helper.action_click_element(locator_button_login) # нажате на кнопку логина
        print('Логин выполнен') # сообщение о статусе выполнения кода

    def test_login_successful(self, browser, login): # Тест для проверки успешного входа в систему
        """Проверка входа"""
        assert "https://www.saucedemo.com/inventory.html" in browser.current_url.lower() # проверка текущего URL после входа
        print('Логин успешный')

    def test_logout_successful(self, browser, login): # Тест для проверки успешного выхода из системы
        """Проверка выхода"""
        self.logout(browser) # вызов метода для выполнения выхода
        assert "https://www.saucedemo.com/" in browser.current_url.lower() # проверка текущего URL после выхода
        print('Логаут успешный')

    def test_sort_products_successful(self, browser, login): # Тест для проверки успешной сортировки продуктов
        """Проверка сортировки"""
        self.sort_products(browser) # вызов метода для выполнения сортировки продуктов
        first_product_id = browser.find_element(*locator_sort_first_prod).get_attribute("id") # получение атрибута ID первого продукта после сортировки
        assert first_product_id == "item_3_img_link" # проверка ID первого продукта после сортировки
        print('Сортировка успешна')

    def test_get_product_successful(self, browser, login): # Тест для проверки успешной покупки продукта
        """Проверка покупки"""
        self.get_product(browser) # вызов метода для выполнения покупки продукта
        assert "https://www.saucedemo.com/checkout-complete.html" in browser.current_url.lower() # проверка текущего URL после покупки
        print('Покупка успешна')

    def sort_products(self, browser): # Метод для выполнения сортировки продуктов
        """Сортировка"""
        selenium_helper = SeleniumAction(browser) # инициализация объекта SeleniumAction для выполнения действий на странице
        selenium_helper.action_click_element(locator_sort_za) # клик по элементу для сортировки по убыванию
        print('Сортировка выполнена')

    def logout(self, browser): # Метод для выполнения выхода из системы
        """Выход"""
        selenium_helper = SeleniumAction(browser) # инициализация объекта SeleniumAction для выполнения действий на странице
        selenium_helper.action_click_element(locator_button_menu) # клик по элементу меню
        selenium_helper.action_click_element(locator_button_logout) # клик по кнопке выхода
        print('Логаут выполнен')

    def get_product(self, browser): # Метод для выполнения покупки продукта
        """Покупки"""
        selenium_helper = SeleniumAction(browser) # инициализация объекта SeleniumAction для выполнения действий на странице
        selenium_helper.action_click_element(locator_add_cart_product_1) # клик по кнопке добавления продукта в корзину
        selenium_helper.action_click_element(locator_add_cart_product_2) # клик по кнопке добавления продукта в корзину
        selenium_helper.action_click_element(locator_shopping_cart) # клик по кнопке перехода в корзину
        selenium_helper.action_click_element(locator_button_checkout) # клик по кнопке перехода к оформлению заказа
        input_field_first_name = browser.find_element(*locator_field_first_name) # поиск поля ввода имени
        input_field_first_name.send_keys(data_first_name) # ввод имени
        input_field_last_name = browser.find_element(*locator_field_last_name) # поиск поля ввода фамилии
        input_field_last_name.send_keys(data_last_name) # ввод фамилии
        input_field_postal_code = browser.find_element(*locator_field_postal_code) # поиск поля ввода почтового индекса
        input_field_postal_code.send_keys(data_zip_code) # ввод почтового индекса
        selenium_helper.action_click_element(locator_button_submit) # клик по кнопке подтверждения заказа
        selenium_helper.action_click_element(locator_button_finish) # клик по кнопке завершения заказа
        print('Покупка выполнена')
