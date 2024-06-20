from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import time
import autoit


class CreateVesselPage(BaseClass):
    name = (By.XPATH, "//input[@class ='vs-inputx vs-input--input normal']")
    imoNumber = (By.XPATH, "//input[@name = 'imo_number']")
    owner = (By.XPATH, "(//div[@class ='vx-row w-full m-0'])[1]/div/div[@name ='owner']")
    manager = (By.XPATH, "//div[@name ='manager']")
    office = (By.XPATH, "//div[@name ='office']")
    fleet = (By.XPATH, "//div[@name ='fleet']")
    type = (By.XPATH, "(//div[@class ='vs__actions'])[15]")
    subType = (By.XPATH, "//div[@class ='vx-col sm: w-full md:w-1/2 pr-0 mt-4']/div[@name ='subtype']")
    country = (By.XPATH, "//div[@name ='country']")
    port = (By.XPATH, "//div[@name ='port']")


    def __init__(self, driver):
        self.driver = driver

    def fillVesselDetails(self, getData):
        self.sendKeys(getData["VesselName"], self.driver.find_element(*CreateVesselPage.name))
        self.sendKeys(getData["IMONumber"], self.driver.find_element(*CreateVesselPage.imoNumber))
        self.sleep(1)
        self.dropdownSelectByLi(getData["Owner"], self.driver.find_element(*CreateVesselPage.owner))
        self.sleep(1)
        self.dropdownSelectByLi(getData["Manager"], self.driver.find_element(*CreateVesselPage.manager))
        self.sleep(1)
        self.dropdownSelectByLi(getData["Office"], self.driver.find_element(*CreateVesselPage.office))
        self.sleep(1)
        self.dropdownSelectByLi(getData["Fleet"], self.driver.find_element(*CreateVesselPage.fleet))
        self.sleep(1)
        self.dropdownSelectByLi(getData["Type"], self.driver.find_element(*CreateVesselPage.type))
        self.sleep(1)
        self.dropdownSelectByLi(getData["SubType"], self.driver.find_element(*CreateVesselPage.subType))
        self.sleep(1)
        self.dropdownSelectByLi(getData["Country"], self.driver.find_element(*CreateVesselPage.country))
        self.sleep(1)
        self.dropdownSelectByLi(getData["Port"], self.driver.find_element(*CreateVesselPage.port))









