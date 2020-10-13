import pytest
import sys
import os
import time
from datetime import datetime
from UserNamePage import UserNamePage
from PasswordPage import PasswordPage
from LoggedInEmailPage import LoggedInEmailPage
from EmailContentCheck import EmailContentCheck
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  
import logging
import csv
import yaml

with open(r'Executiondeciders.yaml') as file:
        yaml_data = yaml.load(file)
  
def read_test_data_from_csv():
    test_data = []
    FileNameParam = yaml_data['FileName']
    cwd = os.getcwd()
    FilePath = cwd + "\\" + FileNameParam   
    with open(FilePath,'r') as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        logging.debug(data)
        next(data)
        for row in data:
            test_data.append(row)
    logging.debug(test_data)
    return test_data

def assert_Failure_Messages(FailureMessage, driver):
    print(FailureMessage)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file('screenshot-%s.png' % now)
    driver.quit()

@pytest.mark.parametrize("UserName, Password, SearchString", read_test_data_from_csv())

def test_Email_with_String_In_Subject_And_Body(UserName, Password, SearchString):   
    #Getting browser Name from yaml file
    browserName = yaml_data['browserType']
    logging.debug("***** "+ browserName + " is the browser chosen for execution")
    #Creating Webdriver for execution
    if browserName == 'Chrome':
        driver = webdriver.Chrome()
        logging.debug("***** Chrome driver opened")
    if browserName == 'Firefox':
        driver = webdriver.Firefox()
        logging.debug("***** Firefox driver opened")
    element = WebDriverWait(driver, 20)
    #Loading the URL
    URLParam = yaml_data['URLName']
    driver.get(URLParam)
    logging.debug("***** URL : "+URLParam+" is loaded")
    #Maximizing window
    driver.maximize_window()
    logging.debug("***** window maximized")
    #Accessing actions and elements in User Name page
    UserNameParam = yaml_data['UserNameFieldXpath']    
    US1 = UserNamePage()
    element.until(EC.element_to_be_clickable((By.XPATH, UserNameParam)))
    US1.enterUserName(driver, UserName, UserNameParam)
    logging.debug("***** UserName is entered")
    NextButtonParam = yaml_data['UserNameNextButtonXpath']
    US1.clickOnNext(driver, NextButtonParam)
    logging.debug("***** clicked on next in username page")
    #Accessing actions and elements in Password page
    PasswordParam = yaml_data['PasswordFieldXpath'] 
    PS1 = PasswordPage()
    try:
        element.until(EC.element_to_be_clickable((By.XPATH, PasswordParam)))
    except:
        assert_Failure_Messages("Password field was not loaded, please check your username", driver)
    PS1.enterPassword(driver, Password, PasswordParam)
    logging.debug("***** Password is entered")
    NextButtonParam = yaml_data['PasswordNextButtonXpath']
    PS1.clickOnNext(driver, NextButtonParam)
    logging.debug("***** Next clicked on password page")
    #Accessing actions and elements in Logged in Email Page
    SearchFieldParam = yaml_data['SearchFieldXpath']
    # StringToSearch = Sheet.cell_value(1,2)
    LEP1 = LoggedInEmailPage()
    try:
        element.until(EC.element_to_be_clickable((By.XPATH, SearchFieldParam)))
    except:
        assert_Failure_Messages("Search field was not loaded, please check screenshot to look for error", driver)
    LEP1.enterSearchString(driver, SearchString, SearchFieldParam)
    logging.debug("***** Search String Entered")
    SearchButtonParam = yaml_data['SearchButtonXpath']
    LEP1.clickOnSearchButton(driver, SearchButtonParam)
    logging.debug("***** Search button clicked")
    #Clicking on First email after search is completed
    EmailThreadsParam = yaml_data['EmailThreadsXpath']
    assert ("No messages matched your search" in driver.page_source), assert_Failure_Messages("No email with the search string found", driver)
    LEP1.clickOnEmail(driver, SearchString, EmailThreadsParam)
    logging.debug("***** Email with Search String specified is clicked and opened")
    #Checking the content of the email both subject and body if it contains the string we are searching.
    SubjectFieldParam = yaml_data['SubjectFieldXpath']
    ECC1 = EmailContentCheck()
    time.sleep(3)
    logging.debug("***** Performing check for if string is present in Subject line")
    Subj_status = ECC1.stringExixtsInSubject(driver, SearchString, SubjectFieldParam)
    assert Subj_status == True, assert_Failure_Messages("Search text not found in Subject field", driver)
    time.sleep(3)
    BodyFieldParam = yaml_data['BodyFieldXpath']
    logging.debug("***** Performing check for if string is present in Subject line")
    Body_status = ECC1.stringExixtsInBody(driver, SearchString, BodyFieldParam)
    assert Body_status == True, assert_Failure_Messages("Search text not found in Body field", driver)
    driver.quit()