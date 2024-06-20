import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateVesselTypePage import CreateVesselTypePage
from pageObjects.CreateFoldersPage import CreateFoldersPage
from pageObjects.SelectAddVesselPage import SelectAddVesselPage
from pageObjects.CreateVesselPage import CreateVesselPage
from pageObjects.RemoveMappingPage import RemoveMappingPage
from utilities.BaseClass import BaseClass


class TestRemoveMapping(BaseClass):
    @pytest.mark.vessel
    @pytest.mark.run(order=1)
    def test_RemoveMapping(self, setup, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        vesselType = CreateVesselTypePage(self.driver)
        folder = CreateFoldersPage(self.driver)
        selectAddVesselPage = SelectAddVesselPage(self.driver)
        createProjectPage = CreateVesselPage(self.driver)
        removeMapping = RemoveMappingPage(self.driver)


        loginPage.loginPageAdmin(getData)
        vesselType.fillVesselDetails(getData)
        folder.createFolderForVesselType(getData)
        selectAddVesselPage.selectAddVessel()
        createProjectPage.fillVesselDetails(getData)
        removeMapping.removeMappingg(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "CreateVesselType"))
    def getData(self, request):
        return request.param
