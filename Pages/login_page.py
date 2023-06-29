import time

from selenium.common import TimeoutException

from locators.locators import LoginPageLocators, StartPageLocators
import random
from Pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from generator import generated_pass_number


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
        self.element_is_clickable(self.locators.BUTTON_EXIT)
        return self.driver.current_url


class StartPage(BasePage):
    locators = StartPageLocators()

    def add_visitors(self):
        last_name = 'Autotest'
        first_name = 'Test'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.VISITORS).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        text_id = self.element_is_visible(self.locators.TEXT_ID).text
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.SAVE_PERSON).click()
        return text_id

    def del_visitors(self):
        last_name = 'Autotest '
        first_name = 'Test'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.VISITORS).click()
        self.element_is_visible(self.locators.FIND_VISITORS).send_keys(last_name + first_name[0])
        self.elements_are_present(self.locators.FIND_CHECKBOX)[1].click()
        self.element_is_clickable(self.locators.BUTTON_DEL).click()
        self.element_is_clickable(self.locators.BUTTON_OK).click()
        return last_name, first_name

    def add_access_group(self):
        name_access_group = 'Футбол'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_clickable(self.locators.ACCESS_GROUP).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.NAME_ACCESS_GROUP).send_keys(name_access_group)
        self.element_is_visible(self.locators.SAVE_APPROVE).click()
        return name_access_group

    def add_my_application(self, number):
        last_name = 'Autotest '
        name_access_group = 'Авто'
        first_name = 'Test'
        fi_name = last_name + first_name
        self.element_is_clickable(self.locators.MY_APPLICATION).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        mess = self.switch_to_pass(number)
        if mess == "Success":
            self.element_is_visible(self.locators.INPUT_WORKER).send_keys(fi_name)
        else:
            self.element_is_visible(self.locators.INPUT_VISITOR).send_keys(fi_name)
        lists = self.elements_are_visible(self.locators.VISITORS_BUTTON)
        lists[1].click()
        self.element_is_visible(self.locators.ACCESS_GROUP_IN_MY_APP).send_keys(name_access_group)
        self.element_is_visible(self.locators.INPUT_ACCESS_GROUP_IN_MY_APP).click()
        self.element_is_visible(self.locators.BUTTON_IN_PROCESSING).click()
        self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()

    def del_my_application(self):
        last_name = 'Autotest'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.MY_APPLICATION).click()
        self.element_is_visible(self.locators.FIND_APPLICATION).send_keys(last_name)
        self.elements_are_present(self.locators.CHECKBOX_APPLICATION)[1].click()
        self.element_is_clickable(self.locators.DEL_APPLICATION).click()
        self.element_is_clickable(self.locators.BUTTON_OK).click()

    def open_incoming(self):
        # self.element_is_visible(self.locators.MENU).click()  # закомментить при необходимости
        self.element_is_visible(self.locators.INCOMING).click()
        self.elements_are_visible(self.locators.FIRST_STRING_IN_TABLE)[0].click()

    def agreement_application(self):
        self.element_is_visible(self.locators.AGREEMENT_BUTTON).click()
        # number_pass = generated_pass_number()  # сделать рандомную генерацию
        # print(number_pass)

    def issue_pass(self):
        txt_1 = self.element_is_visible(self.locators.STATUS_AGREEMENT).text
        page_source = self.driver.page_source
        if "Шаблон согласия" in page_source:
            self.element_is_visible(self.locators.BUTTON_OK).click()
        return txt_1

    def signing_receiving_pass(self, txt):
        if txt == 'Гостевой':
            self.element_is_clickable(self.locators.CHECK_BOX_APPROVE).click()
            self.element_is_visible(self.locators.SAVE_APPROVE).click()
        number_pass = random.randint(0, 100000)
        self.element_is_visible(self.locators.INPUT_NUMBER_PASS).send_keys(number_pass)
        self.element_is_visible(self.locators.BUTTON_OK).click()
        txt_3 = self.element_is_visible(self.locators.STATUS_AGREEMENT).text
        txt_2 = self.parser_status(txt_3)
        self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()
        # статусы Согласуется - разрешено - обработано
        return txt_2

    def reject_application(self):
        self.element_is_visible(self.locators.REJECT_BUTTON).click()

    def annul_application(self):
        self.element_is_visible(self.locators.ANNUL_BUTTON).click()

    def withdraw_pass(self):
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
        # self.element_is_visible(self.locators.MENU).click() #- если меню закрыто - раскомментить
        self.element_is_visible(self.locators.MY_APPLICATION_STATUS).click()
        self.elements_are_visible(self.locators.FIRST_STRING_IN_TABLE)[0].click()
        txt_2 = self.parser_status(self.element_is_visible(self.locators.STATUS_AGREEMENT).text)
        return txt_2

    def parser_status(self, txt):
        text = txt.split('[', 1)[1].split(']')[0]
        return text

    def add_employee(self):
        last_name = 'Autotest'
        first_name = 'Test'
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
        last_name = 'Autotest '
        first_name = 'Test'
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
        self.element_is_visible(self.locators.BUTTON_OK).click()

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
        self.element_is_visible(self.locators.BUTTON_OK).click()
        time.sleep(0.1)
        self.element_is_visible(self.locators.BUTTON_OK).click()
        window_operator = self.driver.window_handles[1]
        self.driver.switch_to.window(window_operator)
        return self.driver.current_url

    def open_menu(self):
        self.element_is_visible(self.locators.MENU).click()

    def switch_to_pass(self, number):
        pass_options = {
            'Постоянный': self.locators.BUTTON_CONST_PASS,
            'Временный': self.locators.BUTTON_TEMPORARY_PASS
        }

        if number in pass_options:
            self.element_is_visible(self.locators.BUTTON_PASS).click()
            self.element_is_visible(pass_options[number]).click()
            return "Success"

    def del_operator(self):
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_clickable(self.locators.MENU_STAFF).click()
        last_name = 'Autotest'
        self.element_is_visible(self.locators.FIND_APPLICATION).send_keys(last_name)
        checkbox_button = self.elements_are_present(self.locators.FIND_CHECKBOX)
        checkbox_button[1].click()
        self.element_is_clickable(self.locators.BUTTON_DEL).click()
        self.element_is_clickable(self.locators.BUTTON_OK).click()

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

    def parser_id(self, txt):
        return ''.join(i for i in txt if i.isdigit())

    # TODO - Работает. Есть три недоработки.
    # TODO - 1: Checkbox плохо распознается. Приходится обрабатывать исключение.
    # TODO - 2: Из-за одинаковых элементов выскакивает ошибка наложения. Работает также через обработку исключения.
    # TODO - 3: Из-за того, что поиск не работает по названию и может меняться ID невозможно выбрать то, что нам надо. Обрабатываем только первую строку.
    def fill_credentials(self, login, pas, url_skd):
        self.element_is_visible(self.locators.LOG).clear()
        self.element_is_visible(self.locators.LOG).send_keys(login)
        self.element_is_visible(self.locators.PASSWORD_OPERATOR).clear()
        self.element_is_visible(self.locators.PASSWORD_OPERATOR).send_keys(pas)
        self.element_is_visible(self.locators.INPUT_URL).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.INPUT_URL).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.INPUT_URL).send_keys(url_skd)

    def configure_integration(self, url_web, port, name, base_url, queue):
        self.element_is_visible(self.locators.CHECKBOX_INTEGRATION).click()
        self.configure_rabbitmq_lyrix(url_web, queue)
        self.element_is_visible(self.locators.INPUT_URL_RABBIT).clear()
        self.element_is_visible(self.locators.INPUT_URL_RABBIT).send_keys(base_url)
        self.element_is_visible(self.locators.INPUT_PORT).clear()
        self.element_is_visible(self.locators.INPUT_PORT).send_keys(port)
        self.element_is_visible(self.locators.INPUT_NAME).clear()
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.PASSWORD_OPERATOR).clear()
        self.element_is_visible(self.locators.PASSWORD_OPERATOR).send_keys(name)
        self.element_is_visible(self.locators.ACTIVE_BUTTON).click()
        self.element_is_clickable(self.locators.BUTTON_OK).click()
        time.sleep(0.1)
        self.element_is_clickable(self.locators.BUTTON_OK).click()
        try:
            self.elements_are_visible(self.locators.BUTTON_CANCEL, timeout=0.5)[2].click()
        except IndexError:
            self.elements_are_visible(self.locators.BUTTON_CANCEL)[2].click()
        self.element_is_visible(self.locators.SAVE_APPROVE).click()
        if 'Активация соединения' in self.driver.page_source:
            self.element_is_clickable(self.locators.BUTTON_OK).click()

    def configure_rabbitmq_lyrix(self, url_web, queue):
        try:
            input_con = self.element_is_visible(self.locators.INPUT_WEB_SERVER, timeout=0.1)
        except TimeoutException:
            self.element_is_visible(self.locators.CHECKBOX_INTEGRATION).click()
            input_con = self.element_is_visible(self.locators.INPUT_WEB_SERVER)
        input_con.send_keys(Keys.CONTROL + 'a')
        input_con.send_keys(Keys.DELETE)
        input_con.send_keys(url_web)
        self.element_is_visible(self.locators.INPUT_QUEUE).clear()
        self.element_is_visible(self.locators.INPUT_QUEUE).send_keys(queue)

    def integration_lyrix(self):
        url_skd = "http://192.168.2.166:1234/AxisWebApp/services/CardlibIntegrationService2Port?wsdl"
        login, pas, name, port, queue = '1', '1', 'test', 5672, 'PassOfficeQueue'
        url_web = 'http://192.168.2.166:8089'
        base_url = url_web.split(':')[0] + '://' + url_web.split('//')[1].split(':')[0]
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.MENU_INTEGRATION).click()
        # TODO - работает только когда LyriX первый
        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()
        self.fill_credentials(login, pas, url_skd)
        self.elements_are_visible(self.locators.EVENT)[1].click()
        self.configure_integration(url_web, port, name, base_url, queue)
        return self.element_is_visible(self.locators.BUTTON_CHECK).text

    def integration_APACS(self):
        url_skd = "http://192.168.2.166:1234/AxisWebApp/services/CardlibIntegrationService2Port?wsdl"
        login, pas, name, port, queue = '1', '1', 'test', 5672, 'PassOfficeQueue'
        url_web = 'http://192.168.2.166:8089'
        base_url = url_web.split(':')[0] + '://' + url_web.split('//')[1].split(':')[0]
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.MENU_INTEGRATION).click()
        # TODO - работает только когда APACS первый
        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()
        self.fill_credentials(login, pas, url_skd)
        self.elements_are_visible(self.locators.EVENT)[1].click()
        self.configure_integration(url_web, port, name, base_url, queue)
        return '✓'

    def switch_integration(self, name):
        SKD = {
            'LyriX': self.integration_lyrix,
            'APACS': self.integration_APACS
        }

        if name in SKD:
            integration_function = SKD[name]
            integration_function()
