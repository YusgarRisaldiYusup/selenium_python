import pytest

from helper.config import *
from helper.action import *
from helper.shared_step import *

@pytest.mark.testManagement(10)
def test_add_item_to_cart_valid(open_driver):
    step_login_with_valid_email(open_driver)
    element_click(open_driver, home_btn_add_tochart)
    element_click(open_driver, home_btn_add_tochart)
    element_click(open_driver, home_btn_add_tochart)
    cart_item = elemnt_get_text(open_driver, home_notif_cart)
    validate_isEqual(cart_item, "3")

@pytest.mark.testManagement(11)
def test_delete_item_to_cart_valid(open_driver):
    step_login_with_valid_email(open_driver)
    element_click(open_driver, home_btn_add_tochart)
    element_click(open_driver, home_btn_add_tochart)
    element_click(open_driver, home_btn_add_tochart)
    cart_item = elemnt_get_text(open_driver, home_notif_cart)
    validate_isEqual(cart_item, "3")
    element_click(open_driver, home_btn_delete_from_chart)
    cart_item = elemnt_get_text(open_driver, home_notif_cart)
    validate_isEqual(cart_item, "2")