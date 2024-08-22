from selenium.webdriver.common.by import By

LOGIN_input_username = [By.ID,"user-name"]
LOGIN_input_password = [By.NAME,"password"]
LOGIN_button_login = [By.XPATH,"//input[@data-test='login-button']"]
LOGIN_error_message_invalid_password = [By.XPATH,"//*[contains(text(),'do not match')]"]
LOGIN_error_message_without_password = [By.XPATH,"//*[contains(text(),'is required')]"]
LOGIN_error_message_locked_user = [By.XPATH,"//*[contains(text(),'has been locked out')]"]