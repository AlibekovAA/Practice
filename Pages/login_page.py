import time

from locators.locators import LoginPageLocators, StartPageLocators
import random
from Pages.base_page import BasePage
from generator import generated_pass_number
from test import parser_status


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def filing_login_pass(self):
        login = 'admin'
        password = 'admin'
        self.element_is_visible(self.locators.LOGIN).send_keys(login)
        self.element_is_visible(self.locators.PASS).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        return

    def check_login(self):
        button_exit = self.element_is_clickable(self.locators.BUTTON_EXIT)
        return self.driver.current_url


class StartPage(BasePage):
    locators = StartPageLocators()

    def add_visitors(self):
        txt = 'Посетители'
        last_name = 'Autotest'
        first_name = 'Test'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.VISITORS).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.SAVE_PERSON).click()
        page_source = self.driver.page_source
        if "Autotest T" in page_source:
            print("\nПользователь добавлен")
        else:
            print("\nНе удалось добавить пользователя")
        return last_name, first_name

    def del_visitors(self):
        last_name = 'Autotest'
        first_name = 'Test'
        fi_name = last_name + ' ' + first_name[0]
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.VISITORS).click()
        self.element_is_visible(self.locators.FIND_VISITORS).send_keys(fi_name)
        checkbox_button = self.elements_are_present(self.locators.FIND_CHECKBOX, timeout=10)
        checkbox_button[1].click()
        self.element_is_clickable(self.locators.BUTTON_DEL, timeout=10).click()
        self.element_is_clickable(self.locators.BUTTON_OK).click()
        return fi_name

    def add_access_group(self):
        name_access_group = 'Авто'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.ACCESS_GROUP).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.NAME_ACCESS_GROUP).send_keys(name_access_group)
        self.element_is_visible(self.locators.SAVE_AG).click()
        return name_access_group

    def add_my_application(self):
        last_name = 'Autotest '
        name_access_group = 'Авто'
        first_name = 'Test'
        fi_name = last_name + first_name
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_clickable(self.locators.MY_APPLICATION).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.INPUT_VISITOR).send_keys(fi_name)
        self.element_is_clickable(self.locators.VISITORS_BUTTON).click()
        self.element_is_visible(self.locators.ACCESS_GROUP_IN_MY_APP).send_keys(name_access_group)
        self.element_is_visible(self.locators.INPUT_ACCESS_GROUP_IN_MY_APP).click()
        self.element_is_visible(self.locators.BUTTON_IN_PROCESSING).click()
        self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()
        # element = self.element_is_visible(self.locators.BUTTON_DAWN_DROP).text
        # self.element_is_visible(self.locators.BUTTON_DAWN_DROP).click()  # .send_keys(last_name)
        # # print(f' Элемент - {element}') # пустое значение
        # self.element_is_visible(
        #     self.locators.INPUT_VISITORS).click()  # иногда падает тут - понять в чем плавающая ошибка, возможно дело в локаторе
        # # time.sleep(6)
        # self.element_is_visible(self.locators.ACCESS_GROUP_IN_MY_APP).send_keys(name_access_group)
        # # time.sleep(3)
        # self.element_is_visible(self.locators.INPUT_ACCESS_GROUP_IN_MY_APP).click()
        # self.element_is_visible(self.locators.BUTTON_IN_PROCESSING).click()
        # # time.sleep(3)
        # self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()

    def del_my_application(self):
        last_name = 'Autotest'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.MY_APPLICATION).click()
        self.element_is_visible(self.locators.FIND_APPLICATION).send_keys(last_name)
        checkbox_button = self.elements_are_present(self.locators.CHECKBOX_APPLICATION)
        checkbox_button[1].click()
        self.element_is_clickable(self.locators.DEL_APPLICATION).click()
        self.element_is_clickable(self.locators.APPLICATION_OK).click()

    def open_incoming(self):
        # self.element_is_visible(self.locators.MENU).click()  # закомментить при необходимости
        self.element_is_visible(self.locators.INCOMING).click()
        string_table = self.elements_are_visible(self.locators.FIRST_STRING_IN_TABLE)
        string_table[0].click()

    def agreement_application(self):
        self.element_is_visible(self.locators.AGREEMENT_BUTTON).click()
        # number_pass = generated_pass_number()  # сделать рандомную генерацию
        # print(number_pass)

    def issue_pass(self):
        txt_1 = self.element_is_visible(self.locators.STATUS_AGREEMENT).text
        # print(txt_1) # написать функцию которая парсит текст и находит слово в []
        # self.element_is_visible(self.locators.THREE_POINT_AGREEMENT).click()
        page_source = self.driver.page_source
        if "Шаблон согласия" in page_source:
            self.element_is_clickable(self.locators.BUTTON_ISSUE_PASS).click()
        return txt_1
        # ТЕПЕРЬ МЫ ТУТ УРАААА
        #  сделать проверку если есть окно - то делаем согласие - если нет то идем сразу на выдачу

    def signing_receiving_pass(self, txt_1):
        # if self.parser_status(txt_1) == "Согласуется":
        #     # # approve согласие на новом пользаке
        #     self.element_is_visible(self.locators.BUTTON_OK_PATTERN_APPROVE).click()
        #     # ТЕПЕРЬ МЫ ТУТ УРАААА
        #     time.sleep(5)
        self.element_is_clickable(self.locators.CHECK_BOX_APPROVE).click()
        self.element_is_visible(self.locators.SAVE_APPROVE).click()
        # # выдача пропуска
        # # сделать рандомный выбор HEX / DEC
        # time.sleep(5)
        number_pass = random.randint(0, 10000)
        self.element_is_visible(self.locators.INPUT_NUMBER_PASS).send_keys(number_pass)
        self.element_is_visible(self.locators.BUTTON_OK_NUMBER_PASS).click()
        txt_3 = self.element_is_visible(self.locators.STATUS_AGREEMENT).text
        txt_2 = parser_status(txt_3)  # По идее парсер уже можно перенести сюда из test.py. Пока импортировал
        self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()
        # статусы Согласуется - разрешено - обработано
        return txt_2

    def reject_application(self):
        self.element_is_visible(self.locators.REJECT_BUTTON).click()

    def annul_application(self):
        self.element_is_visible(self.locators.ANNUL_BUTTON).click()

    def withdraw_pass(self):
        # url = 'http://localhost/listedData/passDictionaryActive'
        # open(url)
        self.element_is_visible(self.locators.BUTTON_ACTIVE_PASS).click()

        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()

        self.element_is_visible(self.locators.BUTTON_WITHDROW).click()

        self.element_is_visible(self.locators.BUTTON_OK_PATTERN_APPROVE).click()
        self.element_is_visible(self.locators.CLOSE_WINDOW_ACTIVATE_PASS).click()

    def copy_application(self):
        # открыть заявку, которую копировать
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.MY_APPLICATION).click()
        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()
        # copy
        self.element_is_visible(self.locators.COPY_APPLICATION_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_IN_PROCESSING).click()
        self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()

        # перенести в другое

    def add_another_pass(self):
        self.element_is_visible(self.locators.AGREEMENT_BUTTON).click()
        self.element_is_visible(self.locators.THREE_POINT_AGREEMENT).click()
        self.element_is_visible(self.locators.BUTTON_ISSUE_ANOTHER_PASS).click()
        self.element_is_visible(self.locators.BUTTON_YES_PO).click()

    def check_status(self):
        # self.element_is_visible(self.locators.MENU).click() - если меню закрыто - раскомментить
        self.element_is_visible(self.locators.MY_APPLICATION_STATUS).click()
        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()
        txt_2 = parser_status(self.element_is_visible(self.locators.STATUS_AGREEMENT).text)
        return txt_2

    # def parser_status(txt):
    #     text = txt.split('[', 1)[1].split(']')[0]
    #     return text
    def add_employee(self):
        last_name = 'Testov'
        first_name = 'Testь'
        mail = 'AutotestT12@mail.ru'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.VISITORS).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_present(self.locators.ADD_INFORM).click()
        self.element_is_present(self.locators.DEL_CATEGORY).click()
        self.element_is_visible(self.locators.BUTTON_SEARCH).send_keys('Сотрудники')
        self.element_is_visible(self.locators.CATEGORY_BUTTON).click()
        self.element_is_present(self.locators.CONTACT_INFORM).click()
        self.element_is_visible(self.locators.EMAIL_SEARCH).send_keys(mail)
        self.element_is_visible(self.locators.SAVE_PERSON).click()

    def add_operator(self):
        last_name = 'Testov '
        first_name = 'Testь'
        # self.element_is_visible(self.locators.MENU).click() - раскомментить, если меню закрыто
        self.element_is_present(self.locators.OPERATORS).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.BUTTON_OPERATOR).send_keys(last_name + first_name)
        listop = self.elements_are_visible(self.locators.OPERATOR_BUTTON)
        listop[2].click()
        login = 'operator'
        password = 'Operator23.08'
        self.element_is_visible(self.locators.LOGIN_OPERATOR).send_keys(login)
        self.element_is_visible(self.locators.PASSWORD_OPERATOR).send_keys(password)
        self.element_is_visible(self.locators.REPLY_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.CHECK_BOX_OPERATOR).click()
        self.element_is_visible(self.locators.SAVE_APPROVE).click()
        self.element_is_clickable(self.locators.BUTTON_OK_NUMBER_PASS).click()

    def open_new_url(self):
        self.driver.switch_to.new_window()
        self.driver.get('http://localhost/auth/login')
        login = 'operator'
        password = 'Operator23.08'
        self.element_is_visible(self.locators.LOGIN).send_keys(login)
        self.element_is_visible(self.locators.PASS).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        self.element_is_visible(self.locators.BUTTON_TEXT)
        return self.driver.current_url


    def active_off(self):
        window_admin = self.driver.window_handles[0]
        self.driver.switch_to.window(window_admin)
        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()
        self.element_is_visible(self.locators.CHECK_BOX_OPERATOR).click()
        self.element_is_visible(self.locators.SAVE_APPROVE).click()
        self.element_is_visible(self.locators.BUTTON_OK_NUMBER_PASS).click()
        time.sleep(0.1) #TODO - слишком быстро прокликивает и не успевает увидеть второй раз кнопку ок.
        #TODO - по идее можно попробовать через крестик, но у меня возникли с этим проблемы
        self.element_is_visible(self.locators.BUTTON_OK).click()
        window_operator = self.driver.window_handles[1]
        self.driver.switch_to.window(window_operator)
        return self.driver.current_url


    def open_menu(self):
        self.element_is_visible(self.locators.MENU).click()
