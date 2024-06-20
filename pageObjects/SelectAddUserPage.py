from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class SelectAddUserPage(BaseClass):
    # Admin
    admin = (By.XPATH, "(//ul[@class='ul-tabs vs-tabs--ul ul-tabs-left']/li)[1]")
    client = (By.XPATH, "(//ul[@class='ul-tabs vs-tabs--ul ul-tabs-left']/li)[2]")
    consultant = (By.XPATH, "(//ul[@class='ul-tabs vs-tabs--ul ul-tabs-left']/li)[3]")
    user = (By.XPATH, "//a[@href ='/users']")
    addUser = (By.XPATH, "//span[contains(text(),'Add User')]")
    adminName = (By.XPATH, "(//input[@class='vs-inputx vs-input--input normal hasValue hasIcon'])[1]")
    userRole = (By.XPATH, "//div[@name='role_validation']")
    email = (By.XPATH, "//input[@name ='email']")
    addUserClick = (By.XPATH, "//button[@id ='create-user']")
    changeToClient = (By.XPATH, "(//span[@class ='vs-radio'])[2]")
    changeToConsultant = (By.XPATH, "(//span[@class ='vs-radio'])[3]")
    addUserClient = (By.XPATH, "//a/button/i[@class='vs-icon notranslate icon-scale vs-button--icon  feather icon-plus null']")

    # Client
    organisationName = (By.XPATH, "//input[@name ='organisation_name']")
    subTypeManager = (By.XPATH, "//div[@name ='subtype']/descendant::input")
    owner = (By.XPATH, "//div[@name ='owner']")
    manager = (By.XPATH, "//div[@name='manager']")
    office = (By.XPATH, "//div[@name='office']")
    clientName = (By.XPATH, "//div[@class ='vs-component vs-con-input-label vs-input w-full mt-1 vs-input-primary']/descendant::input[@name ='name']")
    clientEmail = (By.XPATH, "//div[@class ='vs-component vs-con-input-label vs-input w-full mt-1 vs-input-primary']/descendant::input[@name ='email']")

    # Consultant
    consultantName = (By.XPATH, "(//input[@class ='vs-inputx vs-input--input normal hasIcon'])[1]")
    consultantOrganisationName = (By.XPATH, "//input[@name='org_name']")
    emailConsultant = (By.XPATH, "(//input[@name='email'])[1]")
    nationality = (By.XPATH, "//div[@name='nationality']")
    dateOfBirth = (By.XPATH, "//input[@name ='date_of_birth']")
    placeOfBirth = (By.XPATH, "//div[@class = 'vs-component vs-con-input-label vs-input w-full mt-1 vs-input-primary']//descendant::input[@name ='place_of_birth']")
    streetOne = (By.XPATH, "//input[@name ='street1']")
    streetTwo = (By.XPATH, "//input[@name ='street2']")
    city = (By.XPATH, "//input[@name ='city']")
    country = (By.XPATH, "//div[@name ='country']//descendant::input")
    postalCode = (By.XPATH, "//input[@name ='postal_code']")
    rank = (By.XPATH, "//input[@name ='rank']")
    dateOfJoining = (By.XPATH, "//input[@name ='date_of_joining']")
    workMobileNumber = (By.XPATH, "//input[@name ='work_mobile_number']")
    homeTelephoneNumber = (By.XPATH, "//input[@name ='home_telephone_number']")
    alternateMobileNumber = (By.XPATH, "//input[@name='alternate_mobile_number']")
    homeEmailAddress = (By.XPATH, "//input[@name='home_email_address']")
    contactName = (By.XPATH, "//input[@name='contact_name']")
    mobileNumber = (By.XPATH, "//input[@name='mobile_number']")
    kinAlternateMobileNumber = (By.XPATH, "//input[@name='kin_alternate_number']")
    kinEmailAddress = (By.XPATH, "(//input[@name ='email'])[2]")
    addUserConsultant = (By.XPATH, "//div[@class ='flex justify-center mt-2']//child::button[@id ='update-profile']")

    def __init__(self, driver):
        self.driver = driver

    def userAdminCration(self,getData):
        self.elementClick(self.driver.find_element(*SelectAddUserPage.user))
        self.elementClick(self.driver.find_element(*SelectAddUserPage.addUser))
        self.sleep(2)
        self.sendKeys(getData["AdminName"], self.driver.find_element(*SelectAddUserPage.adminName))
        self.dropdownSelectByLi(getData["UserRole"], self.driver.find_element(*SelectAddUserPage.userRole))
        self.sendKeys(getData["AdminEmail"], self.driver.find_element(*SelectAddUserPage.email))
        self.elementClick(self.driver.find_element(*SelectAddUserPage.addUserClick))

    def userClientCreation(self,getData):
        self.elementClick(self.driver.find_element(*SelectAddUserPage.addUserClient))
        self.elementClickByJS(self.driver.find_element(*SelectAddUserPage.changeToClient))
        self.sendKeys(getData["ClientName"], self.driver.find_element(*SelectAddUserPage.clientName))
        self.sendKeys(getData["OrganisationName"], self.driver.find_element(*SelectAddUserPage.organisationName))
        self.sendKeys(getData["ClientEmail"], self.driver.find_element(*SelectAddUserPage.clientEmail))
        self.dropdownSelectByLi(getData["SubTypeManager"], self.driver.find_element(*SelectAddUserPage.subTypeManager))
        self.sleep(2)
        self.dropdownSelectByLi(getData["Owner"], self.driver.find_element(*SelectAddUserPage.owner))
        self.sleep(2)
        self.dropdownSelectByLi(getData["Manager"], self.driver.find_element(*SelectAddUserPage.manager))
        self.sleep(2)
        self.dropdownSelectByLi(getData["Office"], self.driver.find_element(*SelectAddUserPage.office))
        self.elementClick(self.driver.find_element(*SelectAddUserPage.addUserClick))

    def userConsultantCreation(self,getData):
        self.sleep(2)
        self.elementClick(self.driver.find_element(*SelectAddUserPage.addUserClient))
        self.elementClickByJS(self.driver.find_element(*SelectAddUserPage.changeToConsultant))
        self.sendKeys(getData["ConsultantName"], self.driver.find_element(*SelectAddUserPage.consultantName))
        self.sendKeys(getData["ConsultantOrganisationName"], self.driver.find_element(*SelectAddUserPage.consultantOrganisationName))
        self.sendKeys(getData["EmailConsultant"], self.driver.find_element(*SelectAddUserPage.emailConsultant))
        self.sleep(2)
        self.dropdownSelectByLi(getData["Nationality"], self.driver.find_element(*SelectAddUserPage.nationality))
        self.elementClickByJS(self.driver.find_element(*SelectAddUserPage.dateOfBirth))
        self.datepickerBirthDate(getData["BirthMonth"], getData["BirthYear"],getData["BirthDay"])
        self.sendKeys(getData["PlaceOfBirth"], self.driver.find_element(*SelectAddUserPage.placeOfBirth))
        self.sendKeys(getData["StreetOne"], self.driver.find_element(*SelectAddUserPage.streetOne))
        self.sendKeys(getData["StreetTwo"], self.driver.find_element(*SelectAddUserPage.streetTwo))
        self.sendKeys(getData["City"], self.driver.find_element(*SelectAddUserPage.city))
        self.sleep(2)
        self.dropdownSelectByLi(getData["Country"], self.driver.find_element(*SelectAddUserPage.country))
        self.sendKeys(getData["PostalCode"], self.driver.find_element(*SelectAddUserPage.postalCode))
        self.sendKeys(getData["Rank"], self.driver.find_element(*SelectAddUserPage.rank))
        self.sleep(2)
        self.elementClickByJS(self.driver.find_element(*SelectAddUserPage.dateOfJoining))
        self.datepickerJoiningDate(getData["JoiningMonth"], getData["JoiningYear"], getData["JoiningDay"])
        self.sendKeys(getData["WorkMobileNumber"], self.driver.find_element(*SelectAddUserPage.workMobileNumber))
        self.sendKeys(getData["HomeTelePhoneNumber"], self.driver.find_element(*SelectAddUserPage.homeTelephoneNumber))
        self.sendKeys(getData["AlternateMobileNumber"], self.driver.find_element(*SelectAddUserPage.alternateMobileNumber))
        self.sendKeys(getData["HomeEmailAddress"], self.driver.find_element(*SelectAddUserPage.homeEmailAddress))
        self.sendKeys(getData["ContactName"], self.driver.find_element(*SelectAddUserPage.contactName))
        self.sendKeys(getData["MobileNumber"], self.driver.find_element(*SelectAddUserPage.mobileNumber))
        self.sendKeys(getData["KinAlternateMobileNumber"], self.driver.find_element(*SelectAddUserPage.kinAlternateMobileNumber))
        self.sendKeys(getData["KinEmailAddress"], self.driver.find_element(*SelectAddUserPage.kinEmailAddress))
        self.webScroll(getData["Scrolling"])
        self.elementClickByJS(self.driver.find_element(*SelectAddUserPage.addUserConsultant))
        self.sleep(10)


















