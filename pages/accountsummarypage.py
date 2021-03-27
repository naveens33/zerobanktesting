from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class AccountSummaryPage(BasePage):
    pay_bills_link = By.XPATH,"//a[text()='Pay Bills']"

    def click_pay_bills_link(self):
        self.click(self.pay_bills_link)
