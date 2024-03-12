from test_bankxyz.test_step import *


class TestBankChecks:
    def test_login_successful_bank(self, browser, selenium_action, login_bank_customer):
        """Проверка входа"""
        login_bank_customer()
        browser.get(data_web_adres) # добавлен
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/customer" in browser.current_url.lower()
        print('Вход успешный')
        selenium_action.action_close_current_window()

    def test_login_successful_potter(self, browser, selenium_action, login_bank_customer, login_bank_potter):
        """Проверка входа Гарри Поттер"""
        login_bank_customer()
        login_bank_potter()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in browser.current_url.lower()
        print('Вход Гарри Поттер успешный')
        selenium_action.action_close_current_window()

    def test_login_and_back_home_successful_potter(self, browser, selenium_action, login_bank_customer, login_bank_potter, bank_home):
        """Проверка входа Гарри Поттер и возврат на главную страницу"""
        login_bank_customer()
        login_bank_potter()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in browser.current_url.lower()
        print('Вход Гарри Поттер успешный')
        bank_home()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/login" in browser.current_url.lower()
        print('Переход на главную страницу успешный')
        selenium_action.action_close_current_window()

    def test_login_successful_weasly(self, browser, selenium_action, login_bank_customer, login_bank_weasly, logout_bank):
        """Проверка входа Рон Уизли и логаут"""
        login_bank_customer()
        login_bank_weasly()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in browser.current_url.lower()
        print('Вход Рон Уизли успешный')
        logout_bank()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/customer" in browser.current_url.lower()
        print('Выход успешный')
        selenium_action.action_close_current_window()

    def test_successful_deposit_potter(self, browser, selenium_action, login_bank_customer, login_bank_potter, deposit):
        """Проверка депонирования средств"""
        login_bank_customer()
        login_bank_potter()
        deposit()
        selenium_action.action_wait_on_page(1000)
        successful_text = selenium_action.action_get_text(locator_message_successful)
        assert successful_text == "Deposit Successful"
        print('Депонирование произведено успешно')
        selenium_action.action_close_current_window()

    def test_successful_withdrawl_potter(self, browser, selenium_action, login_bank_customer, login_bank_potter, deposit, withdrawl):
        """Проверка списания средств"""
        login_bank_customer()
        login_bank_potter()
        deposit()
        withdrawl()
        selenium_action.action_wait_on_page(1000)
        successful_text = selenium_action.action_get_text(locator_message_successful)
        assert successful_text == "Transaction successful"
        print('Списание произведено успешно')
        selenium_action.action_close_current_window()

    def test_successful_fail_withdrawl_potter(self, browser, selenium_action, login_bank_customer, login_bank_potter, deposit, withdrawl):
        """Проверка списания средств"""
        login_bank_customer()
        login_bank_potter()
        withdrawl()
        selenium_action.action_wait_on_page(1000)
        successful_text = selenium_action.action_get_text(locator_message_successful)
        assert successful_text == "Transaction Failed. You can not withdraw amount more than the balance."
        print('Списание произведено успешно')
        selenium_action.action_close_current_window()

    def test_successful_transaction_potter(self, browser, selenium_action, login_bank_customer, login_bank_potter, deposit, withdrawl, transaction):
        """Проверка отчета об операциях"""
        login_bank_customer()
        login_bank_potter()
        deposit()
        withdrawl()
        transaction()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/listtx" in browser.current_url.lower()
        print('Отчет об операциях сформирован')
        selenium_action.action_close_current_window()

    def test_login_successful_manager(self, browser, selenium_action, login_bank_manager):
        """Проверка входа работника банка"""
        browser.get(data_web_adres) # добавлен
        login_bank_manager()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/manager" in browser.current_url.lower()
        print('Вход работника успешный')
        selenium_action.action_close_current_window()

    def test_successful_add_customer(self, selenium_action, login_bank_manager, add_customer, list_customer):
        """Проверка добавления клиента"""
        login_bank_manager()
        add_customer()
        selenium_action.action_wait_on_page(1000)
        list_customer()
        contains_farell = selenium_action.assert_check_element_in_elements(locator_assert_td_ng_binding_1, data_last_name)
        print("Строка не найдена",contains_farell)
        assert contains_farell == True, "Cтрока найдена"
        print('Клиент добавлен')
        selenium_action.action_close_current_window()

    def test_successful_open_account_potter(self, selenium_action, login_bank_manager, open_account):
        """Проверка открытия счета"""
        login_bank_manager()
        open_account()
        selenium_action.action_wait_on_page(1000)
        print('Счет открыт успешно')
        selenium_action.action_close_current_window()

    def test_list_customer(self, browser, selenium_action, login_bank_manager, list_customer):
        """Проверка формирования списка клиентов"""
        login_bank_manager()
        list_customer()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/manager/list" in browser.current_url.lower()
        print('Список клиентов сформирован успешно')
        selenium_action.action_close_current_window()