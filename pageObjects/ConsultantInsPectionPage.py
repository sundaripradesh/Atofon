from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class ConsultantInspectionPage(BaseClass):
    projects = (By.XPATH, "//span[contains(text(),'Projects')]")
    inspection = (By.XPATH, "(//button[@title='Inspection'])[1]")
    folderFour = (By.XPATH, "//h4[contains(text(),'4.Folder_four')]")
    subFolderFour = (By.XPATH, "//h4[contains(text(),'1.One')] ")
    folderFive = (By.XPATH, "//h4[contains(text(),'5.Folder_five')]")
    subFolderFive = (By.XPATH, "//h4[contains(text(),'1.One')]")
    folderSix = (By.XPATH, "//h4[contains(text(),'6.Folder_six')]")
    subFolderSix = (By.XPATH, "//h4[contains(text(),'1.One')]")
    folderSeven = (By.XPATH, "//h4[contains(text(),'7.Folder_seven')]")
    subFolderSeven = (By.XPATH, "//h4[contains(text(),'1.One')]")
    selectSeven = (By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[7]")
    mapSeven = (By.XPATH, "(//div[@class='pin cursor-grab'])[7]")
    uploadImage = (By.XPATH, "//div[@class='image-card text-center position-relative']")
    dragSeven = (By.XPATH, "(//div[@class='text-white yellow-pin'])[7]")
    dragSubFolder = (By.XPATH, "//div[@class='text-white yellow-pin']")
    selectHomePage = (By.XPATH, "//i[@class='vs-icon notranslate icon-scale vs-button--icon  feather icon-arrow-left null']")
    updateStatus = (By.XPATH, "(//button[@title='Update Status'])[1]")
    inProgress = (By.XPATH, "(//span[@class='vs-radio--circle'])[3]")
    sentForReview = (By.XPATH, "(//span[@class='vs-radio'])[4]")
    saveData = (By.XPATH, "//button[@class='vs-component vs-button vs-component vs-button vs-button-warning vs-button-filled vs-button-warning vs-button-filled']")
    update = (By.XPATH, "(//button[@id='update-status'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def consultantInspection(self, getData):
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.projects))
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.inspection))
        self.webScroll(getData["Scrolling"])
        self.section(getData["SectionNameSeven"])
        self.sleep(2)
        self.webScroll(getData["Scrolling"])
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.selectSeven))
        self.createMap()
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.mapSeven))
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.mapSeven))
        self.dragTheLocationSeven(self.driver.find_element(*ConsultantInspectionPage.dragSeven))

        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.folderSeven))

        self.subFolderClick(getData["SubFolderNameSeven"])
        self.subFolderMapping()
        self.dragTheLocationSubFolder(self.driver.find_element(*ConsultantInspectionPage.dragSubFolder))
        self.webScroll(getData["Scrolling"])
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.folderFour))
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.subFolderFour))

        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\ImagesFolder\\20240204 (282)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (283)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (284)_1024x768.jpg")
        self.closeFolder()
        self.webScroll(getData["Scrolling"])
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.folderFour))
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.subFolderFive))
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\ImagesFolder\\20240204 (282)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (283)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (284)_1024x768.jpg")
        self.closeFolder()
        self.webScroll(getData["Scrolling"])
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.folderSix))
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.subFolderSeven))

        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\ImagesFolder\\20240204 (282)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (283)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (284)_1024x768.jpg")
        self.closeFolder()

        self.webScroll(getData["Scrolling"])
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.folderSeven))
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.subFolderSeven))

        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\ImagesFolder\\20240204 (282)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (283)_1024x768.jpg")
        self.uploadPhotos("C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\ImagesFolder\\20240204 (284)_1024x768.jpg")
        self.closeFolder()
        self.sleep(2)
        self.webScroll(getData["Scrolling"])
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.saveData))

        self.webScroll(getData["ScrollingUp"])
        self.sleep(3)
        self.elementClickByJS(self.driver.find_element(*ConsultantInspectionPage.selectHomePage))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.updateStatus))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.inProgress))

        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.update))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.updateStatus))
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.sentForReview))
        self.elementClick(self.driver.find_element(*ConsultantInspectionPage.update))



