from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class PayBillsPage(BasePage):
    add_new_payee_link =  By.LINK_TEXT,"Add New Payee"
    payee_name = By.ID,"np_new_payee_name"
    payee_address = By.ID, "np_new_payee_address"
    payee_account = By.ID,"np_new_payee_account"
    payee_details = By.ID, "np_new_payee_details"
    add_button = By.ID,"add_new_payee"
    payee_dropdown = By.ID,"sp_payee"

    def click_add_new_payee_link(self):
        self.click(self.add_new_payee_link)

    def add_new_payee(self,name,address,account,details):
        self.wait_for_element(self.payee_name,"visibility").send_keys(name)
        self.enterText(self.payee_address, address)
        self.enterText(self.payee_account, account)
        self.enterText(self.payee_details, details)
        self.click(self.add_button)

    def get_payee_name_from_payee_dropdown(self):
        self.wait_for_element(self.payee_dropdown,"visibility")
        options = self.get_options(self.payee_dropdown)
        options_text = []
        for option in options:
            options_text.append(option.text)
        return options_text