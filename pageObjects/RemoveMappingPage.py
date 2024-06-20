from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains, Keys


class RemoveMappingPage(BaseClass):
    folderOne = (By.XPATH, "//h4[@title='folder_one']")
    folderTwo = (By.XPATH, "//h4[@title='Folder_two']")
    folderThree = (By.XPATH, "//h4[@title='Folder_three']")
    selectOne = (By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[1]")
    mapOne = (By.XPATH, "(//div[@class='pin cursor-grab'])[1]")
    selectTwo = (By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[2]")
    mapTwo = (By.XPATH, "(//div[@class='pin cursor-grab'])[2]")
    selectThree = (By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[3]")
    mapThree = (By.XPATH, "(//div[@class='pin cursor-grab'])[3]")
    addVessel = (By.XPATH, "//span[contains(text(),'Add Vessel')]")
    drag = (By.XPATH, "//div[@class='text-white yellow-pin']")
    target = (By.XPATH, "//img[@class='cursor-auto']")
    redTwo = (By.XPATH, "//div[@class='text-white red-pin']")
    dragTwo = (By.XPATH, "(//div[@class='text-white yellow-pin'])[2]")
    dragThree = (By.XPATH, "(//div[@class='text-white yellow-pin'])[3]")
    dragSubFolderOne = (By.XPATH, "(//div[@class='text-white yellow-pin'])[1]")
    dragSubFolderTwo = (By.XPATH, "(//div[@class='text-white yellow-pin'])[2]")
    dragSubFolderThree = (By.XPATH, "(//div[@class='text-white yellow-pin'])[3]")
    removeSectionMap = (By.XPATH, "//span[contains(text(),'Remove Section Map')]")
    removeFolderMap = (By.XPATH, "//span[contains(text(),'Remove Folder Map')]")
    remove = (By.XPATH,  "(//span[contains(text(),'Confirm')])[1]")
    deleteSection = (By.XPATH, "//span[contains(text(),'Delete Section')]")
    deleteFolder = (By.XPATH, "//span[contains(text(),'Delete Folder')]")
    renameSection = (By.XPATH,"//span[contains(text(),'Rename Section')]")
    renameFolder = (By.XPATH,"//span[contains(text(),'Rename Folder')]")
    rename = (By.XPATH, "(//input[@name ='name'])[1]")
    updateRename = (By.XPATH, "(//span[contains(text(),'Update')])[1]")
    delete = (By.XPATH, "//span[contains(text(),'Delete')]")

    def __init__(self, driver):
        self.driver = driver

    def removeMappingg(self, getData):
        
        self.webScroll(getData["Scrolling"])
        self.section(getData["SectionName"])
        self.section(getData["SectionNameOne"])
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectOne))
        self.createMap()
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.mapOne))
        self.elementClick(self.driver.find_element(*RemoveMappingPage.mapOne))
        self.dragTheLocationOne(self.driver.find_element(*RemoveMappingPage.drag))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectTwo))
        self.createMap()
        self.elementClick(self.driver.find_element(*RemoveMappingPage.mapTwo))
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.mapTwo))
        self.dragTheLocationTwo(self.driver.find_element(*RemoveMappingPage.dragTwo))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectThree))
        self.createMap()
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.mapThree))
        self.elementClick(self.driver.find_element(*RemoveMappingPage.mapThree))
        self.dragTheLocationThree(self.driver.find_element(*RemoveMappingPage.dragThree))
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectOne))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*RemoveMappingPage.removeSectionMap))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*RemoveMappingPage.remove))
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectTwo))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*RemoveMappingPage.deleteSection))
        self.elementClick(self.driver.find_element(*RemoveMappingPage.delete))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectTwo))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.renameSection))
        self.sleep(2)
        self.send(self.driver.find_element(*RemoveMappingPage.rename))
        self.sleep(2)
        self.send(self.driver.find_element(*RemoveMappingPage.rename))
        self.sendKeys(getData["Rename"], self.driver.find_element(*RemoveMappingPage.rename))
        self.elementClick(self.driver.find_element(*RemoveMappingPage.updateRename))
        self.sleep(4)
        self.elementClick(self.driver.find_element(*RemoveMappingPage.folderOne))
        self.subFolderClick(getData["SubFolderName"])
        self.removeMapFolder(getData["SubFolderNameOne"])
        self.removeMapFolder(getData["SubFolderNameTwos"])
        self.subFolderMappingOne()
        self.sleep(2)
        self.dragTheLocationSubFolderOne(self.driver.find_element(*RemoveMappingPage.dragSubFolderOne))
        self.subFolderMappingTwo()
        self.sleep(2)
        self.dragTheLocationSubFolderTwo(self.driver.find_element(*RemoveMappingPage.dragSubFolderTwo))
        self.subFolderMappingThree()
        self.dragTheLocationSubFolderThree(self.driver.find_element(*RemoveMappingPage.dragSubFolderThree))

        self.sleep(3)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectOne))
        self.elementClick(self.driver.find_element(*RemoveMappingPage.removeFolderMap))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*RemoveMappingPage.remove))
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectTwo))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*RemoveMappingPage.deleteFolder))
        self.elementClick(self.driver.find_element(*RemoveMappingPage.delete))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.selectTwo))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.renameFolder))
        self.sleep(2)
        self.send(self.driver.find_element(*RemoveMappingPage.rename))
        self.sleep(2)
        self.send(self.driver.find_element(*RemoveMappingPage.rename))
        self.sendKeys(getData["SubFolderReName"], self.driver.find_element(*RemoveMappingPage.rename))
        self.elementClick(self.driver.find_element(*RemoveMappingPage.updateRename))

        self.webScroll(getData["Scrolling"])
        self.elementClickByJS(self.driver.find_element(*RemoveMappingPage.addVessel))
        self.sleep(6)


