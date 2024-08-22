from helper.shared_steps import *
from pom.POM_cart import *


def test_add_item_to_cart(open_driver):
    STEP_login_valid(open_driver)
    click_element(open_driver, HOME_button_add_to_cart_item1)
    click_element(open_driver, HOME_button_add_to_cart_item2)
    click_element(open_driver, HOME_button_add_to_cart_item3)

    number_of_item = get_text_element(open_driver, HOME_button_cart)
    validate_is_equal(number_of_item, "3")


def test_remove_item(open_driver):
    STEP_login_valid(open_driver)
    STEP_add_to_cart(open_driver)
    click_element(open_driver, HOME_button_remove_item1)
    click_element(open_driver, HOME_button_remove_item2)

    number_of_item = get_text_element(open_driver, HOME_button_cart)
    validate_is_equal(number_of_item, "1")


def test_remove_item_from_cart(open_driver):
    STEP_login_valid(open_driver)
    STEP_add_to_cart(open_driver)
    click_element(open_driver, HOME_button_cart)
    click_element(open_driver, CART_button_remove_item1)

    number_of_item = get_text_element(open_driver, CART_button_cart)
    validate_is_equal(number_of_item, "2")