from locators.locators import AllLocators
from Pages.supporting_page import SupportingPage
from selenium.webdriver.common.keys import Keys
from selenium.common import TimeoutException, StaleElementReferenceException
import time


class IntegrationPage(SupportingPage):
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
            try:
                self.element_is_clickable(self.locators.base.BUTTON_OK).click()
            except StaleElementReferenceException:
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
        # Тут надо выбрать откуда будем импортировать. Изначально все доступные будут активны и нам нужно отключить ненужные
        self.element_is_clickable(self.locators.integration_settings.CHECKBOX_ACTIVITY_LyriX).click()
        self.element_is_present(self.locators.integration_settings.INPUT_CONTAINER).send_keys('Alexey')
        lists = self.elements_are_visible(self.locators.visitors.VISITORS_BUTTON)
        lists[0].click()
        self.element_is_clickable(self.locators.integration_settings.BUTTON_IMPORT).click()
        self.elements_are_present(self.locators.base.FIND_POISK)[0].clear()
        txt = self.element_is_visible(self.locators.integration_settings.SUCCESS_IMPORT).text
        self.element_is_visible(self.locators.base.BUTTON_RESTART).click()
        self.element_is_visible(self.locators.integration_settings.NEW_FIRST_STRING_IN_TABLE).click()
        text_id = self.element_is_visible(self.locators.visitors.TEXT_ID).text
        self.element_is_visible(self.locators.base.SAVE_APPROVE).click()
        return txt, text_id

    def check_operator(self, id_person):
        self.elements_are_present(self.locators.base.FIND_POISK)[0].clear()
        self.elements_are_present(self.locators.base.FIND_POISK)[0].send_keys('Операторы')
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys('Test')
        status_1 = not self.check_visitor_id(id_person)
        self.elements_are_present(self.locators.base.FIND_POISK)[0].clear()
        self.elements_are_present(self.locators.base.FIND_POISK)[0].send_keys('Сотрудники')
        self.element_is_visible(self.locators.visitors.FIND_VISITORS).send_keys('Test')
        status_2 = self.check_visitor_id(id_person)
        return status_1, status_2

    def login_AD(self):
        login, password = 'Autotest@test.local', 'Passw0rd_2'
        self.element_is_clickable(self.locators.login_page.BUTTON_ADMIN)
        self.elements_are_present(self.locators.login_page.BUTTON_EXIT)[2].click()
        self.elements_are_present(self.locators.integration_settings.CHECKBOX_INTEGRATION)[0].click()
        self.element_is_visible(self.locators.login_page.LOGIN).send_keys(login)
        self.element_is_visible(self.locators.login_page.PASS).send_keys(password)
        self.element_is_visible(self.locators.login_page.BUTTON_LOGIN).click()
