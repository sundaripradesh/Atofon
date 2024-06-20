import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.LoginPage import LoginPage
from pageObjects.SelectAddUserPage import SelectAddUserPage
from utilities.BaseClass import BaseClass


class TestCreateUser(BaseClass):
    def test_CreateUser(self, setup, getData):
         log = self.getLogger()
         loginPage = LoginPage(self.driver)
         selectAddUser = SelectAddUserPage(self.driver)

         loginPage.loginPageAdmin(getData)
         selectAddUser.userAdminCration(getData)
         selectAddUser.userClientCreation(getData)
         selectAddUser.userConsultantCreation(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "CreateUser"))
    def getData(self, request):
        return request.param
