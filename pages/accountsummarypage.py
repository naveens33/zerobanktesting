from selenium.webdriver.common.by import By
from base.basepage import BasePage


class AccountSummaryPage(BasePage):
    _pay_bills_link = By.LINK_TEXT,"Pay Bills"

    def click_pay_bills_link(self):
        self._click(self._pay_bills_link)