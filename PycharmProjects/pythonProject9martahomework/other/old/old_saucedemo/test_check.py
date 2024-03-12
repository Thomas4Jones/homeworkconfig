from test_saucedemo.test_step import *

class TestSaucedemoChecks:
    def test_login_successful(self, browser, selenium_action, login, logout):
        """Проверка входа"""
        print("Начинаю тест входа...")
        login()
        assert "https://www.saucedemo.com/inventory.html" in browser.current_url.lower()
        print('Вход успешный')
        logout()
        selenium_action.action_close_current_window()

    def test_logout_successful(self, browser, selenium_action, login, logout):
        """Проверка выхода"""
        print("Начинаю тест выхода...")
        login()
        logout()
        assert "https://www.saucedemo.com/" in browser.current_url.lower()
        print('Выход успешный')
        selenium_action.action_close_current_window()

    def test_sort_products_successful(self, browser, selenium_action, login, logout, sort_products):
        """Проверка сортировки"""
        print("Начинаю тест сортировки...")
        login()
        sort_products()
        first_product_id = selenium_action.action_get_attribute(locator_sort_first_prod, "id")
        selenium_action.action_wait_on_page(1000)
        assert first_product_id == "item_2_img_link"
        print('Сортировка успешна')
        logout()
        selenium_action.action_close_current_window()

    def test_get_product_successful(self, browser, selenium_action, login, logout, get_product):
        """Проверка покупки"""
        print("Начинаю тест покупки...")
        login()
        get_product()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.saucedemo.com/checkout-complete.html" in browser.current_url.lower()
        print('Покупка успешна')
        logout()
        selenium_action.action_close_current_window()