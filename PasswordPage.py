from selenium import webdriver

class PasswordPage() :

    def enterPassword(self, driver, Password, PasswordFieldXpath):
        element = driver.find_element_by_xpath(PasswordFieldXpath)
        element.send_keys(Password)
        
    
    def clickOnNext(self, driver, NextButtonXpath):
        element = driver.find_element_by_xpath(NextButtonXpath)
        element.click()