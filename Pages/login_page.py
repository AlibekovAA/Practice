from locators.locators import AllLocators
from Pages.base_page import BasePage


class LoginPage(BasePage):
    locators = AllLocators()

    def filing_login_pass(self):
        login = 'admin'
        password = 'admin'
        self.element_is_visible(self.locators.login_page.LOGIN).send_keys(login)
        self.element_is_visible(self.locators.login_page.PASS).send_keys(password)
        self.element_is_visible(self.locators.login_page.BUTTON_LOGIN).click()
        return

    def check_login(self):
        self.element_is_clickable(self.locators.login_page.BUTTON_ADMIN)
        return self.driver.current_url
