from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class ReturnToHomePage(BaseClass):
    updateStatus = (By.XPATH, "(//button[@title ='Update Status'])[1]")
    sendForReview = (By.XPATH, "(//span[@class ='vs-radio--borde'])[4]")
    updateStatusToConsultant = (By.XPATH, "(//button[@id ='update-status'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def returnToHome(self):
        self.elementClick(self.driver.find_element(*ReturnToHomePage.updateStatus))
        self.elementClick(self.driver.find_element(*ReturnToHomePage.sendForReview))
        self.elementClick(self.driver.find_element(*ReturnToHomePage.updateStatusToConsultant))
