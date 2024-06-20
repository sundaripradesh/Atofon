from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class CompareProjectPage(BaseClass):
    projects = (By.XPATH, "(//span[contains(text(),'Projects')])[1]")
    projectOne = (By.XPATH, "(//input[@class='vs-checkbox--input'])[2]")
    projectThree = (By.XPATH, "(//input[@class='vs-checkbox--input'])[3]")
    clickCompare = (By.XPATH, "//span[contains(text(),'Compare')]")
    firstFolder = (By.XPATH, "//h4[contains(text(),'one')]")
    subFolderOne = (By.XPATH, "(//div[@class='text-center card-content'])[1]")
    compareFirstImage = (By.XPATH, "(//span[@class='vs-button-text vs-button--text'])[4]")
    compareSecondImage = (By.XPATH, "(//span[@class='vs-button-text vs-button--text'])[6]")

    def __init__(self, driver):
        self.driver = driver

    def compareProjectPage(self, getData):
        self.elementClick(self.driver.find_element(*CompareProjectPage.projects))
        self.elementClick(self.driver.find_element(*CompareProjectPage.projectOne))
        self.elementClick(self.driver.find_element(*CompareProjectPage.projectThree))

        self.elementClick(self.driver.find_element(*CompareProjectPage.clickCompare))
        self.sleep(5)
        self.elementClick(self.driver.find_element(*CompareProjectPage.firstFolder))
        self.sleep(6)
        self.elementClickByJS(self.driver.find_element(*CompareProjectPage.subFolderOne))
        self.sleep(5)
        self.webScroll(getData["Scrolling"])
        self.elementClick(self.driver.find_element(*CompareProjectPage.compareFirstImage))
        self.sleep(5)
        self.elementClick(self.driver.find_element(*CompareProjectPage.compareSecondImage))











