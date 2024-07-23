import time
from selenium import webdriver
import pytest
from selenium.webdriver.edge.options import Options

from helper.config import *
from helper.test_qase_management import *


@pytest.fixture()
# melakukan pemanggilan driver dri selenium yg akan dipanggil di test dan hooks
def open_driver():
    o = Options()
    o.add_argument("--headless")
    driver = webdriver.Edge(options=o)
    driver.implicitly_wait(2)
    return driver

# melakukan hit ke url dengan memanggil driver, melakukan setup report ke qase
@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    open_driver.get(url_web)
    get_error = request.session.testsfailed
    yield
    status = request.session.testsfailed - get_error
    marker = request.node.get_closest_marker("testManagement")

    if marker and marker.args:
        case_id = str(marker.args[0])
        if status == 0:
            push_result(case_id, "passed")
        else:
            push_result(case_id, "failed")

    time.sleep(2)
    open_driver.quit()

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # before suite
    yield
    # after suite