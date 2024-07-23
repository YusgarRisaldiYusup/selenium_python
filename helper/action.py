from pom.pom_login import *
from pom.pom_home import *
from assertpy import assert_that

# melakukan setup action dan validation agar reusable

# ====================== ACTION ====================

# melakukan pemanggilan per fungsi agar reusable dan elemt yang di pom dipanggil menggunakan index

def element_click(open_driver, pom):
     open_driver.find_element(pom[0], pom[1]).click()

def element_sendkeys(open_driver, pom, text):
     open_driver.find_element(pom[0], pom[1]).send_keys(text)

def elemnt_get_text(open_driver, pom):
     # dibuat return karna menerima sebuah value
     return open_driver.find_element(pom[0], pom[1]).text

# ====================== Validation ====================

def element_isdisplayed(open_driver, pom):
     open_driver.find_element(pom[0], pom[1]).is_displayed()

# validate with assertpy
def validate_isEqual(text1, text2):
     assert_that(text1).is_equal_to(text2)

