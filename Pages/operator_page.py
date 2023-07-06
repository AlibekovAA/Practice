from locators.locators import AllLocators
from Pages.base_page import BasePage
from selenium.common import StaleElementReferenceException


class OperatorPage(BasePage):
    locators = AllLocators()

    def add_operator(self):
        last_name = 'Autotest'
        first_name = 'Test'
        # self.element_is_visible(self.locators.MENU).click() - раскомментить, если меню закрыто
        self.element_is_present(self.locators.operators.OPERATORS).click()
        self.element_is_visible(self.locators.visitors.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.operators.BUTTON_INPUT).send_keys(last_name + ' ' + first_name)
        listop = self.elements_are_visible(self.locators.operators.OPERATOR_BUTTON)
        listop[1].click()
        login = 'operator'
        password = 'Operator23.08'
        self.element_is_visible(self.locators.operators.LOGIN_OPERATOR).send_keys(login)
        self.element_is_visible(self.locators.operators.PASSWORD_OPERATOR).send_keys(password)
        self.element_is_visible(self.locators.operators.REPLY_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.operators.CHECK_BOX_OPERATOR).click()
        self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
        self.element_is_visible(self.locators.base.BUTTON_OK).click()
        return last_name

    def del_operator(self, name):
        self.element_is_visible(self.locators.login_page.MENU).click()
        if name == 'Сотрудники':
            self.element_is_clickable(self.locators.employee.MENU_EMPLOYEE).click()
        else:
            self.element_is_clickable(self.locators.operators.MENU_STAFF).click()
        last_name = 'Autotest '
        firs_name = 'Test'
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).clear()
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(last_name)
        self.elements_are_present(self.locators.visitors.FIND_CHECKBOX)[1].click()
        self.element_is_clickable(self.locators.visitors.BUTTON_DEL).click()
        self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        try:
            self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        except StaleElementReferenceException:
            self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        return last_name, firs_name

    def open_new_url(self):
        self.driver.switch_to.new_window()
        self.driver.get('http://localhost/auth/login')
        login = 'operator'
        password = 'Operator23.08'
        self.element_is_visible(self.locators.login_page.LOGIN).send_keys(login)
        self.element_is_visible(self.locators.login_page.PASS).send_keys(password)
        self.element_is_visible(self.locators.login_page.BUTTON_LOGIN).click()
        self.element_is_clickable(self.locators.login_page.BUTTON_ADMIN)
        return self.driver.current_url

    def active_off(self, last_name):
        window_admin = self.driver.window_handles[0]
        self.driver.switch_to.window(window_admin)
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(last_name)
        self.element_is_visible(self.locators.base.BUTTON_RESTART).click()
        self.element_is_clickable(self.locators.incoming.FIRST_STRING_IN_TABLE).click()
        self.element_is_visible(self.locators.operators.CHECK_BOX_OPERATOR).click()
        self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
        self.element_is_visible(self.locators.base.BUTTON_OK).click()
        try:
            self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        except StaleElementReferenceException:
            self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        window_operator = self.driver.window_handles[1]
        self.driver.switch_to.window(window_operator)
        self.elements_are_present(self.locators.integration_settings.CHECKBOX_AD_LOGIN)
        return self.driver.current_url
