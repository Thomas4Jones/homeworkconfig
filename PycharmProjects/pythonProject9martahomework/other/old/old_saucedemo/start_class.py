import subprocess
import sys

def run_all():  # команда в консоли: python start_class.py run_all
    """ВСЕ ТЕСТЫ"""  # pytest test_check_class.py
    print("Запускаю все тесты")
    subprocess.run(["pytest", "test_check.py", "-k", "TestSaucedemoChecks", "--verbose", "--tb=long", "--color=yes"])

def run_login():  # команда в консоли: python start_class.py run_login
    """ЛОГИН""" # pytest test_check_class.py -k TestSaucedemoLogin
    print("Запускаю тест логина")
    subprocess.run(["pytest", "test_check_class.py", "-k", "TestSaucedemoLogin", "--verbose", "--tb=long", "--color=yes"])

def run_logout():  # команда в консоли: python start_class.py run_logout
    """ВЫХОД"""  # pytest test_check_class.py -k TestSaucedemoLogout
    print("Запускаю тест выхода")
    subprocess.run(["pytest", "test_check_class.py", "-k", "TestSaucedemoLogout", "--verbose", "--tb=long", "--color=yes"])

def run_sort():  # команда в консоли: python start_class.py run_sort
    """СОРТИРОВКА"""  # pytest test_check_class.py -k TestSaucedemoSortProducts
    print("Запускаю тест сортировки")
    subprocess.run(["pytest", "test_check_class.py", "-k", "TestSaucedemoSortProducts", "--verbose", "--tb=long", "--color=yes"])

def run_get():  # команда в консоли: python start_class.py run_get
    """ПОКУПКА"""  # pytest test_check_class.py -k TestSaucedemoGetProducts
    print("Запускаю тест покупки")
    subprocess.run(["pytest", "test_check_class.py", "-k", "TestSaucedemoGetProducts", "--verbose", "--tb=long", "--color=yes"])

if __name__ == "__main__":
    command = sys.argv[1]
    if command == "run_all":
        run_all()
    elif command == "run_login":
        run_login()
    elif command == "run_logout":
        run_logout()
    elif command == "run_sort":
        run_sort()
    elif command == "run_get":
        run_get()
    else:
        print("Неправильная команда. Используйте одну из следующих команд: run_all, run_login, run_logout, run_sort, run_get.")

"""
Команды включения виртуального окружения

CMD
C:\\Users\Rumata\PycharmProjects\PythonTestProject\venv\Scripts\activate

PowerShell
Команда для перехода к администратору
Set-ExecutionPolicy RemoteSigned
Команда включения окружения
C:\\Users\Rumata\PycharmProjects\PythonTestProject\venv\Scripts\Activate.ps1
"""
