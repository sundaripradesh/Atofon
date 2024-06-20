from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class salusWebPage(BaseClass):
    name = (By.XPATH, "//input[@name ='your-name']")
    email = (By.XPATH, "//input[@name ='your-email']")
    telephone =(By.XPATH, "//input[@name ='your-tel']")
    message =(By.XPATH, "//textarea[@name ='your-message']")
    submit = (By.XPATH, "//p/input[@class ='wpcf7-form-control has-spinner wpcf7-submit']")

    def __init__(self, driver):
        self.driver = driver

    def webPage(self,getData):
        self.webScroll(getData["Scrolling"])
        self.sendKeys(getData["Name"], self.driver.find_element(*salusWebPage.name))

        self.sendKeys(getData["Email"], self.driver.find_element(*salusWebPage.email))
        self.sendKeys(getData["Telephone"], self.driver.find_element(*salusWebPage.telephone))
        self.sendKeys(getData["Message"], self.driver.find_element(*salusWebPage.message))
        self.webScroll(getData["Scrolling"])
        self.elementClickByJS(self.driver.find_element(*salusWebPage.submit))
        self.sleep(4)

