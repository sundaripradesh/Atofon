import pytest
from pageObjects.SelectAddLeadPage  import SelectAddLeadPage
from pageObjects.CreateLeadPage import CreateLeadPage
from pageObjects.SelectAddProjectPage import SelectAddProjectPage
from pageObjects.CreateProjectPage import CreateProjectPage
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.LogOutPage import LogOutPage
from pageObjects.SelectAddVesselPage import SelectAddVesselPage
from pageObjects.CreateVesselPage import CreateVesselPage
from pageObjects.ConsultantPage import ConsultantPage
from pageObjects.InspectionPage import InspectionPage
from pageObjects.ReturnToHomePage import ReturnToHomePage
from pageObjects.ClientPage import ClientPage
from utilities.BaseClass import BaseClass


class TestCreateLead(BaseClass):

    def test_CreateProject(self, setup, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        selectAddVesselPage = SelectAddVesselPage(self.driver)
        createVesselPage = CreateVesselPage(self.driver)
        selectAddLeadPage = SelectAddLeadPage(self.driver)
        createLead = CreateLeadPage(self.driver)
        selectAddProjectPage = SelectAddProjectPage(self.driver)
        createProject = CreateProjectPage(self.driver)
        logOut = LogOutPage(self.driver)
        consultantPage = ConsultantPage(self.driver)
        inspectionPage = InspectionPage(self.driver)
        returnToHome = ReturnToHomePage(self.driver)
        clientPage = ClientPage(self.driver)

        loginPage.loginPageAdmin(getData)
        selectAddVesselPage.selectAddVessel()
        createVesselPage.fillVesselDetails(getData)
        selectAddLeadPage.selectAddLead()
        createLead.fillLeadDetails(getData)
        selectAddProjectPage.selectAddProject()
        createProject.fillProjectDetails(getData)
        self.sleep(3)
        logOut.logOutInAdmin()
        self.sleep(4)
        loginPage.loginPageConsultant(getData)
        consultantPage.updateProjectStatus(getData)
        inspectionPage.inspectionPage(getData)
        returnToHome.returnToHome()
        logOut.logOutInAdmin()
        loginPage.loginPageClient(getData)
        clientPage.clientPage()

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "CreateLead"))
    def getData(self, request):
        return request.param
