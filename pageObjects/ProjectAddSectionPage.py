from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class ProjectAddSectionPage(BaseClass):
    folderFour = (By.XPATH, "//h4[@title='Folder_four']")
    folderFive = (By.XPATH, "//h4[@title='Folder_five']")
    selectFour = (By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[4]")
    mapFour = (By.XPATH, "(//div[@class='pin cursor-grab'])[4]")
    selectFive = (By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[5]")
    mapFive = (By.XPATH, "(//div[@class='pin cursor-grab'])[5]")
    saveAsConfirm = (By.XPATH, "//span[contains(text(),'Save as Confirm')]")
    dragFour = (By.XPATH, "(//div[@class='text-white yellow-pin'])[4]")
    dragFive = (By.XPATH, "(//div[@class='text-white yellow-pin'])[5]")
    dragSubFolder = (By.XPATH, "//div[@class='text-white yellow-pin']")

    def __init__(self, driver):
        self.driver = driver

    def projectAddSection(self, getData):
        self.section(getData["SectionNameFour"])
        self.section(getData["SectionNameFive"])
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*ProjectAddSectionPage.selectFour))
        self.createMap()
        self.elementClickByJS(self.driver.find_element(*ProjectAddSectionPage.mapFour))
        self.elementClick(self.driver.find_element(*ProjectAddSectionPage.mapFour))
        self.dragTheLocationTwo(self.driver.find_element(*ProjectAddSectionPage.dragFour))
        self.elementClickByJS(self.driver.find_element(*ProjectAddSectionPage.selectFive))
        self.createMap()

        self.elementClickByJS(self.driver.find_element(*ProjectAddSectionPage.mapFive))
        self.elementClick(self.driver.find_element(*ProjectAddSectionPage.mapFive))
        self.dragTheLocationFive(self.driver.find_element(*ProjectAddSectionPage.dragFive))

        self.elementClick(self.driver.find_element(*ProjectAddSectionPage.folderFour))
        self.subFolderClick(getData["SubFolderNameFour"])
        self.subFolderMapping()
        self.dragTheLocationSubFolder(self.driver.find_element(*ProjectAddSectionPage.dragSubFolder))
        self.webScroll(getData["Scrolling"])
        self.sleep(3)
        self.elementClick(self.driver.find_element(*ProjectAddSectionPage.folderFive))
        self.subFolderClick(getData["SubFolderNameFive"])
        self.subFolderMapping()
        self.dragTheLocationSubFolder(self.driver.find_element(*ProjectAddSectionPage.dragSubFolder))
        self.webScroll(getData["Scrolling"])
        self.elementClickByJS(self.driver.find_element(*ProjectAddSectionPage.saveAsConfirm))
        self.sleep(5)



