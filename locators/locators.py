from selenium.webdriver.common.by import By


class AllLocators:
    def __init__(self):
        self.login_page = LoginPageLocators()
        self.incoming = IncomingLocators()
        self.access_group = AccessGroupLocators()
        self.visitors = VisitorsLocators()
        self.employee = EmployeeLocators()
        self.base = BaseLocators()
        self.operators = OperatorsLocator()
        self.integration_settings = IntegrationSettingsLocators()
        self.active_pass = ActivePasseLocators()
        self.application = ApplicationLocators()


class LoginPageLocators:
    LOGIN = (By.CSS_SELECTOR, "input[id='loginControl']")
    PASS = (By.CSS_SELECTOR, "input[id='passwordControl']")
    BUTTON_LOGIN = (By.CSS_SELECTOR,
                    'button[class="mat-mdc-tooltip-trigger login__form__btn mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]')
    BUTTON_EXIT = (By.CSS_SELECTOR, 'span[class="mdc-button__label"]')
    MENU = (By.CSS_SELECTOR, "span[class='mat-mdc-button-touch-target']")
    BUTTON_ADMIN = (By.CSS_SELECTOR,
                    "#body > app-root > div > app-toolbar > div > mat-toolbar > mat-toolbar-row > div > div:nth-child(5) > app-profile-brief > button > span.mdc-button__label")


class IncomingLocators:
    INCOMING = (By.XPATH, '//div[contains(text(),"Входящие")]/ancestor::a')
    FIRST_STRING_IN_TABLE = (By.CSS_SELECTOR,
                             '#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div.table-container > table > tbody')
    # TODO - хочу искать вторую строчку и если ее нет, то кликать на первую
    # SECOND_STRING_IN_TABLE = ()



class AccessGroupLocators:
    ACCESS_GROUP = (By.XPATH,
                    '//*[@id="body"]/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[2]/table/tr[9]/td/mat-nav-list/a[1]/span/span/div/div/div')
    BUTTON_ADD_ACCESS_GROUP = (By.XPATH,
                               '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav-content/div/app-listed-data/app-paged-object-list2/mat-drawer-container/mat-drawer-content/div/div[2]/div/button[1]')
    NAME_ACCESS_GROUP = (By.XPATH,
                         '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-access/lib-base-panel/section/div[2]/div[2]/div/div/mat-form-field/div[1]/div[2]/div/input')
    SAVE_AG = (By.XPATH,
               '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-access/lib-base-panel/section/div[2]/mat-dialog-actions/button[1]')
    INPUT_ACCESS_GROUP_IN_MY_APP = (By.XPATH, '/html/body/div[4]/div[3]/div/div/mat-option/span')
    ACCESS_GROUP_IN_MY_APP = (By.XPATH,
                              '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[2]/div/div[1]/div[2]/app-access-group-list-control/mat-form-field/div[1]/div[2]/div[1]/mat-chip-grid/div/input')


class VisitorsLocators:
    VISITORS = (By.CSS_SELECTOR, 'a[href="listedData/PersonByCategory/16"]')
    LAST_NAME = (By.XPATH,
                 '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-person/lib-base-panel/section/div[2]/div[2]/div/div[1]/div/mat-form-field[1]/div[1]/div[2]/div/input')
    VISITORS_FRAME = (By.CSS_SELECTOR, 'div[class="content ng-star-inserted"]')
    FIRST_NAME = (By.XPATH,
                  '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-person/lib-base-panel/section/div[2]/div[2]/div/div[1]/div/mat-form-field[2]/div[1]/div[2]/div/input')
    SAVE_PERSON = (By.XPATH,
                   '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-person/lib-base-panel/section/div[2]/mat-dialog-actions/button[1]')
    FIND_VISITORS = (By.XPATH, "//input[contains(@name, 'filter-input')]")
    FIND_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and contains(@class, 'mdc-checkbox__native-control')]")
    BUTTON_DEL = (By.CSS_SELECTOR,
                  "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div:nth-child(2) > div > button.mat-mdc-tooltip-trigger.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted > span.mat-mdc-button-touch-target")
    BUTTON_ADD_VISITORS = (By.CSS_SELECTOR,
                           "button[class='mat-mdc-tooltip-trigger mdc-icon-button mat-mdc-icon-button mat-primary mat-mdc-button-base ng-star-inserted']")

    TEXT_ID = (By.XPATH, "//h3[@class='title ng-star-inserted']")
    VISITORS_BUTTON = (By.CSS_SELECTOR, "span[class='mdc-list-item__primary-text']")
    INPUT_VISITOR = (By.XPATH, "//input[@placeholder='Посетители']")


class EmployeeLocators:
    MENU_EMPLOYEE = (By.CSS_SELECTOR,
                     "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav > div > div > div:nth-child(1) > div.divLtr.ng-star-inserted > table > tr:nth-child(3) > td > mat-nav-list > a:nth-child(1) > span > span > div")
    INPUT_WORKER = (By.XPATH, "//input[@placeholder='Работник']")
    EMAIL_SEARCH = (By.XPATH, ".//input[@autocomplete='email']")
    CONTACT_INFORM = (By.XPATH, '//div[@class="wrapper" and contains(text(), "Контактная информация")]')


class BaseLocators:
    MENU = (By.CSS_SELECTOR, "span[class='mat-mdc-button-touch-target']")
    FIND = (By.CSS_SELECTOR, 'input[id="mat-input-1"]')
    BUTTON_OPEN_ALL = "/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[1]/div/button/span[1]"
    SAVE_APPROVE = (By.XPATH, "//span[contains(text(), 'Сохранить')]")
    BUTTON_OK = (By.XPATH, "//span[contains(text(), 'ОК')]")
    # переделать остальные FIND под этот
    FIND_POISK = (By.XPATH, "//input[@placeholder='Поиск']")
    BUTTON_RESTART = (By.CSS_SELECTOR,
                      '#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div:nth-child(2) > div > button:nth-child(6)')


class OperatorsLocator:
    OPERATORS = (By.CSS_SELECTOR, 'a.mat-mdc-list-item[href="listedData/User"]')
    BUTTON_INPUT = (By.XPATH, "//input[@placeholder='ФИО и персональные данные']")
    # Выбираем оператора из выпадающего списка (первую строку - единственную)
    OPERATOR_BUTTON = (By.CSS_SELECTOR, "span[class='mdc-list-item__primary-text']")
    LOGIN_OPERATOR = (By.XPATH, "//input[@placeholder='Логин']")
    PASSWORD_OPERATOR = (By.XPATH, "//input[@placeholder='Пароль']")
    REPLY_PASSWORD = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    CHECK_BOX_OPERATOR = (By.XPATH, "//label[contains(text(), 'Активен ')]")
    MENU_STAFF = (By.XPATH,
                  '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[2]/table/tr[10]/td/mat-nav-list/a[1]')


class IntegrationSettingsLocators:
    MENU_INTEGRATION = (By.XPATH, '//div[contains(text(), "Настройки интеграции")]')
    LOGIN_INTEGRATION = (By.ID, "new-username")
    INPUT_URL = (By.XPATH, "//textarea[@placeholder='URL СКД' or @placeholder='Active Directory URL']")
    NOTIFY = (By.XPATH,
              "//span[@class='mdc-list-item__content']//div[@class='wrapper']")  # заменить на //div[contains(text(), ' Уведомления ')]
    CHECKBOX_INTEGRATION = (By.CLASS_NAME, 'mdc-checkbox__native-control')
    CHECKBOX_AD_LOGIN = (By.XPATH, "//label[contains(text(), ' Авторизация ActiveDirectory ')]")
    INPUT_WEB_SERVER = (By.XPATH, "//input[@placeholder='URL веб сервера']")
    INPUT_URL_RABBIT = (By.XPATH, "//input[@placeholder='URL-адрес RabbitMQ']")
    INPUT_PORT = (By.XPATH, "//input[@placeholder='Порт']")
    INPUT_BASE = (By.XPATH, "//input[@placeholder='Поисковая база']")
    INPUT_NAME = (By.XPATH, "//input[@placeholder='Имя пользователя']")
    INPUT_QUEUE = (By.XPATH, "//input[@placeholder='Название очереди']")
    ACTIVE_BUTTON = (By.XPATH, "//span[contains(text(), 'Активировать') or contains(text(), 'Реактивировать')]")
    BUTTON_CANCEL = (By.XPATH, '//mat-dialog-actions//button[contains(., "Отмена")]')
    CONNECT_CHECK = (By.CSS_SELECTOR,
                     "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div.table-container > table > tbody > tr:nth-child(1) > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.cdk-column-active.mat-column-active.table-cell.ng-star-inserted > div > div")
    WINDOW_SUCCESS = (By.CLASS_NAME, 'mat-mdc-dialog-container')
    BUTTON_IMPORT = (By.XPATH, "//span[contains(text(), 'Импортировать')]")
    BUTTON_SYNCHRON = (By.CSS_SELECTOR,
                       "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div:nth-child(2) > div > div > button > span.mat-mdc-button-touch-target")
    SUCCESS_IMPORT = (By.XPATH, "//span[@class='ng-star-inserted']")
    CHECKBOX_ACTIVITY_AD = (By.XPATH, "//label[contains(text(), ' Active Directory ')]")
    CHECKBOX_ACTIVITY_LyriX = (By.XPATH, "//label[contains(text(), ' LyriX ')]")
    INPUT_CONTAINER = (By.XPATH, "//input[@role='combobox']")
    NEW_FIRST_STRING_IN_TABLE = (By.XPATH, '//button[contains(@class, "edit-btn")]')


class ActivePasseLocators:
    BUTTON_ACTIVE_PASS = (By.CSS_SELECTOR,
                          '#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav > div > div > div:nth-child(1) > div.divLtr.ng-star-inserted > table > tr:nth-child(6) > td > mat-nav-list > a:nth-child(1) > span > span > div > div > div')
    BUTTON_WITHDROW = (By.XPATH, "//span[contains(text(),'Изъять')]")

    CLOSE_WINDOW_ACTIVATE_PASS = (
        By.XPATH, '//button[@class="mdc-icon-button mat-mdc-icon-button mat-primary mat-mdc-button-base"]')
    BUTTON_OK_PATTERN_APPROVE = (By.CSS_SELECTOR,
                                 ' div > div > app-show-msg-component > section > mat-dialog-actions > app-btn-dialog:nth-child(1) > button > span.mdc-button__label')


class ApplicationLocators:
    MY_APPLICATION = (By.XPATH,
                      '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[2]/table/tr[1]/td/mat-nav-list/a[1]')
    DEL_APPLICATION = (By.CSS_SELECTOR,
                       "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div:nth-child(2) > div > button:nth-child(2) > span.mat-mdc-button-touch-target")
    MY_APPLICATION_STATUS = (By.CSS_SELECTOR,
                             "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav > div > div > div:nth-child(1) > div.divLtr.ng-star-inserted > table > tr:nth-child(2) > td > mat-nav-list > a:nth-child(2) > span > span > div")
    # выпадающий список
    LIST_DROP_DAWN = (By.CSS_SELECTOR, "span[class='mdc-list-item__primary-text']")
    BUTTON_IN_PROCESSING = (By.XPATH, "//span[contains(text(), 'В обработку')]")
    AGREEMENT_BUTTON = (By.XPATH, "//span[contains(text(), 'Выдать')]")
    CHECK_BOX_APPROVE = (By.XPATH, "//label[contains(text(), 'Согласие на обработку персональных данных подписано ')]")
    INPUT_NUMBER_PASS = (By.XPATH, "//input[@placeholder='Номер пропуска']")
    STATUS_AGREEMENT = (By.CSS_SELECTOR,
                        ' div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.cdk-drag.cdk-drag-handle.left-side > h3')
    REJECT_BUTTON = (By.XPATH,
                     '/html/body/div[6]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[3]/mat-dialog-actions/app-btn-plain[2]/button')
    ANNUL_BUTTON = (By.XPATH,
                    '/html/body/div[6]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[3]/mat-dialog-actions/button[1]')
    COPY_APPLICATION_BUTTON = (By.CSS_SELECTOR,
                               'div > div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.content.ng-star-inserted > div.content-wrapper > div.toolbar.ng-star-inserted > app-action-toolbar > div > button:nth-child(5)')
    THREE_POINT_AGREEMENT = (By.CSS_SELECTOR,
                             'div > div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.content.ng-star-inserted > div.content-wrapper > div.wrapper.ng-star-inserted > div:nth-child(1) > app-cardholders-table > div > table > tbody > tr > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.actions.cdk-column-actions.mat-column-actions.ng-star-inserted > button')
    BUTTON_ISSUE_ANOTHER_PASS = (By.CSS_SELECTOR, 'div > div > button > span.mdc-list-item__primary-text')
    BUTTON_YES_PO = (By.CSS_SELECTOR,
                     'div > div > app-show-msg-component > section > mat-dialog-actions > app-btn-dialog:nth-child(1) > button')
    BUTTON_PASS = (By.XPATH, "//span[contains(text(), 'Гостевой пропуск')]")
    BUTTON_CONST_PASS = (By.XPATH, "//span[contains(text(), 'Постоянный пропуск')]")
    BUTTON_TEMPORARY_PASS = (By.XPATH, "//span[contains(text(), 'Временный пропуск')]")
