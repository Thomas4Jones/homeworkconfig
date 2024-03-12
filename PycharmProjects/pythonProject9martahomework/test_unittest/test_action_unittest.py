from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time


class SeleniumAction:
    def __init__(self, driver):
        self.driver = driver

    def action_click_element(self, locator, timeout=10):  # нажатие на элемент
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Ошибка нажатия на элемент {locator}: {e}")

    @staticmethod
    def action_click_element_static(driver, locator, timeout=10):  # нажатие на элемент
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Ошибка нажатия на элемент {locator}: {e}")

    def action_check_element_presence(self, locator):  # проверка наличия элемента
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        except Exception as e:
            print(f"Ошибка при проверке наличия элемента {locator}: {e}")

    def action_wait_for_element_visibility(self, locator, timeout=10):  # ожидание видимости элемента
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Ошибка ожидания видимости элемента {locator}: {e}")

    def action_wait_for_element_text(self, locator, expected_text, timeout=10):  # ожидание появления текста в элементе
        try:
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, expected_text))
        except TimeoutException:
            print(f"Ошибка ожидания текста '{expected_text}' в элементе {locator} в течение {timeout} секунд.")

    def action_wait_on_page(self, milliseconds):  # ожидание
        seconds = milliseconds / 1000
        time.sleep(seconds)
        print(f"Ожидание завершено после {seconds:.2f} секунд")

    def action_fill_input(self, locator, text, timeout=10):  # заполнение поля ввода текстом
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Ошибка ввода в элемент {locator} текста '{text}': {e}")

    @staticmethod
    def action_fill_input_static(driver, locator, text, timeout=10):  # заполнение поля ввода текстом
        try:
            element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Ошибка ввода в элемент {locator} текста '{text}': {e}")

    def action_get_text(self, locator, timeout=10):  # получение текста из элемента
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.text
        except Exception as e:
            print(f"Ошибка получения текста из элемента {locator}: {e}")
            return None

    def action_get_attribute(self, locator, attribute, timeout=10):  # получение значения атрибута элемента
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.get_attribute(attribute)
        except Exception as e:
            print(f"Ошибка получения атрибута '{attribute}' из формы {locator}: {e}")
            return None

    def action_submit_form(self, locator, timeout=10):  # отправка формы
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            element.submit()
        except Exception as e:
            print(f"Ошибка отправки формы {locator}: {e}")

    def action_scroll_to_element(self, locator):  # прокрутка к элементу
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            print(f"Ошибка прокрутки к элементу {locator}: {e}")

    def action_scroll_to_element_center(self, locator):  # прокрутка к элементу, чтобы он был по центру
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        except Exception as e:
            print(f"Ошибка прокрутки к элементу {locator}: {e}")

    def action_wait_for_element_to_disappear(self, locator, timeout=10):  # ожидание исчезновения элемента со страницы
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Ошибка, элемент {locator} не исчез после {timeout} секунд.")

    def action_hover_over_element(self, locator):  # наведение курсора мыши на элемент
        try:
            element = self.driver.find_element(*locator)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            print(f"Ошибка наведения курсора на элемент {locator}: {e}")

    def action_switch_to_frame(self, locator):  # переключение на фрейм
        try:
            frame = self.driver.find_element(*locator)
            self.driver.switch_to.frame(frame)
        except Exception as e:
            print(f"Ошибка переключения на фрейм {locator}: {e}")

    def action_switch_to_default_content(self):  # переключение на основе содержимого страницы из фрейма
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(f"Ошибка переключения на содержимое по умолчанию: {e}")

    def action_select_dropdown_option(self, locator, option_text):  # выбор опции из выпадабщего списка
        try:
            select_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            select = Select(select_element)
            select.select_by_visible_text(option_text)
        except Exception as e:
            print(f"Ошибка выбора опции '{option_text}' из списка {locator}: {e}")

    def action_drag_and_drop(self, source_locator,
                             target_locator):  # перетаскивание элемента и сброс его в другом месте
        try:
            source_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(source_locator))
            target_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(target_locator))
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
        except Exception as e:
            print(f"Ошибка перемещения элемента {source_locator} в {target_locator}: {e}")

    def action_execute_script(self, script):  # выполнение js кода на странице
        try:
            self.driver.execute_script(script)
        except Exception as e:
            print(f"Ошибка выполнения скрипта: {e}")

    def action_upload_file(self, locator, file_path):  # загрузка файла на страницу
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.send_keys(file_path)
        except Exception as e:
            print(f"Ошибка загрузки файла {file_path} в {locator}: {e}")

    def action_accept_alert(self):  # принятие всплывающего окна
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as e:
            print(f"Ошибка принятия всплывающего окна: {e}")

    def action_dismiss_alert(self):  # отмена всплывающего окна
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except Exception as e:
            print(f"Ошибка отмены всплывающего окна: {e}")

    def action_switch_to_alert(self):  # переключение на всплывающее окно
        try:
            return self.driver.switch_to.alert
        except Exception as e:
            print(f"Ошибка переключения на всплывающее окно: {e}")
            return None

    def action_scroll_to_top(self):  # прокрутка к верхней части
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
        except Exception as e:
            print(f"Ошибка прокрутки к верхней части: {e}")

    def action_scroll_to_bottom(self):  # прокрутка к нижней части
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            print(f"Ошибка прокрутки к нижней части: {e}")

    def action_refresh_page(self):  # обновление страницы
        try:
            self.driver.refresh()
        except Exception as e:
            print(f"Ошибка при обновлении страницы: {e}")

    def action_go_back(self):  # назад
        try:
            self.driver.back()
        except Exception as e:
            print(f"Ошибка при возврате на предыдущую страницу: {e}")

    def action_go_forward(self):  # вперед
        try:
            self.driver.forward()
        except Exception as e:
            print(f"Ошибка при переходе на следующую страницу: {e}")

    def action_switch_to_window(self, window_handle):  # переключение окон браузера
        try:
            self.driver.switch_to.window(window_handle)
        except Exception as e:
            print(f"Ошибка при переключении на окно, с дескриптором {window_handle}: {e}")

    def action_close_current_window(self): # закрытие текущего окна барузера
        try:
            self.driver.close()
        except Exception as e:
            print(f"Ошибка при закрытии активного окна: {e}")

    def action_close_other_windows(self): # закрытие всех окон барузера кроме текущего
        try:
            current_window_handle = self.driver.current_window_handle
            for handle in self.driver.window_handles:
                if handle != current_window_handle:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(current_window_handle)
        except Exception as e:
            print(f"Ошибка при закрытии других окон: {e}")

    def action_maximize_window(self): # растягивание окна браузера на весь экран
        try:
            self.driver.maximize_window()
        except Exception as e:
            print(f"Ошибка при максимизации окна браузера: {e}")

    def action_minimize_window(self):  # уменьшение окна браузера
        try:
            self.driver.minimize_window()
        except Exception as e:
            print(f"Ошибка при минимизации окна браузера: {e}")

    def action_get_current_url(self):  # получение текущего url страницы
        try:
            return self.driver.current_url
        except Exception as e:
            print(f"Ошибка получения актуального url: {e}")
            return None

    def action_get_page_title(self):  # получение заголовка текущей страницы
        try:
            return self.driver.title
        except Exception as e:
            print(f"Ошибка получения заголовка страницы: {e}")
            return None

    def action_take_screenshot(self, filename):  # делаем скриншот
        try:
            self.driver.save_screenshot(filename)
        except Exception as e:
            print(f"Ошибка создания скриншота: {e}")
