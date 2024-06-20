from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class SelectAddVesselPage(BaseClass):
    vessel = (By.XPATH, "//a[@href='/vessels']")
    addVessel = (By.XPATH, "//span[contains(text(),'Add Vessel')]")

    def __init__(self, driver):
        self.driver = driver

    def selectAddVessel(self):
        self.sleep(2)
        self.elementClick(self.driver.find_element(*SelectAddVesselPage.vessel))
        self.elementClick(self.driver.find_element(*SelectAddVesselPage.addVessel))
