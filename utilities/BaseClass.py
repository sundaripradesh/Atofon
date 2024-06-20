import inspect
import logging
import time
import traceback
import pytest
import autoit
from select import select
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, \
    StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, element = None):
         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
         element.click()

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.getLogger().error("Failed to get page title")
            traceback.print_stack()
            return False

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def sleep(self, sec, info=""):
        if info is not None:
            self.getLogger().info("Wait :: " + str(sec) + " seconds for " + info)
            try:
                time.sleep(sec)
            except:
                traceback.print_stack()

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches
        :param expectedList: Expected List
        :param actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list
        :param expectedList: Expected List
        :param actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True

    def verifyTextContains(self, actualText, expectedText):
        """
        verify actual text contains expected text string
        :param actualText: Actual Text
        :param expectedText: Expected Text
        """
        self.getLogger().info("Actual Text From Application Web UI --> :: " + actualText)
        self.getLogger().info("Expected Text From Application Web UI --> :: " + expectedText)

        if expectedText.lower() in actualText.lower():
            self.getLogger().info("### VERIFICATIONS CONTAINS !!!")
            return True
        else:
            self.getLogger().error("### VERIFICATIONS DOES NOT CONTAINS !!!")

    def verifyTextMatch(self, actualText, expectedText):
        """
        verify text match
        :param actualText: Actual Text
        :param expectedText: Expected Text
        """
        self.getLogger().info("Actual Text From Application Web UI --> :: " + actualText)
        self.getLogger().info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.getLogger().info("### VERIFICATIONS MATCHED !!!")
            return True
        else:
            self.getLogger().error("### VERIFICATIONS DOES NOT MATCHED !!!")

    def getTitle(self):
        return self.driver.title

    def sendKeys(self, data, element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            element.click()
            element.send_keys(data)
            self.getLogger().info(str(data) + " is entered into text box")
        except:
            self.getLogger().error(data + " is not entered into text box")
            traceback.print_stack()

    def clear(self, element=None):
        """
        Clear the data

        """
        try:
            element.click()
            element.clear()
            self.getLogger().info("text is clear")
        except:
             self.getLogger().info("text is clear")

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.getLogger().info("Locator type" + locatorType + "not correct/supported")
        return False

    def dropdownSelectByLi(self, data, element=None):
        try:
            action = ActionChains(self.driver)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(element))
            element.click()
            list = self.driver.find_elements(By.XPATH, "//ul[@class ='vs__dropdown-menu']//child:: li")
            for option in list:
                if option.text == data:
                    action.scroll_to_element(option)
                    option.click()
                    break
        except:
            self.getLogger().error("DropdownValue is not selected")
            return False

    def dropdownSelectByLiClose(self, data, element=None):
        try:
            action = ActionChains(self.driver)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(element))
            element.click()
            list = self.driver.find_elements(By.XPATH, "//ul[@class ='vs__dropdown-menu']//child:: li")
            for option in list:
                if option.text == data:
                    action.scroll_to_element(option)
                    option.click()
                    element = self.driver.switch_to.active_element
                    element.send_keys(Keys.ESCAPE)
                    break

        except:
            self.getLogger().error("DropdownValue is not selected")
            return False

    def dropdownMultiSelectByLiStale(self, data, element=None):
        as_list = data.split(',')
        for data1 in as_list:
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
                element.click()
                list = self.driver.find_elements(By.XPATH, "//ul[@class ='vs__dropdown-menu']//child:: li")
                for option in list:
                    if option.text == data1:
                        time.sleep(1)
                        option.click()
                        element = self.driver.switch_to.active_element
                        element.send_keys(Keys.ESCAPE)
                        break
            except StaleElementReferenceException:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
                list1 = self.driver.find_elements(By.XPATH, "//ul[@class ='vs__dropdown-menu']//child:: li")
                for option1 in list1:
                    if option1.text == data1:
                        time.sleep(3)
                        option1.click()
                        element = self.driver.switch_to.active_element
                        element.send_keys(Keys.ESCAPE)
                self.getLogger().error("DropdownValue is not selected")
                return False
    def isElementSelected(self, element=None):
        isSelected = None
        try:
            isSelected = element.is_selected()
            self.getLogger().info("Element found and selected")
        except:
            self.getLogger().error("Element not selected")

        return isSelected

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.getLogger().info("Element list found with locator: " + locator +
                                  " and locatorType: " + locatorType)
        except:
            self.getLogger().error("Element list not found with locator: " + locator +
                                   " and locatorType: " + locatorType)

        return element

    def  elementClick(self, element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            element.click()
            self.getLogger().info("clicked on the element")
        except:
            self.getLogger().error("cannot click on the element")
            traceback.print_stack()

    def elementClickByJS(self, element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            self.driver.execute_script("arguments[0].click();", element)
            self.getLogger().info("clicked on the element")
        except:
            self.getLogger().error("cannot click on the element")
            traceback.print_stack()

    def elementHover(self, element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            self.getLogger().info("hover to element")
        except:
            self.getLogger().error("cannot hover to the element")
            traceback.print_stack()

    def elementHoverClick(self, element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            hover = ActionChains(self.driver).move_to_element(element)
            hover.click()
            hover.perform()

            self.getLogger().info("hover to element")
        except:
            self.getLogger().error("cannot hover to the element")
            traceback.print_stack()

    def elementHoverSend(self, data, element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            hover = ActionChains(self.driver).click(element)

            hover.send_keys(data)
            hover.perform()

            self.getLogger().info("hover to element")
        except:
            self.getLogger().error("cannot hover to the element")
            traceback.print_stack()

    def clearKeys(self, element=None):
        """
        Clear keys of an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            element.clear()
            self.getLogger().info("Text box is cleared")
        except:
            self.getLogger().error("cannot clear data of the element")
            traceback.print_stack()

    def getText(self, element=None):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
        except:
            self.getLogger().error("Failed to get text on element")
            traceback.print_stack()
            text = None
        return text

    def isElementPresent(self, element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if element is not None:
                self.getLogger().info("Element found")
                return True
            else:
                self.getLogger().error("Element not found")
                return False
        except:
            self.getLogger().error("Element not found")
            return False

    def isElementDisplayed(self, element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if element is not None:
                isDisplayed = element.is_displayed()
                self.getLogger().info("Element is displayed")
            else:
                self.getLogger().error("Element is not displayed")
            return isDisplayed
        except:
            self.getLogger().error("Element is not displayed")
            return False

    def elementPresenceCheck(self, elementList=None):
        try:
            if len(elementList) > 0:
                self.getLogger().info("Element Found")
                return True
            else:
                self.getLogger().info("Element not found")
                return False
        except:
            self.getLogger().info("Element not found")
            return False

    def waitForElement(self, element=None, timeout=10, pollFrequency=0.5):

        try:
            self.getLogger().info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            wait.until(EC.element_to_be_clickable(element))

            self.getLogger().info("Element appeared on the web page")

        except:
            self.getLogger().info("Element not appeared on the web page")
            return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -2000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 3500);")

    def scrollIntoView(self, element=None):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            self.getLogger().error("Failed to scroll")
            traceback.print_stack()
            return False

    def scrollByHeight(self):
        try:
            return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except:
            self.getLogger().error("Failed to scroll by height")
            traceback.print_stack()
            return False

    def getURL(self):
        '''
        Get the current URL
        :return: current URL
        '''
        currentURL = self.driver.current_url
        return currentURL

    def pageBack(self):
        '''
        page back the browser
        '''
        self.driver.execute_script("window.history.go(-1)")

    def getAttributeValue(self, element=None, attribute=""):
        '''
        get attribute value
        '''
        try:
            attribute_value = element.get_attribute(attribute)
        except:
            self.getLogger().error("Failed to get " + attribute + " in element")
            traceback.print_stack()
            attribute_value = None
        return attribute_value

    def refresh(self):
        self.driver.get(self.driver.current_url)

    def datepicker(self, Month,Year, Date):

        time.sleep(2)
        datepicker_month = Select(self.driver.find_element(By.XPATH, "//select[@class ='flatpickr-monthDropdown-months']"))
        datepicker_month.select_by_visible_text(Month)

        while True:
            year = self.driver.find_element(By.XPATH, "//input[@type ='number']")
            value = self.driver.execute_script("return arguments[0].value;", year)
            print(value)
            if value == Year:

               break
            else:
                self.driver.find_element(By.XPATH, "//span[@class='arrowUp']").click()

        Days = self.driver.find_elements(By.XPATH, "//div[@class ='dayContainer']/child::span[@class='flatpickr-day']")
        for days in Days:

            if days.text == Date:
                days.click()
                break

    def datepickerBirthDate(self, Month,Year, Date):

        time.sleep(2)
        datepicker_month = Select(self.driver.find_element(By.XPATH, "(//select[@class ='flatpickr-monthDropdown-months'])[1]"))
        datepicker_month.select_by_visible_text(Month)

        while True:
            year = self.driver.find_element(By.XPATH, "(//input[@type='number'])[6]")
            value = self.driver.execute_script("return arguments[0].value;", year)

            if value == Year:
               break
            else:
                self.driver.find_element(By.XPATH, "//span[@class='arrowDown']").click()

        Days = self.driver.find_elements(By.XPATH, "//div[@class ='dayContainer']/child::span[@class='flatpickr-day']")
        for days in Days:

            if days.text == Date:
                days.click()
                break

    def datepickerJoiningDate(self, Month,Year, Date):

        time.sleep(2)
        datepicker_month = Select(self.driver.find_element(By.XPATH, "(//select[@class ='flatpickr-monthDropdown-months'])[2]"))
        datepicker_month.select_by_visible_text(Month)

        while True:
            year = self.driver.find_element(By.XPATH, "(//input[@type='number'])[7]")
            value = self.driver.execute_script("return arguments[0].value;", year)

            if value == Year:
               break
            else:
                self.driver.find_element(By.XPATH, "(//span[@class='arrowUp'])[2]").click()

        Days = self.driver.find_elements(By.XPATH, "//div[@class ='dayContainer']/child::span[@class='flatpickr-day']")
        for days in Days:

            if days.text == Date:
                days.click()
                break

    def datepickerLead(self, Month, Date):
       time.sleep(2)
       while True:
            months = self.driver.find_element(By.XPATH, "//span[@class='day__month_btn up']").text
            if months == Month:
              break
            else:
                self.driver.find_element(By.XPATH, "(// span[@class ='next'])[1]").click()

       Days = self.driver.find_elements(By.XPATH, "//div[@class='vdp-datepicker__calendar']//self::div//child::div//child::span[@class ='cell day']/following-sibling::span")
       for days in Days:
            if days.text == Date:
                days.click()
                break

    def setattribute(self, element):
        self.driver.execute_script("arguments[0].setAttribute('value', '7')", element)

    def slider(self, element=None):
        try:
            sliderscroll = ActionChains(self.driver).drag_and_drop_by_offset(element, 60, 0)
            sliderscroll.click()
            sliderscroll.perform()
        except:
            self.getLogger().error("cannot scroll on the element")
            traceback.print_stack()

    def switchrole(self, data):
        try:
            self.driver.find_element(By.XPATH, "//img[@class ='avatar rounded-circle']").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//*[name()='svg'][@class ='c-icon']").click()
            self.driver.find_element(By.XPATH, "//div[@name ='user_type']").click()

            Switch = self.driver.find_elements(By.XPATH, "//ul[@class='vs__dropdown-menu']/child::li")
            for switch in Switch:
              if switch.text == data:
                switch.click()
                break
            self.driver.find_element(By.XPATH, "//button[@form ='switchUserType']").click()
        except:
            self.getLogger().error("cannot switch the role of  the element")
            traceback.print_stack()

    def candidate(self):

            action = ActionChains(self.driver)
            time.sleep(2)
            ele = self.driver.find_element(By.XPATH, "//div/span[contains(text(),'Candidates')]")
            ele1 = self.driver.find_element(By.XPATH, "//a[@href ='/candidate-list']/em[@class ='fas fa-user-friends mr-2']")
            action.move_to_element(ele).move_to_element(ele).move_to_element(ele1).click().perform()

    def selectCandidate(self):
        try:
            action = ActionChains(self.driver)
            time.sleep(2)
            ele = self.driver.find_element(By.XPATH, "//div/span[contains(text(),'Candidates')]")
            ele1 = self.driver.find_element(By.XPATH, "//a[@href ='/candidate-list']/em[@class ='fas fa-user-friends mr-2']")
            action.move_to_element(ele).move_to_element(ele).move_to_element(ele1).click().perform()
            time.sleep(1)
            candidateDetails = self.driver.find_element(By.XPATH, "//button[contains(text(),'More Details')][1]")
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", candidateDetails)

        except:
            self.getLogger().error("cannot select the candidate")
            traceback.print_stack()

    def selectTheProcess(self, data, data1):
        try:
             moveTo  = self.driver.find_element(By.XPATH, "//button[contains(text(),'Refresh')]")
             self.driver.execute_script("arguments[0].scrollIntoView();", moveTo)
             Process = self.driver.find_elements(By.XPATH, "//ul[@id ='infoNav']/li/a")
             for process in Process:
                if process.text == data:
                    process.click()
                    break
             scrollTo = self.driver.find_element(By.XPATH, "//div[@class ='info-content mt-2']")
             self.driver.execute_script("arguments[0].scrollIntoView();", scrollTo)
             time.sleep(1)
             self.driver.find_element(By.XPATH, "//div/div/i[@class ='fas fa-ellipsis-v']").click()
             Recruitment = self.driver.find_elements(By.XPATH, "//div[@class='dropdown-menu show']/child::a")
             time.sleep(1)
             for recruitment in Recruitment:
                if recruitment.text == data1:
                    recruitment.click()
                    break
        except:
            self.getLogger().error("cannot select the recruitment process")

    def selectTheProject(self, Data):
         ProjectRows = self.driver.find_elements(By.XPATH, "//div[@class ='vs-con-tbody vs-table--tbody ']//child::tr")
         Rows = ProjectRows.size
         ProjectColumns = self.driver.find_element(By.XPATH, " //div[@class ='vs-con-tbody vs-table--tbody ']//child::tr/child::td")
         Columns = ProjectColumns.size
         for i in range (Rows):
             for j in range (Columns):
                 project = self.driver.find_element(By.XPATH, "((//div[@class ='vs-con-tbody vs-table--tbody ']/table/tr)[i]/td)[j]").text
                 if project == Data:
                     break
                 else:
                     self.driver.find_element(By.XPATH,"(//i[@class ='vs-icon notranslate icon-scale material-icons null'])[2]")

    def selectMasterTypes(self,Data):
         MasterTypes = self.driver.find_elements(By.XPATH, "(//ul[@class='vs-sidebar-group-items'])[1]/descendant::span/following-sibling::span")
         for masterTypes in MasterTypes:
             if masterTypes.text == Data:
                 masterTypes.click()
                 break

    def pagination (self, Data):
        Pages = self.driver.find_elements(By.XPATH, "//ul[@class='vs-pagination--ul']/li/span")
        for pages in Pages:
            print(pages.text)
            if pages.text == Data:
                pages.click()
                break

    def scrollinWheel(self, element):
        action = ActionChains(self.driver)
        action.scroll_to_element(element).perform()

    def section(self, Data):

        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-3 vs-button-primary vs-button-border includeIcon includeIconOnly small']").click()
        sectionName = self.driver.find_element(By.XPATH, "(//input[@class='vs-inputx vs-input--input normal hasValue'])[1]")
        sectionName.send_keys(Data)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Create')]").click()

    def createMap(self):

        self.sleep(2)
        mapSection  = self.driver.find_element(By.XPATH, "//div/descendant::span[contains(text(),'Map Section')]")
        self.driver.execute_script("arguments[0].click();", mapSection)
        self.sleep(1)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Confirm')]").click()


    def subFolderClick(self,Data):
        self.sleep(2)
        chooseFile = self.driver.find_element(By.XPATH, "//input[@accept='image/*']")
        self.driver.execute_script("arguments[0].click();", chooseFile)
        time.sleep(2)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\ALAGU SUNDARI\\PycharmProjects\\IQ-CRM_Admin\\TestData\\20240204 (290)_1024x768.jpg")
        time.sleep(2)
        autoit.control_click("Open", "Button1")
        self.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-3 vs-button-primary vs-button-border includeIcon includeIconOnly small']").click()
        self.driver.find_element(By.XPATH, "(//input[@class='vs-inputx vs-input--input normal hasValue'])[1]").send_keys(Data)
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-5 vs-button-primary vs-button-filled']").click()

    def subFolderMapping(self):
        self.driver.find_element(By.XPATH, "//button[@class='vs-con-dropdown parent-dropdown']").click()
        self.driver.find_element(By.XPATH, "//div[@class='con-vs-dropdown--menu vs-dropdown-menu rightx notHeight']/descendant::span[contains(text(),'Map Folder')]").click()
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-5 vs-button-primary vs-button-filled']").click()
        self.driver.find_element(By.XPATH, "//div[@class='pin cursor-grab']").click()
        self.webScroll("up")
        self.driver.find_element(By.XPATH, "(//button[@class='vs-component vs-button p-0 vs-button-dark vs-button-flat includeIcon includeIconOnly'])[2]").click()



    def subFolderMappingInspection(self):
         self.driver.find_element(By.XPATH, "//button[@class='vs-con-dropdown parent-dropdown']").click()
         self.driver.find_element(By.XPATH, "//div[@class='con-vs-dropdown--menu vs-dropdown-menu rightx notHeight']/descendant::span[contains(text(),'Map Folder')]").click()
         self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-5 vs-button-primary vs-button-filled']").click()
         self.driver.find_element(By.XPATH, "//div[@class='pin cursor-grab']").click()

    def uploadPhotos(self,data):
        self.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='image-card text-center position-relative']").click()
        time.sleep(2)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", data)
        time.sleep(2)
        autoit.control_click("Open", "Button1")

    def closeFolder(self):
        self.webScroll("up")
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button mr-1 vs-button-primary vs-button-flat includeIcon includeIconOnly']").click()
        self.sleep(2)
        self.driver.find_element(By.XPATH, "(//i[@class='vs-icon notranslate icon-scale vs-button--icon  feather icon-arrow-left null'])[2]").click()

    def dragTheLocationOne(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, -90, 0).double_click(drag).perform()

    def dragTheLocationTwo(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, 0, -20).double_click(drag).perform()

    def dragTheLocationThree(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, -300, 20).double_click(drag).perform()

    def dragTheLocationFour(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, -200, 30).double_click(drag).perform()

    def dragTheLocationFive(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, -40, 80).double_click(drag).perform()

    def dragTheLocationSix(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, -270, -90).double_click(drag).perform()

    def dragTheLocationSeven(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, 80, 21).double_click(drag).perform()

    def dragTheLocationSubFolder(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, 40, -50).double_click(drag).perform()

    def clientCloseFolder(self):
        self.webScroll("up")
        self.sleep(2)
        self.driver.find_element(By.XPATH, "//i[@class='vs-icon notranslate icon-scale vs-button--icon  material-icons null']").click()
        self.sleep(2)
        self.driver.find_element(By.XPATH, "(//i[@class='vs-icon notranslate icon-scale vs-button--icon  feather icon-arrow-left null'])[2]").click()

    def removeMapFolder(self,Data):
        self.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-3 vs-button-primary vs-button-border includeIcon includeIconOnly small']").click()
        self.driver.find_element(By.XPATH, "(//input[@class='vs-inputx vs-input--input normal hasValue'])[1]").send_keys(Data)
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-5 vs-button-primary vs-button-filled']").click()


    def subFolderMappingOne(self):
        self.driver.find_element(By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[1]").click()
        self.driver.find_element(By.XPATH, "//div[@class='con-vs-dropdown--menu vs-dropdown-menu rightx notHeight']/descendant::span[contains(text(),'Map Folder')]").click()
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-5 vs-button-primary vs-button-filled']").click()
        self.driver.find_element(By.XPATH, "//div[@class='pin cursor-grab']").click()

    def subFolderMappingTwo(self):
        self.driver.find_element(By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[2]").click()
        self.driver.find_element(By.XPATH, "//div[@class='con-vs-dropdown--menu vs-dropdown-menu rightx notHeight']/descendant::span[contains(text(),'Map Folder')]").click()
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-5 vs-button-primary vs-button-filled']").click()
        self.driver.find_element(By.XPATH, "(//div[@class='pin cursor-grab'])[2]").click()

    def subFolderMappingThree(self):
        self.driver.find_element(By.XPATH, "(//button[@class='vs-con-dropdown parent-dropdown'])[3]").click()
        self.driver.find_element(By.XPATH, "//div[@class='con-vs-dropdown--menu vs-dropdown-menu rightx notHeight']/descendant::span[contains(text(),'Map Folder')]").click()
        self.driver.find_element(By.XPATH, "//button[@class='vs-component vs-button ml-5 vs-button-primary vs-button-filled']").click()
        self.driver.find_element(By.XPATH, "(//div[@class='pin cursor-grab'])[3]").click()

    def send(self, element):

        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.BACKSPACE)


    def dragTheLocationSubFolderOne(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, 40, 40).double_click(drag).perform()

    def dragTheLocationSubFolderTwo(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, 10, -20).double_click(drag).perform()

    def dragTheLocationSubFolderThree(self, drag):
        action = ActionChains(self.driver)
        self.sleep(3)
        target = self.driver.find_element(By.XPATH, "//img[@class='cursor-auto']")
        action.click_and_hold(drag).move_to_element_with_offset(target, 80, 30).double_click(drag).perform()












