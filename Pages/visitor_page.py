from locators.locators import AllLocators
from Pages.base_page import BasePage


class VisitorsPage(BasePage):
    locators = AllLocators()

    def add_visitors(self):
        last_name = 'Autotest'
        first_name = 'Test'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.visitors.VISITORS).click()
        self.element_is_visible(self.locators.visitors.BUTTON_ADD_VISITORS).click()
        text_id = self.element_is_visible(self.locators.visitors.TEXT_ID).text
        self.element_is_visible(self.locators.visitors.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.visitors.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.visitors.SAVE_PERSON).click()
        return text_id

    def del_visitors(self):
        last_name = 'Autotest'
        first_name = 'Test'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.visitors.VISITORS).click()
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(last_name + ' ' + first_name[0])
        self.elements_are_present(self.locators.visitors.FIND_CHECKBOX)[1].click()
        self.element_is_clickable(self.locators.visitors.BUTTON_DEL).click()
        self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        return last_name, first_name

    def add_employee(self):
        last_name = 'Autotest'
        first_name = 'Test'
        mail = 'AutotestT12@mail.ru'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.employee.MENU_EMPLOYEE).click()
        self.element_is_visible(self.locators.visitors.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.visitors.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.visitors.FIRST_NAME).send_keys(first_name)
        self.element_is_present(self.locators.employee.CONTACT_INFORM).click()
        self.element_is_visible(self.locators.employee.EMAIL_SEARCH).send_keys(mail)
        self.element_is_visible(self.locators.visitors.SAVE_PERSON).click()
