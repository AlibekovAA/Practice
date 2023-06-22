

from locators.locators import StartPageLocators


from Pages.base_page import BasePage


class StartPage(BasePage):
    locators = StartPageLocators()

    def open_menu(self):
        self.element_is_visible(self.locators.MENU).click()


