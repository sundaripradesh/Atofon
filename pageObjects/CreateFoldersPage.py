from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import time
import autoit
from selenium.webdriver import ActionChains, Keys


class CreateFoldersPage(BaseClass):
    viewFolder = (By.XPATH, "//button[@title='View']")
    folder = (By.XPATH, "//ul[@class='vs-sidebar-group-items']/li/div/a[@href='/masters/folders']")
    pageNo = (By.XPATH, "(//li[@class='item-pagination vs-pagination--li'])[3]")
    addSection = (By.XPATH, "//span[contains(text(),'Add Section')]")
    folderName = (By.XPATH, "//input[@name ='folder_name']")
    chooseToFileUpload = (By.XPATH, "//h4[contains(text(),'Choose File to upload')]")
    createFolder = (By.XPATH, "//button[@id ='create-folder']")
    scroll = (By.XPATH, "//div[@class='ps__scrollbar-y']")

    def __init__(self, driver):
        self.driver = driver

    def createFolderForVesselType(self, getData):
        self.sleep(3)
        self.selectMasterTypes(getData["MasterTypesOne"])
        self.webScroll(getData["Scrolling"])
        self.sleep(3)
        self.elementClick(self.driver.find_element(*CreateFoldersPage.pageNo))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*CreateFoldersPage.viewFolder))
        self.elementClick(self.driver.find_element(*CreateFoldersPage.addSection))
        self.sendKeys(getData["FolderName"], self.driver.find_element(*CreateFoldersPage.folderName))
        self.elementClick(self.driver.find_element(*CreateFoldersPage.chooseToFileUpload))
        time.sleep(3)
        autoit.control_focus("Open", "Edit1")
        time.sleep(3)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\20240204 (290)_1024x768.jpg")
        time.sleep(3)
        autoit.control_click("Open", "Button1")
        self.elementClick(self.driver.find_element(*CreateFoldersPage.createFolder))









