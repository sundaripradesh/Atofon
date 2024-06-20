from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class SelectAddProjectPage(BaseClass):
    projects = (By.XPATH, "(//span[contains(text(),'Projects')])[1]")
    addProject = (By.XPATH, "//span[contains(text(),'Add Project')]")

    def __init__(self, driver):
        self.driver = driver

    def selectAddProject(self):
        self.sleep(2)
        self.elementClick(self.driver.find_element(*SelectAddProjectPage.projects))
        self.sleep(2)
        self.elementClick(self.driver.find_element(*SelectAddProjectPage.addProject))
