import pytest
from pages.accountsummarypage import AccountSummaryPage
from pages.paybillspage import PayBillsPage
from testdata.datagetter import getData


class TestAddNewPayee():

    @pytest.fixture(scope="class",autouse=True)
    def navigate_to_paybills_page(self,login,driver):
        asp = AccountSummaryPage(driver)
        asp.click_pay_bills_link()

    @pytest.fixture(autouse=True)
    def navigate_to_add_new_payee_page(self,login,driver):
        self.paybills = PayBillsPage(driver)
        self.paybills.click_add_new_payee_link()

    @pytest.mark.parametrize("name,address,account,details", getData(r"TestData.xls","AddNewPayee"))
    def test_add_new_payee(self,name,address,account,details):
        self.paybills.do_add_a_new_payee(name,address,account,details)