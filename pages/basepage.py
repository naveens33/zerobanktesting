from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def enterText(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)

    def find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def get_options(self,locator):
        dropdown = Select(self.driver.find_element(*locator))
        return dropdown.options

    def wait_for_element(self,locator,condition):
        wait = WebDriverWait(self.driver, 5)
        if condition == "visibility":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "clickable":
            return wait.until(EC.element_to_be_clickable(locator))
        else:
            print("Invalid condition")
            return None