import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.AdminInspectionPage import AdminInspectionPage
from pageObjects.LogOutPage import LogOutPage
from pageObjects.ConsultantInsPectionPage import ConsultantInspectionPage
from pageObjects.AdminUpdateStatusPage import AdminUpdateStatusPage
from utilities.BaseClass import BaseClass
from pageObjects.ClientViewProjectPage import ClientViewProjectPage


class TestCreateProject(BaseClass):
    @pytest.mark.vessel
    @pytest.mark.run(order=3)
    def test_CreateProject(self, setup, getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        adminInspection = AdminInspectionPage(self.driver)
        logOut = LogOutPage(self.driver)
        consultantInspection = ConsultantInspectionPage(self.driver)
        adminUpdate = AdminUpdateStatusPage(self.driver)
        clientViewProject = ClientViewProjectPage(self.driver)



        #loginPage.loginPageAdmin(getData)
        #adminInspection.adminInspection(getData)
        #logOut.logOutInAdmin()
        loginPage.loginPageConsultant(getData)
        consultantInspection.consultantInspection(getData)
        logOut.logOutInAdmin()
        loginPage.loginPageAdmin(getData)
        adminUpdate.adminUpdateStatus(getData)

        logOut.logOutInAdmin()
        self.sleep(3)
        loginPage.loginPageClient(getData)
        clientViewProject.clientViewProject(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "AdminInspection"))
    def getData(self, request):
        return request.param
