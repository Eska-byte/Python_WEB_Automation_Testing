from selenium.webdriver.common.by import By

DATA_checkout_info = [By.XPATH, "//*[@class='checkout_info']"]
DATA_input_first_name = [By.ID, "first-name"]
DATA_input_last_name = [By.ID, "last-name"]
DATA_input_postal_code = [By.NAME, "postalCode"]
DATA_button_continue = [By.ID, "continue"]
DATA_error_message_data_required = [By.XPATH,"//*[contains(text(),'is required')]"]