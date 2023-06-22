import time

from Pages.login_page import LoginPage



def test_login_form(driver):
    login_page = LoginPage(driver, 'google.com')
    login_page.open()
    time.sleep(3)