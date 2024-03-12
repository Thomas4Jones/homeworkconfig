from selenium.webdriver.common.by import By

# локаторы логина
locator_field_user_name = (By.XPATH, '//*[@id="user-name"]')
locator_field_user_pass = (By.XPATH, '//*[@id="password"]')
locator_button_login = (By.XPATH, '//*[@id="login-button"]')
# локаторы меню и выхода
locator_button_menu = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
locator_button_logout = (By.XPATH, '//*[@id="logout_sidebar_link"]')
# локаторы сортировки
locator_sort = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
locator_sort_az = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]')
locator_sort_za = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
locator_sort_low = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]')
locator_sort_high = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]')
# локаторы продукта
locator_sort_first_prod = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]//a')
locator_add_cart_product_1 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
locator_add_cart_product_2 = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
# локатор корзины
locator_shopping_cart = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
# локаторы покупки
locator_button_checkout = (By.XPATH, '//*[@id="checkout"]')
locator_field_first_name = (By.XPATH, '//*[@id="first-name"]')
locator_field_last_name = (By.XPATH, '//*[@id="last-name"]')
locator_field_postal_code = (By.XPATH, '//*[@id="postal-code"]')
locator_button_submit = (By.XPATH, '//*[@id="continue"]')
locator_button_finish = (By.XPATH, '//*[@id="finish"]')