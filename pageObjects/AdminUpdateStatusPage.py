from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class AdminUpdateStatusPage(BaseClass):
    projects = (By.XPATH, "(//span[contains(text(),'Projects')])[1]")
    updateStatus = (By.XPATH, "(//button[@title='Update Status'])[1]")
    inReviewByAdmin = (By.XPATH, "(//span[@class='vs-radio'])[4]")
    approved = (By.XPATH, "(//span[@class='vs-radio'])[5]")
    sentToClient = (By.XPATH, "(//span[@class='vs-radio'])[6]")
    update = (By.XPATH, "(//button[@id='update-status'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def adminUpdateStatus(self, getData):
        self.sleep(2)
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.projects))

        self.sleep(2)
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.updateStatus))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.inReviewByAdmin))
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.update))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.updateStatus))
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.approved))
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.update))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.updateStatus))
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.sentToClient))
        self.elementClick(self.driver.find_element(*AdminUpdateStatusPage.update))
