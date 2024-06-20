import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.SelectAddVesselPage import SelectAddVesselPage
from pageObjects.CreateVesselPage import CreateVesselPage
from utilities.BaseClass import BaseClass


class TestCreateVessel(BaseClass):

    def test_CreateProject(self, setup, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        selectAddVesselPage = SelectAddVesselPage(self.driver)
        createProjectPage = CreateVesselPage(self.driver)

        loginPage.loginPageAdmin(getData)
        selectAddVesselPage.selectAddVessel()
        createProjectPage.fillVesselDetails(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "CreateVessel"))
    def getData(self, request):
        return request.param
