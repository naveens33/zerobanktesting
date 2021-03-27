import pytest

from pages.homepage import HomePage
from pages.searchpage import SearchPage


class TestSearch:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,driver):
        global driver_
        driver_ = driver

    def test_search(self):
        homepage = HomePage(driver_)
        homepage.do_search("Account")
        searchpage = SearchPage(driver_)
        links_text = searchpage.get_links_text()
        assert 2 == len(links_text)
