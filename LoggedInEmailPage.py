from selenium import webdriver

class LoggedInEmailPage() :

    def enterSearchString(self, driver, Search_String, SearchFieldXpath):
        element = driver.find_element_by_xpath(SearchFieldXpath)
        element.send_keys(Search_String)
        
    
    def clickOnSearchButton(self, driver, SearchButtonXpath):
        element = driver.find_element_by_xpath(SearchButtonXpath)
        element.click()
        
    def clickOnEmail(self, driver, Search_String, EmailThreads):        
        for element in driver.find_elements_by_xpath(EmailThreads):
            if Search_String in element.text:
                element.click()
                break
            else:
                continue
        
        
# if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # driver.get("http://www.gmail.com")
    # driver.maximize_window()
    # us1 = UserNamePage(driver)
    # us1.enterUserName('Username1')
    # us1.clickOnNext()
    
        