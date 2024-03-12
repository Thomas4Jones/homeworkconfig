"""ПРОВЕРКИ"""
def test_open_in_new_tab(self, browser):
    # Открываем новую вкладку
    browser.execute_script("window.open('');")
    # Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    # Проверяем, что новая вкладка открыта
    assert len(browser.window_handles) == 2
    print("Открыли новую вкладку")

"""ФИКСТУРЫ"""
@pytest.fixture(scope="module") # область видимости фикстуры,
def setup_module_fixture():
    print("\n--- Setup Module Fixture ---")
    yield
    print("\n--- Teardown Module Fixture ---")
    # "function" фикстура будет создана один раз для каждой тестовой функции (по умолчанию)
    # "class" фикстура будет создана один раз для каждого класса тестов
    # "module" фикстура будет создана один раз для каждого модуля тестов
    # "session" фикстура будет создана один раз для всей сессии тестирования

@pytest.fixture(params=[1, 2, 3]) # позволяет задать набор параметров, которые будут переданы в тестовую функцию
def param_fixture(request):
    param_value = request.param
    print(f"\n--- Setup Param Fixture with param value: {param_value} ---")
    yield param_value
    print("\n--- Teardown Param Fixture ---")

@pytest.fixture(autouse=True) # указывает, будет ли фикстура вызвана автоматически или только при явном запросе в тесте
def autouse_fixture():
    print("\n--- Setup Autouse Fixture ---")
    yield
    print("\n--- Teardown Autouse Fixture ---")

@pytest.fixture(ids=["test_case_1", "test_case_2", "test_case_3"]) # устанавливает пользовательские идентификаторы для фикстуры, которые будут отображаться в отчете о тестировании
def id_fixture():
    print("\n--- Setup ID Fixture ---")
    yield
    print("\n--- Teardown ID Fixture ---")

def test_example(setup_module_fixture, param_fixture, id_fixture):
    print("\n--- Running Test Example ---")
    assert True

@pytest.fixture(name="name_fixture") # устанавливает имя для фикстуры, которое будет отображаться в отчете о тестировании
def name_fixture():
    print("\n--- Name Fixture ---")

"""ДИРЕКТОРИИ"""
"""os"""
import os
# Получаем путь к текущему скрипту
current_script_path = os.path.abspath(__file__)
# Преобразуем относительный путь в абсолютный
absolute_path = os.path.realpath(current_script_path)
# Получаем родительский каталог
parent_directory = os.path.dirname(absolute_path)
# Получаем путь к текущему рабочему каталогу
current_working_directory = os.getcwd()
print("Текущий рабочий каталог:", current_working_directory)
# Создание нового каталога
new_directory = os.path.join(os.getcwd(), "новый_каталог")
os.makedirs(new_directory)
print("Создан новый каталог:", new_directory)
# Получение списка файлов в каталоге
current_files = os.listdir(os.getcwd())
print("Файлы в текущем каталоге:", current_files)
# Проверка существования файла или каталога
file_to_check = "example.txt"
if os.path.exists(file_to_check):
    print(f"Файл {file_to_check} существует.")
else:
    print(f"Файл {file_to_check} не существует.")
# Получение размера файла
file_to_check = "example.txt"
if os.path.exists(file_to_check):
    file_size_bytes = os.path.getsize(file_to_check)
    file_size_mb = file_size_bytes / (1024 * 1024)
    print(f"Размер файла {file_to_check}: {file_size_mb:.2f} мегабайт.")
    # Проверяем размер файла
    max_file_size_mb = 10  # Максимальный допустимый размер файла в мегабайтах
    if file_size_mb > max_file_size_mb:
        print(f"Размер файла {file_to_check} превышает допустимый размер.")
    else:
        print(f"Размер файла {file_to_check} соответствует допустимому размеру.")
else:
    print(f"Файл {file_to_check} не существует.")
"""pathlib"""
from pathlib import Path
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
file_path = project_root / "folder" / "file.exe"
# __file__ - магическая переменная содержит путь к текущему исполняемому файлу(скрипту)
# Path(__file__) - создает объект Path из пути,gолученного из __file__
# resolve() - преобразует путь к абсолютному виду, разрешая все символические ссылки и относительные пути.
# parent - возвращает родительский каталог указанного пути
"""pathlib"""
# Создание объекта Path из относительного пути
file_path_path = Path("folder/file.exe")
# Преобразование относительного пути в абсолютный
absolute_path = file_path.resolve()
print(absolute_path)
# Проверка существования файла или каталога
if file_path.exists():
    print("Файл существует.")
else:
    print("Файл не существует.")
# Получение размера файла в байтах
file_size = file_path.stat().st_size
print(f"Размер файла: {file_size} байт.")
# Создание объекта Path для нового каталога
new_directory = Path("новый_каталог")
# Создание нового каталога
new_directory.mkdir()
# Получение размера файла в мегабайтах
file_size_mb = file_path.stat().st_size / (1024 * 1024)
print(f"Размер файла: {file_size_mb:.2f} МБ")