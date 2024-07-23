from helper.config import *
from helper.action import *

# dibuat untuk mempersingkat codingan dan agar reusbale di test yang memerlukan langkah yang berulang
def step_login_with_valid_email(open_driver):
    element_sendkeys(open_driver, login_input_username, username)
    element_sendkeys(open_driver, login_input_password, password)
    element_click(open_driver, login_button_login)
    element_isdisplayed(open_driver, home_burger_menu)