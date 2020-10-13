from selenium import webdriver

class EmailContentCheck() :

    def stringExixtsInSubject(self, driver, Search_String, SubjectFieldXpath):
        element = driver.find_element_by_xpath(SubjectFieldXpath)
        Text = element.text
        if Search_String in Text: 
            print("Search String is present in Subject") 
            return True
        else: 
            print("Search String is not present in Subject")
            return False
    
    def stringExixtsInBody(self, driver, Search_String, BodyFieldXpath):
        element = driver.find_element_by_xpath(BodyFieldXpath)
        Text = element.text
        if Search_String in Text: 
            print("***** Search String is present in Body") 
            return True
        else: 
            print("***** Search String is not present in Body")      
            return False