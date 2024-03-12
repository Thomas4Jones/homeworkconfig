import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def browser():
    gecko_path = GeckoDriverManager().install()
    service = Service(gecko_path)
    driver = webdriver.Firefox(service=service)
    yield driver

def test_one(browser):
    browser.get("https://www.google.com")