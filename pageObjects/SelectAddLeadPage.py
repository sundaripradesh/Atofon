from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class SelectAddLeadPage(BaseClass):
    leads = (By.XPATH, "//a[@href ='/leads']")
    addLead = (By.XPATH, "//span[contains(text(),'Add Lead')]")

    def __init__(self, driver):
        self.driver = driver

    def selectAddLead(self):
        self.elementClick(self.driver.find_element(*SelectAddLeadPage.leads))
        self.elementClick(self.driver.find_element(*SelectAddLeadPage.addLead))
