import pytest
from TestData.RetrieveExcelData import RetrieveExcelData
from pageObjects.salusWebPage import salusWebPage
from utilities.BaseClass import BaseClass


class TestCreateProject(BaseClass):

    def test_CreateProject(self, setup, getData):
        log = self.getLogger()
        webPage = salusWebPage(self.driver)

        webPage.webPage(getData)

    @pytest.fixture(params=RetrieveExcelData.getTestData("TestCase1", "Web"))
    def getData(self, request):
        return request.param
