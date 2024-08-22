from helper.shared_steps import *
from pom.POM_cart import *
from pom.POM_checkout import *
from pom.POM_data import *
from pom.POM_overview import *


def test_checkout_item(open_driver):
    STEP_login_valid(open_driver)
    STEP_add_to_cart(open_driver)
    click_element(open_driver, HOME_button_cart)
    click_element(open_driver, CART_button_checkout)
    validate_is_displayed(open_driver, DATA_checkout_info)


def test_checkout_without_filling_data(open_driver):
    STEP_login_valid(open_driver)
    STEP_add_to_cart(open_driver)
    STEP_checkout_from_cart(open_driver)
    click_element(open_driver, DATA_button_continue)
    validate_is_displayed(open_driver, DATA_error_message_data_required)


def test_checkout_by_filling_data(open_driver):
    STEP_login_valid(open_driver)
    STEP_add_to_cart(open_driver)
    STEP_checkout_from_cart(open_driver)
    input_element(open_driver, DATA_input_first_name, "test1")
    input_element(open_driver, DATA_input_last_name, "test2")
    input_element(open_driver, DATA_input_postal_code, "test3")
    click_element(open_driver, DATA_button_continue)
    validate_is_displayed(open_driver, OVERVIEW_payment_info)
    validate_is_displayed(open_driver, OVERVIEW_shipping_info)
    validate_is_displayed(open_driver, OVERVIEW_total_price)
    click_element(open_driver, OVERVIEW_button_finish)
    validate_is_displayed(open_driver, CHECKOUT_message_complete)

