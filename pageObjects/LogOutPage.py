from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class LogOutPage(BaseClass):
    selectLogOut = (By.XPATH, "(//button[@class ='vs-con-dropdown parent-dropdown cursor-pointer'])[2]")
    clickLogOut = (By.XPATH, "(//div[@class ='vs-dropdown--custom vs-dropdown--menu']/ul/li/span)[6]")
    logOut = (By.XPATH, "//button/span[contains(text(),'Logout')]")

    def __init__(self, driver):
        self.driver = driver

    def logOutInAdmin(self):
        self.elementHover(self.driver.find_element(*LogOutPage.selectLogOut))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*LogOutPage.clickLogOut))
        self.elementClickByJS(self.driver.find_element(*LogOutPage.logOut))
