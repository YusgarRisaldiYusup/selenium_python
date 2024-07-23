from selenium.webdriver.common.by import By

# menyiapkan setup selector element halaman login berbentuk list. dan dipanggil menggunakan index saat diperlukan
login_input_username = [By.ID, "user-name"]
login_input_password = [By.ID, "password"]
login_button_login = [By.ID, "login-button"]
error_msg_pwd_wrong = [By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']"]
error_msg_lcked_user = [By.XPATH, "//h3[text()='Epic sadface: Sorry, this user has been locked out.']"]


