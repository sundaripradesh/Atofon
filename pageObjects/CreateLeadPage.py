from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import time
import autoit


class CreateLeadPage(BaseClass):
    organisationName = (By.XPATH, "(//div/input[@class ='vs-inputx vs-input--input normal'])[1]")
    contactName = (By.XPATH, "//input[@name = 'contact_name']")
    email = (By.XPATH, "//div[@class='vx-col sm: w-full md:w-1/2 mb-4 pl-0']/div/div/input[@name ='email']")
    phone = (By.XPATH, "//input[@name = 'phone']")
    name = (By.XPATH, "(//div[@class ='vs-con-input']/input[@name ='name'])[5]")
    imoNumber = (By.XPATH, "//input[@name = 'imo_number']")
    dateOfAttendance = (By.XPATH, "//div[@class ='vdp-datepicker mt-1']")
    portDetails = (By.XPATH, "//textarea[@name ='port_detail']")
    agentDetails = (By.XPATH, "//textarea[@name ='agent_detail']")
    serviceRequirements = (By.XPATH, "//textarea[@name ='service_requirement']")
    remarksAndComments = (By.XPATH, "//textarea[@placeholder = 'Add remarks...']")
    addLead = (By.XPATH, "//span[contains(text(),'Add Lead')]")

    def __init__(self, driver):
        self.driver = driver

    def fillLeadDetails(self, getData):
        self.sendKeys(getData["OrganisationName"], self.driver.find_element(*CreateLeadPage.organisationName))
        self.sendKeys(getData["ContactName"], self.driver.find_element(*CreateLeadPage.contactName))
        self.sendKeys(getData["EmailAddress"], self.driver.find_element(*CreateLeadPage.email))
        self.sendKeys(getData["Phone"], self.driver.find_element(*CreateLeadPage.phone))
        self.sendKeys(getData["VesselName"], self.driver.find_element(*CreateLeadPage.name))
        self.sendKeys(getData["IMONumber"], self.driver.find_element(*CreateLeadPage.imoNumber))
        self.elementClick(self.driver.find_element(*CreateLeadPage.dateOfAttendance))
        self.webScroll(getData["Scrolling"])
        self.datepickerLead(getData["MonthYear"], getData["LeadDay"])
        self.elementHoverSend(getData["PortDetails"], self.driver.find_element(*CreateLeadPage.portDetails))
        self.elementHoverSend(getData["AgentDetails"], self.driver.find_element(*CreateLeadPage.agentDetails))
        self.elementHoverSend(getData["ServiceRequirements"], self.driver.find_element(*CreateLeadPage.serviceRequirements))
        self.elementHoverSend(getData["RemarksAndComments"], self.driver.find_element(*CreateLeadPage.remarksAndComments))
        self.elementClick(self.driver.find_element(*CreateLeadPage.addLead))
        self.sleep(3)



