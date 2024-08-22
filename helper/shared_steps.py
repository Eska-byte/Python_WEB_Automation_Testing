from helper.action import *
from helper.config import *
from pom.POM_cart import *
from pom.POM_data import *
from pom.POM_home import *
from pom.POM_login import *

def STEP_login_valid(open_driver):
    input_element(open_driver, LOGIN_input_username, valid_username)
    input_element(open_driver, LOGIN_input_password, valid_password)
    click_element(open_driver, LOGIN_button_login)
    validate_is_displayed(open_driver, HOME_burger_menu)

def STEP_add_to_cart(open_driver):
    click_element(open_driver, HOME_button_add_to_cart_item1)
    click_element(open_driver, HOME_button_add_to_cart_item2)
    click_element(open_driver, HOME_button_add_to_cart_item3)

def STEP_checkout_from_cart(open_driver):
    click_element(open_driver, HOME_button_cart)
    click_element(open_driver, CART_button_checkout)
    validate_is_displayed(open_driver, DATA_checkout_info)