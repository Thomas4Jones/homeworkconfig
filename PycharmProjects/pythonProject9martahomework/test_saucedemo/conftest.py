"""ФАЙЛ С НАСТРОЙКАМИ PyTEST"""

def pytest_configure(config):  # pytest --markers
    config.addinivalue_line("markers", "smoke_market: Дымовые тесты магазина")