from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class ClientPage(BaseClass):
    projects = (By.XPATH, "//span[contains(text(),'Projects')]")

    def __init__(self, driver):
        self.driver = driver

    def clientPage(self):
        self.elementClick(self.driver.find_element(*ClientPage.projects))
        self.sleep(10)

