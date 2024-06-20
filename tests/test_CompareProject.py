import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.CompareProjectPage import CompareProjectPage
from utilities.BaseClass import BaseClass


class TestCreateProject(BaseClass):
    @pytest.mark.vessel
    @pytest.mark.run(order=3)
    def test_CreateProject(self, setup, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        compareProject = CompareProjectPage(self.driver)




        loginPage.loginPageAdmin(getData)
        compareProject.compareProjectPage(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "AdminInspection"))
    def getData(self, request):
        return request.param
