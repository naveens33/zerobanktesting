from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):
    username =  By.ID,"user_login"
    password = By.ID,"user_password"
    sign_in_button = By.NAME, "submit"
    
    def doLogin(self,uname,pword):
        self.enterText(self.username,uname)
        self.enterText(self.password, pword)
        self.click(self.sign_in_button)