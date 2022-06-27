import pytest

from pages.homepage import HomePage
from pages.searchpage import SearchPage
from testdata.datagetter import getData


class Test_Search:

    @pytest.mark.parametrize("search_term,count", getData(r"TestData.xls", "Search"))
    def test_search(self,driver,search_term,count):
        home = HomePage(driver)
        home.do_search(search_term)
        search = SearchPage(driver)
        assert len(search.get_search_result()) == count
