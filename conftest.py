from selenium import webdriver
import pytest
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver_ = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com/index.html")
    return driver_

@pytest.fixture(scope="module")
def login(driver):
    homepage = HomePage(driver)
    homepage.click_signin_button()
    loginpage =  LoginPage(driver)
    loginpage.doLogin("username","password")
    return driver