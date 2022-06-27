tests -> We are going to maintain all our test files (pytest)

testdata -> We are going to maintain all our test data(excel) and getdata()(.py)

reports -> We are going to maintain all our reports

pages -> We are going to maintain all our page objects & actions 
we are going to create different .py file for each page 
    
* Each class going to inherit BasePage class from base package 


    for example: 
        homepage.py -> HomePage -> signin_button, 
        loginpage.py -> LoginPage -> do_login()
        accountsummarypage.py

base -> we going to maintain all our selenium related action
    
    for example:
        def click(locator)
        def enter_text(locator,text)
