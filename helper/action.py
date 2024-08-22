# =========================================ACTIONS=========================================
from assertpy import *


def click_element(open_driver, pom):
    open_driver.find_element(pom[0], pom[1]).click()


def input_element(open_driver, pom, text):
    open_driver.find_element(pom[0], pom[1]).send_keys(text)


def get_text_element(open_driver, pom):
    return open_driver.find_element(pom[0], pom[1]).text


# =========================================VALIDATION=========================================
def validate_is_displayed(open_driver, pom):
    open_driver.find_element(pom[0], pom[1]).is_displayed()


def validate_is_equal(text1, text2):
    assert_that(text1).is_equal_to(text2)
