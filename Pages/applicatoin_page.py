from locators.locators import AllLocators
from Pages.supporting_page import SupportingPage
import random


class ApplicationPage(SupportingPage):
    locators = AllLocators()

    def add_my_application(self, number):
        last_name = 'Autotest '
        name_access_group = 'Авто'
        first_name = 'Test'
        fi_name = last_name + first_name
        self.element_is_clickable(self.locators.application.MY_APPLICATION).click()
        self.element_is_visible(self.locators.visitors.BUTTON_ADD_VISITORS).click()
        mess = self.switch_to_pass(number)
        if mess == "Success":
            self.element_is_visible(self.locators.employee.INPUT_WORKER).send_keys(fi_name)
        else:
            self.element_is_visible(self.locators.visitors.INPUT_VISITOR).send_keys(fi_name)
        lists = self.elements_are_visible(self.locators.visitors.VISITORS_BUTTON)
        lists[1].click()
        self.element_is_visible(self.locators.access_group.ACCESS_GROUP_IN_MY_APP).send_keys(name_access_group)
        self.element_is_visible(self.locators.access_group.INPUT_ACCESS_GROUP_IN_MY_APP).click()
        self.element_is_visible(self.locators.application.BUTTON_IN_PROCESSING).click()
        self.element_is_visible(self.locators.active_pass.CLOSE_WINDOW_ACTIVATE_PASS).click()

    def del_my_application(self):
        last_name = 'Autotest'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.application.MY_APPLICATION).click()
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(last_name)
        self.elements_are_present(self.locators.visitors.FIND_CHECKBOX)[1].click()
        self.element_is_clickable(self.locators.application.DEL_APPLICATION).click()
        self.element_is_clickable(self.locators.base.BUTTON_OK).click()

    def open_incoming(self):
        # self.element_is_visible(self.locators.MENU).click()  # закомментируй при необходимости
        self.element_is_visible(self.locators.incoming.INCOMING).click()
        self.element_is_visible(self.locators.incoming.FIRST_STRING_IN_TABLE).click()

    def agreement_application(self):
        self.element_is_visible(self.locators.application.AGREEMENT_BUTTON).click()
        # number_pass = generated_pass_number()  # сделать рандомную генерацию
        # print(number_pass)

    def issue_pass(self):
        txt_1 = self.element_is_visible(self.locators.application.STATUS_AGREEMENT).text
        page_source = self.driver.page_source
        if "Шаблон согласия" in page_source:
            self.element_is_visible(self.locators.base.BUTTON_OK).click()
        return txt_1

    def signing_receiving_pass(self, txt):
        if txt == 'Гостевой':
            self.element_is_clickable(self.locators.application.CHECK_BOX_APPROVE).click()
            self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
        number_pass = random.randint(0, 100000)
        self.element_is_visible(self.locators.application.INPUT_NUMBER_PASS).send_keys(number_pass)
        self.element_is_visible(self.locators.base.BUTTON_OK).click()
        txt_3 = self.element_is_visible(self.locators.application.STATUS_AGREEMENT).text
        txt_2 = self.parser_status(txt_3)
        self.element_is_visible(self.locators.active_pass.CLOSE_WINDOW_ACTIVATE_PASS).click()
        # статусы Согласуется - разрешено - обработано
        return txt_2

    def reject_application(self):
        self.element_is_visible(self.locators.application.REJECT_BUTTON).click()

    def annul_application(self):
        self.element_is_visible(self.locators.application.ANNUL_BUTTON).click()

    def withdraw_pass(self):
        self.element_is_visible(self.locators.active_pass.BUTTON_ACTIVE_PASS).click()

        self.element_is_visible(self.locators.active_pass.BUTTON_ACTIVE_PASS).click()

        self.element_is_visible(self.locators.active_pass.BUTTON_WITHDROW).click()

        self.element_is_visible(self.locators.active_pass.BUTTON_OK_PATTERN_APPROVE).click()
        self.element_is_visible(self.locators.active_pass.CLOSE_WINDOW_ACTIVATE_PASS).click()

    def copy_application(self):
        # открыть заявку, которую копировать
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.application.MY_APPLICATION).click()
        self.element_is_visible(self.locators.incoming.FIRST_STRING_IN_TABLE).click()
        # copy
        self.element_is_visible(self.locators.application.COPY_APPLICATION_BUTTON).click()
        self.element_is_visible(self.locators.application.BUTTON_IN_PROCESSING).click()
        self.element_is_visible(self.locators.active_pass.CLOSE_WINDOW_ACTIVATE_PASS).click()

        # перенести в другое

    def add_another_pass(self):
        self.element_is_visible(self.locators.application.AGREEMENT_BUTTON).click()
        self.element_is_visible(self.locators.application.THREE_POINT_AGREEMENT).click()
        self.element_is_visible(self.locators.application.BUTTON_ISSUE_ANOTHER_PASS).click()
        self.element_is_visible(self.locators.application.BUTTON_YES_PO).click()

    def check_status(self):
        # self.element_is_visible(self.locators.MENU).click() #- если меню закрыто - раскомментить
        self.element_is_visible(self.locators.application.MY_APPLICATION_STATUS).click()
        self.element_is_visible(self.locators.incoming.FIRST_STRING_IN_TABLE).click()
        txt_2 = self.parser_status(self.element_is_visible(self.locators.application.STATUS_AGREEMENT).text)
        return txt_2

    def switch_to_pass(self, number):
        pass_options = {
            'Постоянный': self.locators.application.BUTTON_CONST_PASS,
            'Временный': self.locators.application.BUTTON_TEMPORARY_PASS
        }

        if number in pass_options:
            self.element_is_visible(self.locators.application.BUTTON_PASS).click()
            self.element_is_visible(pass_options[number]).click()
            return "Success"
