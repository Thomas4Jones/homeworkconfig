    """ЧЕРНОВИЧОК"""

    wait = WebDriverWait(browser, 10) # ожидание 1 секунда
    element = wait.until(EC.visibility_of_element_located((By.XPATH, 'xpath'))) # ожидание видимости XPATH
    driver.quit() # закрытие окон после тестов

    def fin():
        driver.quit()
    request.addfinalizer(fin)
    return driver

def logout(browser):
    """Выход"""
    selenium_helper = SeleniumAction(browser)
    selenium_helper.action_click_element(logout_but)

def test_logout_successful(browser, login):
    """Проверка выхода"""
    logout(browser)
    assert "https://www.saucedemo.com/" in browser.current_url.lower()

@pytest.fixture(autouse=True)
def setup(browser, selenium_action, login, logout, sort_products, get_product):
    pass
