import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name",
                     action="store", default="chrome"
                     )
    parser.addoption("--cmdopt", action="store", default="defaulttype1")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(
            "C://Users//ALAGU SUNDARI//PycharmProjects//IQ-CRM_Admin//drivers//chromedriver-win64//chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

        driver.implicitly_wait(30)
    elif browser_name == "firefox":
        driver = webdriver.Firefox("firefox exe to be added")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://dev.salustech.org/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.close()
    des_dir = "C://Users//ALAGU SUNDARI//PycharmProjects//IQ-CRM_Admin//reports"
    new_name = request.config.getoption("--cmdopt") + "_" + datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".html"
    # new_name = "title" + datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".html"
    current_file_name = "C://Users//ALAGU SUNDARI//PycharmProjects//IQ-CRM_Admin//reports//report.html"
    os.rename(current_file_name, os.path.join(des_dir, new_name))

# @pytest.fixture
# def pytest_html_report_title(report):
#     report.title = "title1"


# option = ChromiumOptions()
# option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=option)

# pytest --html=.\reports\report.html --self-contained-html
# pytest -q --cmdopt=login_functionality tests/test_login.py --html=reports/login_functionality.html --self-contained-html
# pytest -q --cmdopt=RegressionSuite tests --html=reports/report.html --self-contained-html

# pytest -v -k createuser -q --cmdopt=RegressionSuite --html=reports/report.html --self-contained-html
#pytest -q --cmdopt=RegressionSuite tests --html=reports/report.html --self-contained-html
