import os
import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.service import Service as IeService
from selenium.webdriver.ie.options import Options as IeOptions
from config.action import SeleniumAction


# Функция для получения пути к драйверу
def get_driver_path(browser_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if browser_name.lower() == 'chrome':
        return os.path.join(current_dir, "chromedriver.exe")
    elif browser_name.lower() == 'firefox':
        return os.path.join(current_dir, "geckodriver.exe")
    elif browser_name.lower() == 'opera':
        return os.path.join(current_dir, "chromedriver.exe")
    elif browser_name.lower() == 'yandex':
        return os.path.join(current_dir, "yandexdriver.exe")
    elif browser_name.lower() == 'edge':
        return os.path.join(current_dir, "msedgedriver.exe")
    elif browser_name.lower() == 'edgeie':
        return os.path.join(current_dir, "msedgedriver.exe")
    elif browser_name.lower() == 'ie64':
        return os.path.join(current_dir, "IEDriverServer64.exe")
    elif browser_name.lower() == 'ie32':
        return os.path.join(current_dir, "IEDriverServer32.exe")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Фикстура для создания браузера


@pytest.fixture(params=['chrome', 'firefox', 'opera', 'yandex', 'edge'])
def browser(request):
    browser_name = request.param
    driver_path = get_driver_path(browser_name)
    if browser_name.lower() == 'chrome':
        service = ChromeService(driver_path)
        options_c = ChromeOptions()
        options_c.add_argument("-headless")
        options_c.add_argument("user-agent=Firefox")
        driver = webdriver.Chrome(service=service, options=options_c)
    elif browser_name.lower() == 'firefox':
        service = FirefoxService(driver_path)
        options_f = FirefoxOptions()
        options_f.add_argument("-headless")
        driver = webdriver.Firefox(service=service, options=options_f)
    elif browser_name.lower() == 'opera':
        service = ChromeService(driver_path)
        options_o = ChromeOptions()
        options_o.add_experimental_option('w3c', True)
        driver = webdriver.Chrome(service=service, options=options_o)
    elif browser_name.lower() == 'yandex':
        service = ChromeService(driver_path)
        options_y = ChromeOptions()
        options_y.add_experimental_option('w3c', True)
        driver = webdriver.Chrome(service=service, options=options_y)
    elif browser_name.lower() == 'edge':
        service = EdgeService(executable_path=driver_path)
        options_e = EdgeOptions()
        options_e.add_argument("--headless")
        driver = webdriver.Edge(service=service, options=options_e)
    elif browser_name.lower() == 'edgeie':
        service = EdgeService(executable_path=driver_path)
        options_e_ie = EdgeOptions()
        options_e_ie.add_argument("--force-legacy-default-referrer-policy")
        options_e_ie.add_argument("--use-old-msedge-rendering")
        options_e_ie.add_argument("--use-old-msedge-ua")
        driver = webdriver.Ie(service=service, options=options_e_ie)
    elif browser_name.lower() == 'ie64':
        service = IeService(executable_path=driver_path)
        options_ie = IeOptions()
        driver = webdriver.Ie(service=service, options=options_ie)
    elif browser_name.lower() == 'ie32':
        service = IeService(executable_path=driver_path)
        options_ie = IeOptions()
        driver = webdriver.Ie(service=service, options=options_ie)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()

    # Фикстура для создания объекта SeleniumAction


@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action
