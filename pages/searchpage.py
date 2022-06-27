from selenium.webdriver.common.by import By
from base.basepage import BasePage


class SearchPage(BasePage):
    links = By.XPATH,'//a[starts-with(text(),"Zero -")]'

    def get_search_result(self):
        elements = self._find_elements(self.links)
        return [element.text for element in elements]