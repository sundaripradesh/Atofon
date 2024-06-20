import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.SelectAddProjectPage import SelectAddProjectPage
from pageObjects.CreateProjectPage import CreateProjectPage
from pageObjects.ProjectAddSectionPage import ProjectAddSectionPage
from utilities.BaseClass import BaseClass


class TestCreateProject(BaseClass):
    @pytest.mark.vessel
    @pytest.mark.run(order=2)
    def test_CreateProject(self, setup, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        selectAddProjectPage = SelectAddProjectPage(self.driver)
        createProject = CreateProjectPage(self.driver)
        projectSection = ProjectAddSectionPage(self.driver)

        loginPage.loginPageAdmin(getData)
        selectAddProjectPage.selectAddProject()
        createProject.fillProjectDetails(getData)
        projectSection.projectAddSection(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "CreateProject"))
    def getData(self, request):
        return request.param
