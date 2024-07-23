import pytest

from helper.config import *
from helper.action import *



# pemanggilan driver,action, elemnt yang telah diselector di pom, dan value yang ada di config

@pytest.mark.testManagement(7)
def test_login_with_valid_email(open_driver):
    element_sendkeys(open_driver, login_input_username, username)
    element_sendkeys(open_driver, login_input_password, password)
    element_click(open_driver, login_button_login)
    element_isdisplayed(open_driver, home_burger_menu)

@pytest.mark.testManagement(8)
def test_login_with_invalid_password(open_driver):
    element_sendkeys(open_driver, login_input_username, username)
    element_sendkeys(open_driver, login_input_password, err_password)
    element_click(open_driver, login_button_login)
    element_isdisplayed(open_driver, error_msg_pwd_wrong)

@pytest.mark.testManagement(9)
def test_login_with_invalid_email(open_driver):
    element_sendkeys(open_driver, login_input_username, lcked_username)
    element_sendkeys(open_driver, login_input_password, password)
    element_click(open_driver, login_button_login)
    element_isdisplayed(open_driver, error_msg_lcked_user)


