from pom.POM_home import *
from pom.POM_login import *
from helper.config import *
from helper.action import *


def test_login_with_valid_username_and_password(open_driver):
    input_element(open_driver, LOGIN_input_username, valid_username)
    input_element(open_driver, LOGIN_input_password, valid_password)
    click_element(open_driver, LOGIN_button_login)
    validate_is_displayed(open_driver, HOME_burger_menu)


def test_login_with_invalid_password(open_driver):
    input_element(open_driver, LOGIN_input_username, valid_username)
    input_element(open_driver, LOGIN_input_password, invalid_password)
    click_element(open_driver, LOGIN_button_login)
    validate_is_displayed(open_driver, LOGIN_error_message_invalid_password)


def test_login_with_without_password(open_driver):
    input_element(open_driver, LOGIN_input_username, valid_username)
    click_element(open_driver, LOGIN_button_login)
    validate_is_displayed(open_driver, LOGIN_error_message_without_password)


def test_login_with_locked_user(open_driver):
    input_element(open_driver, LOGIN_input_username, locked_user)
    input_element(open_driver, LOGIN_input_password, valid_password)
    click_element(open_driver, LOGIN_button_login)
    validate_is_displayed(open_driver, LOGIN_error_message_locked_user)