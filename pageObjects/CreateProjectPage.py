from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

import time
import autoit


class CreateProjectPage(BaseClass):
    projectName = (By.XPATH, "//input[@name ='project_name']")
    date = (By.XPATH, "//input[@name ='date']")
    selectVessel = (By.XPATH, "//i[@class = 'vs-icon notranslate icon-scale vs-button--icon  feather icon-maximize-2 null']")
    selectVesselName = (By.XPATH, "(//div[@class ='vs__actions'])[3]")
    reviewer = (By.XPATH, "//div[@name ='reviewer']")
    portName = (By.XPATH, "//div[@name ='port']")
    services = (By.XPATH, "//div[@name ='services']")
    consultant = (By.XPATH, "//div[@name ='consultants']")
    servicesConsultantTestAll = (By.XPATH, "(//input[@class ='vs-checkbox--input'])[1]")
    workInstructions = (By.XPATH, "//textarea[@name='work_instructions_Consultant Test']")
    chooseFile = (By.XPATH, "//input[@name ='work_instructions_attachment']")
    remarksAndComments = (By.XPATH, "//textarea[@name ='remarks']")

    def __init__(self, driver):
        self.driver = driver

    def fillProjectDetails(self, getData):
        self.sendKeys(getData["ProjectName"], self.driver.find_element(*CreateProjectPage.projectName))
        self.elementClick(self.driver.find_element(*CreateProjectPage.date))
        self.datepicker(getData["Month"], getData["Year"], getData["Day"])
        self.elementClick(self.driver.find_element(*CreateProjectPage.selectVessel))
        self.dropdownSelectByLi(getData["VesselName"], self.driver.find_element(*CreateProjectPage.selectVesselName))
        self.dropdownSelectByLi(getData["Reviewer"], self.driver.find_element(*CreateProjectPage.reviewer))
        self.dropdownSelectByLi(getData["PortName"], self.driver.find_element(*CreateProjectPage.portName))
        self.dropdownMultiSelectByLiStale(getData["ServicesName"], self.driver.find_element(*CreateProjectPage.services))
        self.dropdownSelectByLiClose(getData["ConsultantName"], self.driver.find_element(*CreateProjectPage.consultant))
        self.elementClickByJS(self.driver.find_element(*CreateProjectPage.servicesConsultantTestAll))
        self.elementHoverSend(getData["WorkInstructions"], self.driver.find_element(*CreateProjectPage.workInstructions))
        self.elementClickByJS(self.driver.find_element(*CreateProjectPage.chooseFile))
        time.sleep(3)
        autoit.control_focus("Open", "Edit1")
        time.sleep(3)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\sundari.docx")
        time.sleep(3)
        autoit.control_click("Open", "Button1")
        self.elementHoverSend(getData["Comments"], self.driver.find_element(*CreateProjectPage.remarksAndComments))
        self.webScroll(getData["Scrolling"])








