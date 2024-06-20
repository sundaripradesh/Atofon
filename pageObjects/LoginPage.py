from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):
    emailLogin = (By.XPATH, "//input[@name ='email']")
    password = (By.XPATH, "//input[@name ='password']")
    login = (By.XPATH, "//span[@class ='vs-button-text vs-button--text']")

    def __init__(self, driver):
        self.driver = driver

    def loginPageAdmin(self, getData):
        self.sendKeys(getData["Email"], self.driver.find_element(*LoginPage.emailLogin))
        self.sendKeys(getData["Password"], self.driver.find_element(*LoginPage.password))
        self.elementClick(self.driver.find_element(*LoginPage.login))

    def loginPageConsultant(self, getData):
        self.sendKeys(getData["ConsultantEmail"], self.driver.find_element(*LoginPage.emailLogin))
        self.sendKeys(getData["ConsultantPassword"], self.driver.find_element(*LoginPage.password))
        self.elementClick(self.driver.find_element(*LoginPage.login))

    def loginPageClient(self, getData):
        self.sendKeys(getData["ClientEmail"], self.driver.find_element(*LoginPage.emailLogin))
        self.sendKeys(getData["ClientPassword"], self.driver.find_element(*LoginPage.password))
        self.elementClick(self.driver.find_element(*LoginPage.login))






