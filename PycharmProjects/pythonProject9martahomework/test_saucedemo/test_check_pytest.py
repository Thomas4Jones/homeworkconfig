from test_saucedemo.test_step import *

@pytest.mark.smoke_market
def test_login_successful(browser, selenium_action, login, login_successful, logout):
    """Проверка входа"""
    login()
    login_successful()
    logout()

@pytest.mark.smoke_market
def test_logout_successful(browser, selenium_action, login, logout, logout_successful):
    """Проверка выхода"""
    login()
    logout()
    logout_successful()

@pytest.mark.smoke_market
def test_sort_products_successful(browser, selenium_action, login, logout, sort_products, sort_products_successful):
    """Проверка сортировки"""
    login()
    sort_products()
    sort_products_successful()
    logout()

@pytest.mark.smoke_market
def test_get_product_successful(browser, selenium_action, login, logout, get_product, get_product_successful):
    """Проверка покупки"""
    login()
    get_product()
    get_product_successful()
    logout()