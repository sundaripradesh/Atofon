from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class ClientViewProjectPage(BaseClass):
    projects = (By.XPATH, "//span[contains(text(),'Projects')]")
    view = (By.XPATH, "(//button[@title='View'])[1]")
    markerOne = (By.XPATH, "(//div[@class='text-white yellow-pin'])[1]")
    markerTwo = (By.XPATH, "(//div[@class='text-white yellow-pin'])[4]")
    subFolderMarker = (By.XPATH,  "(//div[@class='text-white yellow-pin'])[1]")
    inspectionImage = (By.XPATH, "//span[contains(text(),'Inspection Image')]")
    scrollToShip = (By.XPATH, "//h4[contains(text(),'Ship Image:')]")

    def __init__(self, driver):
        self.driver = driver

    def clientViewProject(self, getData):
        self.elementClick(self.driver.find_element(*ClientViewProjectPage.projects))
        self.elementClick(self.driver.find_element(*ClientViewProjectPage.view))
        self.scrollIntoView(self.driver.find_element(*ClientViewProjectPage.scrollToShip))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*ClientViewProjectPage.markerOne))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*ClientViewProjectPage.subFolderMarker))
        self.clientCloseFolder()
        self.sleep(2)
        self.scrollIntoView(self.driver.find_element(*ClientViewProjectPage.scrollToShip))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*ClientViewProjectPage.markerTwo))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*ClientViewProjectPage.subFolderMarker))
        self.clientCloseFolder()
        self.webScroll(getData["ScrollingUp"])
        self.elementClick(self.driver.find_element(*ClientViewProjectPage.inspectionImage))
        self.sleep(7)







