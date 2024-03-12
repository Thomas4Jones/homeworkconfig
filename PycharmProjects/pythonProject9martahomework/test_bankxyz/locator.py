from selenium.webdriver.common.by import By

"""Вход"""
locator_button_login_customer = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/div[1]/button')
locator_button_login_bank_manager = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/div[2]/button')
locator_button_your_name = (By.XPATH,'//*[@id="userSelect"]')
locator_button_harry_potter = (By.XPATH,'//*[@id="userSelect"]/option[3]')
locator_button_ron_weasly = (By.XPATH,'//*[@id="userSelect"]/option[4]')
locator_button_your_name_login = (By.XPATH,'/html/body/div/div/div[2]/div/form/button')
locator_select_hermoine = (By.XPATH, '//*[@id="userSelect"]/option[2]')
locator_select_harry = (By.XPATH, '//*[@id="userSelect"]/option[3]')
locator_select_albus = (By.XPATH, '//*[@id="userSelect"]/option[5]')
locator_select_neville = (By.XPATH, '//*[@id="userSelect"]/option[6]]')
locator_select_login_button = (By.CSS_SELECTOR, 'button.btn:nth-child(2)')

"""Выход, домой"""
locator_button_logout = (By.XPATH,'/html/body/div/div/div[1]/button[2]')
locator_button_bank_home = (By.XPATH,'/html/body/div/div/div[1]/button[1]')

"""Транзакции"""
locator_button_count_select = (By.XPATH,'//*[@id="accountSelect"]')
locator_count_1004 = (By.XPATH,'//*[@id="accountSelect"]/option[1]')
locator_count_1005 = (By.XPATH,'//*[@id="accountSelect"]/option[2]')
locator_button_deposit = (By.XPATH,'/html/body/div/div/div[2]/div/div[3]/button[2]')
locator_button_withdrawl = (By.XPATH,'/html/body/div/div/div[2]/div/div[3]/button[3]')
locator_button_transactions = (By.XPATH,'/html/body/div/div/div[2]/div/div[3]/button[1]')
locator_field_amount = (By.XPATH,'/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
locator_confirm_deposit = (By.XPATH,'/html/body/div/div/div[2]/div/div[4]/div/form/button')
locator_confirm_withdrawl = (By.XPATH,'/html/body/div/div/div[2]/div/div[4]/div/form/button')
locator_transactions_back = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/button[1]')
locator_transactions_reset = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/button[2]')
locator_data_start = (By.XPATH,'//*[@id="start"]')
locator_data_end = (By.XPATH,'//*[@id="end"]')
locator_message_successful = (By.XPATH,'/html/body/div/div/div[2]/div/div[4]/div/span')
locator_scroll_right = (By.XPATH,'/html/body/div/div/div[2]/div/div[3]/button[3]')
locator_scroll_left = (By.XPATH,'/html/body/div/div/div[2]/div/div[3]/button[1]')
locator_scroll_top = (By.XPATH,'/html/body/div/div/div[2]/div/div[3]/button[2]')

"""Действия работника добавление клиента"""
locator_button_add_customer = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/button[1]')
locator_first_name = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input')
locator_last_name = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input')
locator_post_code = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input')
locator_button_add_customer_confirm = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
locator_assert_td_ng_binding_1 = (By.CSS_SELECTOR, 'td.ng-binding')
locator_assert_td_ng_binding_2 = (By.XPATH,"/td[contains(text(), 'Farell']")

"""Действия работника открытие счета"""
locator_button_open_account = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/button[2]')
locator_customer_name = (By.XPATH,'//*[@id="userSelect"]')
locator_customer_potter = (By.XPATH,'//*[@id="userSelect"]/option[3]')
locator_currency = (By.XPATH,'//*[@id="currency"]')
locator_currency_rupee = (By.XPATH,'//*[@id="currency"]/option[4]')
locator_button_process = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/button')

"""Действия работника список клиентов"""
locator_button_list_customer = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/button[3]')
locator_search = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input')
locator_delete_customer = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[5]/td[5]/button')
locator_search_result = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[2]')