from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class SearchPage(BasePage):
    result_links =  By.XPATH,"//a[starts-with(text(),'Zero - ')]"

    def get_links_text(self):
        elements =  self.find_elements(self.result_links)
        li = []
        for element in elements:
            li.append(element.text)
        return li