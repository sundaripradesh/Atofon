from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import time
import autoit


class CreateVesselTypePage(BaseClass):

    masters = (By.XPATH, "(//span[contains(text(),'Masters')])[1]")
    addVesselType = (By.XPATH, "//span[contains(text(),'Add Vessel Type')]")
    vesselName = (By.XPATH, "//input[@name='vessel_name']")
    parentVesselType = (By.XPATH, "//span[@class='vs__selected']")
    chooseFileUpload = (By.XPATH, "//h4[contains(text(),'Choose File to upload')] ")
    selectAddVesselType = (By.XPATH, "//span[contains(text(),'Add Vessel Type')]")

    def __init__(self, driver):
        self.driver = driver

    def fillVesselDetails(self, getData):
        self.sleep(3)
        self.elementClick(self.driver.find_element(*CreateVesselTypePage.masters))
        self.selectMasterTypes(getData["MasterType"])
        self.elementClick(self.driver.find_element(*CreateVesselTypePage.addVesselType))
        self.sendKeys(getData["VesselTypeName"], self.driver.find_element(*CreateVesselTypePage.vesselName))
        self.dropdownSelectByLi(getData["ParentVesselType"], self.driver.find_element(*CreateVesselTypePage.parentVesselType))
        self.elementClick(self.driver.find_element(*CreateVesselTypePage.chooseFileUpload))
        time.sleep(3)
        autoit.control_focus("Open", "Edit1")
        time.sleep(3)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\istockphoto-90405943-1024x1024.jpg")
        time.sleep(3)
        autoit.control_click("Open", "Button1")
        self.sleep(3)
        self.elementClick(self.driver.find_element(*CreateVesselTypePage.addVesselType))




