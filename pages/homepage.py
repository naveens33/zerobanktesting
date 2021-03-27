from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.basepage import BasePage


class HomePage(BasePage):
    sign_in_button = (By.ID,"signin_button")
    search_text_field = By.ID,"searchTerm"

    def click_signin_button(self):
        self.click(self.sign_in_button)

    def do_search(self,search_term):
        self.enterText(self.search_text_field,search_term)
        self.enterText(self.search_text_field, Keys.ENTER)
