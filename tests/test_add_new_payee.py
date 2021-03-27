import pytest

from pages.accountsummarypage import AccountSummaryPage
from pages.paybillspage import PayBillsPage
from testdata.read_excel_data import getData


class Test_AddNewPayee():

    paybills = None

    @pytest.fixture(scope="class",autouse=True)
    def setup(self,login):
        self.driver = login
        accountsummary = AccountSummaryPage(self.driver)
        accountsummary.click_pay_bills_link()
        global paybills
        paybills  = PayBillsPage(self.driver)
        paybills.click_add_new_payee_link()

    @pytest.fixture(autouse=True)
    def navigate_back(self):
        yield
        global paybills
        paybills.click_add_new_payee_link()

    @pytest.mark.parametrize("name,adderss,account,details",getData("PayeeDetails.xlsx","PayeeDetails"))
    def test_add_new_payee(self,name,adderss,account,details):
        global paybills
        paybills.add_new_payee(name,adderss,account,details)
        options_text = paybills.get_payee_name_from_payee_dropdown()
        assert name in options_text
