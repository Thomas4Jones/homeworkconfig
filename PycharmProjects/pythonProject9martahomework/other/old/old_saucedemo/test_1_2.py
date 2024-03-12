import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config.action import SeleniumAction
from test_saucedemo.test_data import *
from test_saucedemo.locator import *

@pytest.fixture
def browser():
    gecko_path = r"../../../config/geckodriver.exe"
    service = Service(gecko_path)
    driver = webdriver.Firefox(service=service)
    yield driver
#    driver.quit()

@pytest.fixture
def login(browser):
    browser.get(data_web_adres)
    selenium_helper = SeleniumAction(browser)
    selenium_helper.action_click_element(locator_field_user_name)
    input_locator_user = (locator_field_user_name)
    input_field_user = browser.find_element(*input_locator_user)
    input_field_user.send_keys(data_standard_user)
    selenium_helper.action_click_element(locator_field_user_pass)
    input_locator_password = (locator_field_user_pass)
    input_field_password = browser.find_element(*input_locator_password)
    input_field_password.send_keys(data_password)
    selenium_helper.action_click_element(locator_button_login)
def test_login_successful(browser, login):
    assert "https://www.saucedemo.com/inventory.html" in browser.current_url.lower()
def logout(browser):
    selenium_helper = SeleniumAction(browser)
    selenium_helper.action_click_element(locator_button_logout)
def test_logout_successful(browser, login):
    assert "https://www.saucedemo.com/" in browser.current_url.lower()