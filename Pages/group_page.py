from locators.locators import AllLocators
from Pages.base_page import BasePage


class GroupPage(BasePage):
    locators = AllLocators()

    def add_access_group(self):
        name_access_group = 'Авто'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_clickable(self.locators.access_group.ACCESS_GROUP).click()
        self.element_is_visible(self.locators.visitors.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.access_group.NAME_ACCESS_GROUP).send_keys(name_access_group)
        self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
        return name_access_group

    def del_access_group(self):
        name_access_group = 'Авто'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_clickable(self.locators.access_group.ACCESS_GROUP).click()
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(name_access_group)
        self.elements_are_present(self.locators.visitors.FIND_CHECKBOX)[1].click()
        self.element_is_clickable(self.locators.visitors.BUTTON_DEL).click()
        self.element_is_clickable(self.locators.base.BUTTON_OK).click()
