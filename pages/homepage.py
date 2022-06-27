from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class HomePage(BasePage):
    _sign_in_button = By.ID, "signin_button"
    _search_field = By.NAME,"searchTerm"
    _online_banking_tab =  By.XPATH, "//strong[text()='Online Banking']"

    def click_sign_in_button(self):
        self._click(self._sign_in_button)

    def do_search(self,search_term):
        self._enter_text(self._search_field,search_term)
        self._enter_text(self._search_field, Keys.ENTER)


