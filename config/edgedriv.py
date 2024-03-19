import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Edge(executable_path="C:\Users\andrey48\PycharmProjects\pythonProject9martahomework\config\msedgedriver.exe")
    yield driver
    driver.quit()

def test_example(browser):
    browser.get("https://www.example.com")
    assert "Example" in browser.title