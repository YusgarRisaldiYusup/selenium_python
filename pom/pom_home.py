from selenium.webdriver.common.by import By

# menyiapkan setup selector element halaman home berbentuk list. dan dipanggil menggunakan index saat diperlukan
home_burger_menu = [By.ID, "react-burger-menu-btn"]
home_btn_add_tochart = [By.XPATH, "(//button[text()='Add to cart'])[1]"]
home_btn_delete_from_chart = [By.XPATH, "(//button[text()='Remove'])[1]"]
home_notif_cart = [By.XPATH, "//span[@data-test='shopping-cart-badge']"]


