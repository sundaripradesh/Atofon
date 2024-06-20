import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateVesselTypePage import CreateVesselTypePage
from pageObjects.CreateFoldersPage import CreateFoldersPage
from pageObjects.SelectAddVesselPage import SelectAddVesselPage
from pageObjects.CreateVesselPage import CreateVesselPage
from pageObjects.VesselAddSectionPage import VesselAddSectionPage
from utilities.BaseClass import BaseClass


class TestCreateVessel(BaseClass):
    @pytest.mark.vessel
    @pytest.mark.run(order=1)
    def test_CreateProject(self, setup, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        vesselType = CreateVesselTypePage(self.driver)
        folder = CreateFoldersPage(self.driver)
        selectAddVesselPage = SelectAddVesselPage(self.driver)
        createProjectPage = CreateVesselPage(self.driver)
        addSection = VesselAddSectionPage(self.driver)

        loginPage.loginPageAdmin(getData)
        vesselType.fillVesselDetails(getData)
        folder.createFolderForVesselType(getData)
        selectAddVesselPage.selectAddVessel()

        createProjectPage.fillVesselDetails(getData)
        addSection.vesselAddSection(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "CreateVesselType"))
    def getData(self, request):
        return request.param
