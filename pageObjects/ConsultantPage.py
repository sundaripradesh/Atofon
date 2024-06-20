from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class ConsultantPage(BaseClass):
    project = (By.XPATH, "//span[contains(text(),'Projects')]")
    updateStatus = (By.XPATH, "(//i[@class ='vs-icon notranslate icon-scale vs-button--icon  feather icon-settings null'])[1]")
    inProgress = (By.XPATH, "(//span[@class ='vs-radio--borde'])[3]")
    clickUpdateStatus = (By.XPATH, "(//button[@id ='update-status'])[1]")
    sendForReview = (By.XPATH, "(//span[@class ='vs-radio--borde'])[3]")
    closeUpdateStatus = (By.XPATH, "(//i[@class ='vs-icon notranslate icon-scale vs-popup--close vs-popup--close--icon material-icons null'])[2]")
    inspection = (By.XPATH, "(//button[@title ='Inspection'])[1]")
    movePagesToLeft = (By.XPATH, "//i[@class ='vs-icon notranslate icon-scale material-icons null']")

    def __init__(self, driver):
        self.driver = driver

    def updateProjectStatus(self, getData):
             self.elementClick(self.driver.find_element(*ConsultantPage.project))
             self.sleep(3)
             self.elementClick(self.driver.find_element(*ConsultantPage.updateStatus))
             self.sleep(3)
             self .elementClickByJS(self.driver.find_element(*ConsultantPage.inProgress))
             self.sleep(3)
             self.elementClickByJS(self.driver.find_element(*ConsultantPage.clickUpdateStatus))
             self.sleep(3)
             self.elementClick(self.driver.find_element(*ConsultantPage.inspection))



