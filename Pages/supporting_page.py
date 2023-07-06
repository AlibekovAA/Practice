from locators.locators import AllLocators
from Pages.base_page import BasePage


class SupportingPage(BasePage):
    locators = AllLocators()

    def open_only_menu(self):
        self.element_is_visible(self.locators.login_page.MENU).click()

    def check_visitor_fio(self, last_name, first_name):
        page_source = self.driver.page_source
        if f"{last_name} {first_name[0]}" in page_source:
            return True
        else:
            return False

    def check_visitor_id(self, txt):
        page_source = self.driver.page_source
        id_visitor = self.parser_id(txt)
        if id_visitor in page_source:
            return True
        else:
            return False

    @staticmethod
    def parser_id(txt):
        return ''.join(i for i in txt if i.isdigit())

    @staticmethod
    def parser_status(txt):
        text = txt.split('[', 1)[1].split(']')[0]
        return text

