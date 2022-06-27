from selenium.webdriver.common.by import By
from base.basepage import BasePage


class PayBillsPage(BasePage):
    _add_new_payee_link = By.LINK_TEXT, "Add New Payee"
    _name_field = By.ID, "np_new_payee_name"
    _address_field = By.ID, "np_new_payee_address"
    _account_field = By.ID, "np_new_payee_account"
    _details_field = By.ID, "np_new_payee_details"
    _add_button = By.ID, "add_new_payee"

    def click_add_new_payee_link(self):
        self._click(self._add_new_payee_link)

    def do_add_a_new_payee(self, name, address, account, details):
        self._wait_for_element(self._name_field,"visibility")
        self._enter_text(self._name_field, name)
        self._enter_text(self._address_field,address)
        self._enter_text(self._account_field,account)
        self._enter_text(self._details_field,details)
        self._click(self._add_button)

