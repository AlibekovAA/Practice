import time
import random
from selenium.common import TimeoutException
from locators.locators import AllLocators
from Pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


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
        last_name = 'Autotest '
        first_name = 'Test'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.visitors.VISITORS).click()
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(last_name + first_name[0])
        self.elements_are_present(self.locators.visitors.FIND_CHECKBOX)[1].click()
        self.element_is_clickable(self.locators.visitors.BUTTON_DEL).click()
        self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        return last_name, first_name

    def add_employee(self):
        last_name = 'Autotest'
        first_name = 'Test'
        mail = 'AutotestT12@mail.ru'
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.visitors.VISITORS).click()
        self.element_is_visible(self.locators.visitors.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.visitors.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.visitors.FIRST_NAME).send_keys(first_name)
        self.element_is_present(self.locators.visitors.ADD_INFORM).click()
        self.element_is_present(self.locators.visitors.DEL_CATEGORY).click()
        self.element_is_visible(self.locators.visitors.BUTTON_SEARCH).send_keys('Сотрудники')
        self.element_is_visible(self.locators.visitors.CATEGORY_BUTTON).click()
        self.element_is_present(self.locators.visitors.CONTACT_INFORM).click()
        self.element_is_visible(self.locators.visitors.EMAIL_SEARCH).send_keys(mail)
        self.element_is_visible(self.locators.visitors.SAVE_PERSON).click()


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


class ApplicationPage(BasePage, SupportingPage):
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
        last_name = 'Autotest'
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(last_name)
        self.elements_are_present(self.locators.visitors.FIND_CHECKBOX)[1].click()
        self.element_is_clickable(self.locators.visitors.BUTTON_DEL).click()
        self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        if name == 'Операторы':
            time.sleep(0.2)
            self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        return True

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
        time.sleep(0.1)
        self.element_is_clickable(self.locators.incoming.FIRST_STRING_IN_TABLE).click()
        self.element_is_visible(self.locators.operators.CHECK_BOX_OPERATOR).click()
        self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
        self.element_is_visible(self.locators.base.BUTTON_OK).click()
        time.sleep(0.1)
        self.element_is_visible(self.locators.base.BUTTON_OK).click()
        window_operator = self.driver.window_handles[1]
        self.driver.switch_to.window(window_operator)
        self.elements_are_present(self.locators.integration_settings.CHECKBOX_AD_LOGIN)
        return self.driver.current_url


class IntegrationPage(BasePage):
    locators = AllLocators()

    def fill_credentials(self, login, pas, url_skd):
        self.element_is_visible(self.locators.integration_settings.LOGIN_INTEGRATION).clear()
        self.element_is_visible(self.locators.integration_settings.LOGIN_INTEGRATION).send_keys(login)
        self.element_is_visible(self.locators.operators.PASSWORD_OPERATOR).clear()
        self.element_is_visible(self.locators.operators.PASSWORD_OPERATOR).send_keys(pas)
        self.element_is_visible(self.locators.integration_settings.INPUT_URL).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.integration_settings.INPUT_URL).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.integration_settings.INPUT_URL).send_keys(url_skd)

    def configure_integration(self, url_web, port, name, base_url, queue, name_SKD):
        check_box = self.elements_are_present(self.locators.integration_settings.CHECKBOX_INTEGRATION)
        status_1 = check_box[1].get_attribute('aria-checked')
        status_2 = check_box[2].get_attribute('aria-checked')
        if status_1 and status_2 == 'false':
            check_box[2].click()
        if name_SKD == "LyriX":
            self.configure_rabbitmq_lyrix(url_web, queue, base_url)
        elif name_SKD == "APACS":
            self.configure_rabbitmq_APACS(base_url)
        self.element_is_visible(self.locators.integration_settings.INPUT_PORT).clear()
        self.element_is_visible(self.locators.integration_settings.INPUT_PORT).send_keys(port)
        self.element_is_visible(self.locators.integration_settings.INPUT_NAME).clear()
        self.element_is_visible(self.locators.integration_settings.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.operators.PASSWORD_OPERATOR).clear()
        self.element_is_visible(self.locators.operators.PASSWORD_OPERATOR).send_keys(name)
        if name_SKD == "LyriX":  # Удаление очереди на деактивацию
            check_box = self.elements_are_present(self.locators.integration_settings.CHECKBOX_INTEGRATION)
            if check_box[3].get_attribute('aria-checked') == 'false':
                check_box[3].click()
        self.confirm_stage(name_SKD)

    def confirm_stage(self, name_SKD):
        active_button = self.element_is_visible(self.locators.integration_settings.ACTIVE_BUTTON)
        active_button.click()
        status = active_button.get_attribute('innerHTML')
        self.element_is_clickable(self.locators.base.BUTTON_OK).click()
        if name_SKD == 'Active Directory' and status == 'Активировать':
            self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
            try:  # всплывающее окно об успешности интеграции
                window_element = self.element_is_visible(self.locators.integration_settings.WINDOW_SUCCESS)
                if window_element.is_displayed():
                    self.element_is_clickable(self.locators.base.BUTTON_OK).click()
            except TimeoutException:
                pass
        else:
            time.sleep(0.2)
            self.element_is_clickable(self.locators.base.BUTTON_OK).click()
            cancel_button = self.elements_are_present(self.locators.integration_settings.BUTTON_CANCEL)
            self.driver.execute_script("arguments[0].click();", cancel_button[1])
            self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
            try:  # всплывающее окно об успешности интеграции
                window_element = self.element_is_visible(self.locators.integration_settings.WINDOW_SUCCESS)
                if window_element.is_displayed():
                    self.element_is_clickable(self.locators.base.BUTTON_OK).click()
            except TimeoutException:
                pass

    def configure_rabbitmq_lyrix(self, url_web, queue, base_url):
        self.element_is_visible(self.locators.integration_settings.INPUT_WEB_SERVER).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.integration_settings.INPUT_WEB_SERVER).send_keys(Keys.DELETE)
        self.element_is_visible(self.locators.integration_settings.INPUT_WEB_SERVER).send_keys(url_web)
        self.element_is_visible(self.locators.integration_settings.INPUT_URL_RABBIT).clear()
        self.element_is_visible(self.locators.integration_settings.INPUT_URL_RABBIT).send_keys(base_url)
        self.element_is_visible(self.locators.integration_settings.INPUT_QUEUE).clear()
        self.element_is_visible(self.locators.integration_settings.INPUT_QUEUE).send_keys(queue)

    def integration_lyrix(self, ID):
        url_skd = "http://192.168.2.166:1234/AxisWebApp/services/CardlibIntegrationService2Port?wsdl"
        login, pas, name, port, queue = '1', '1', 'test', 5672, 'PassOfficeQueue'
        url_web = 'http://192.168.2.166:8089'
        base_url = url_web.split(':')[0] + '://' + url_web.split('//')[1].split(':')[0]
        self.open_menu_integration(ID)
        self.fill_credentials(login, pas, url_skd)
        self.elements_are_visible(self.locators.integration_settings.NOTIFY)[1].click()
        self.configure_integration(url_web, port, name, base_url, queue, name_SKD="LyriX")
        return self.element_is_visible(self.locators.integration_settings.CONNECT_CHECK).text

    def configure_rabbitmq_APACS(self, base_url):
        self.element_is_visible(self.locators.integration_settings.INPUT_URL_RABBIT).clear()
        self.element_is_visible(self.locators.integration_settings.INPUT_URL_RABBIT).send_keys(base_url)

    def integration_APACS(self, ID):
        url_skd = "http://192.168.2.166:1234/AxisWebApp/services/CardlibIntegrationService2Port?wsdl"
        login, pas, name, port, queue = '1', '1', 'test', 5672, 'PassOfficeQueue'
        url_web = 'http://192.168.2.166:8089'
        base_url = url_web.split(':')[0] + '://' + url_web.split('//')[1].split(':')[0]
        self.open_menu_integration(ID)
        self.fill_credentials(login, pas, url_skd)
        self.elements_are_visible(self.locators.integration_settings.NOTIFY)[1].click()
        self.configure_integration(url_web, port, name, base_url, queue, name_SKD="APACS")
        return self.element_is_visible(self.locators.integration_settings.CONNECT_CHECK).text

    def switch_integration(self, name):
        SKD = {
            'LyriX': (self.integration_lyrix, 43),
            'APACS': (self.integration_APACS, 42),
            'Active Directory': (self.integration_AD, 49)
        }

        if name in SKD:
            integration_function, ID = SKD[name]
            return integration_function(ID=ID)

    def integration_AD(self, ID):
        url_skd = "ldap://192.168.2.158"
        login, pas, base = 'test\\administrator', 'Passw0rd', 'dc=test,dc=local'
        self.open_menu_integration(ID)
        self.fill_credentials(login, pas, url_skd)
        self.element_is_visible(self.locators.integration_settings.INPUT_BASE).clear()
        self.element_is_visible(self.locators.integration_settings.INPUT_BASE).send_keys(base)
        check_box = self.elements_are_present(self.locators.integration_settings.CHECKBOX_INTEGRATION)
        if check_box[2].get_attribute('aria-checked') == 'false':
            check_box[2].click()
        self.confirm_stage(name_SKD='Active Directory')
        return self.element_is_visible(self.locators.integration_settings.CONNECT_CHECK).text

    def open_menu_integration(self, ID):
        self.element_is_visible(self.locators.login_page.MENU).click()
        self.element_is_visible(self.locators.integration_settings.MENU_INTEGRATION).click()
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).clear()
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys(ID)
        time.sleep(0.3)
        self.element_is_visible(self.locators.incoming.FIRST_STRING_IN_TABLE).click()

    def synchron(self):
        self.elements_are_present(self.locators.base.FIND_POISK)[0].clear()
        self.elements_are_present(self.locators.base.FIND_POISK)[0].send_keys('Люди')
        self.element_is_visible(self.locators.integration_settings.BUTTON_SYNCHRON).click()
        # TODO - тут надо выбрать откуда будем импортировать. Изначально все доступные будут активны и нам нужно отключить ненужные
        self.element_is_clickable(self.locators.integration_settings.CHECKBOX_ACTIVITY_LyriX).click()
        self.element_is_present(self.locators.integration_settings.INPUT_CONTAINER).send_keys('Alexey')
        lists = self.elements_are_visible(self.locators.visitors.VISITORS_BUTTON)
        lists[0].click()
        self.element_is_clickable(self.locators.integration_settings.BUTTON_IMPORT).click()
        self.elements_are_present(self.locators.base.FIND_POISK)[0].clear()
        return self.element_is_visible(self.locators.integration_settings.SUCCESS_IMPORT).text

    def check_operator(self):
        status_1, status_2 = True, False
        self.elements_are_present(self.locators.base.FIND_POISK)[0].clear()
        self.elements_are_present(self.locators.base.FIND_POISK)[0].send_keys('Операторы')
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys('Test')
        if 'Test A.' in self.driver.page_source:
            status_1 = False
        self.elements_are_present(self.locators.base.FIND_POISK)[0].clear()
        self.elements_are_present(self.locators.base.FIND_POISK)[0].send_keys('Сотрудники')
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys('Test')
        if 'Test A.' in self.driver.page_source:
            status_2 = True
        return status_1, status_2

    def login_AD(self):
        login, password = 'Autotest@test.local', 'Passw0rd_2'
        self.element_is_clickable(self.locators.login_page.BUTTON_ADMIN)
        self.elements_are_present(self.locators.login_page.BUTTON_EXIT)[2].click()
        self.elements_are_present(self.locators.integration_settings.CHECKBOX_INTEGRATION)[0].click()
        self.element_is_visible(self.locators.login_page.LOGIN).send_keys(login)
        self.element_is_visible(self.locators.login_page.PASS).send_keys(password)
        self.element_is_visible(self.locators.login_page.BUTTON_LOGIN).click()
