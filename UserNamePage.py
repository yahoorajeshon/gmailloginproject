from selenium import webdriver

class UserNamePage() :

    def enterUserName(self, driver, UserName, UserNameParam):
        element = driver.find_element_by_xpath(UserNameParam)
        element.send_keys(UserName)
        
    
    def clickOnNext(self, driver, NextButtonParam):
        element = driver.find_element_by_xpath(NextButtonParam)
        element.click()       