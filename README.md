**** Project to Search String in Email body and Subject ****

Pre-requisites :
1) Install python 3 or above
2) Install pip, please follow instructions provided at : https://pypi.org/project/pip/
3) Download chromedriver @ https://chromedriver.chromium.org/downloads and Firefox driver @ https://github.com/mozilla/geckodriver/releases and place it in system path.
4) Download the project code in to any folder from github location : 
5) On the command prompt reach to the project level and run : pip install -r requirements.txt
6) Open file UserDetails.csv and enter the Username, Password and Search String details.
7) Make sure since we are working on gmail, security restrictions are taken care of before execution.
8) You can Change the browser type, Filename and sheetnumber based on the inputs that you want to provide. Else, you can start execution with the preset values.
6) Now run command : pytest 01_DataDriven_tests.py
