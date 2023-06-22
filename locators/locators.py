from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN = (By.CSS_SELECTOR, "input[id='loginControl']")
    PASS = (By.CSS_SELECTOR, "input[id='passwordControl']")
    BUTTON_LOGIN = (By.CSS_SELECTOR,
                    'button[class="mat-mdc-tooltip-trigger login__form__btn mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base"]')
    BUTTON_EXIT = (By.CSS_SELECTOR, 'span[class="mdc-button__label"]')
    MENU = (By.CSS_SELECTOR, "span[class='mat-mdc-button-touch-target']")

class StartPageLocators:
    MENU = (By.CSS_SELECTOR, "span[class='mat-mdc-button-touch-target']")
    FIND = (By.CSS_SELECTOR, 'input[id="mat-input-1"]')
    BUTTON_OPEN_ALL = "/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[1]/div/button/span[1]"
    VISITORS = (By.CSS_SELECTOR, 'a[href="listedData/PersonByCategory/16"]')
    BUTTON_ADD_VISITORS = (By.CSS_SELECTOR,
                           "button[class='mat-mdc-tooltip-trigger mdc-icon-button mat-mdc-icon-button mat-primary mat-mdc-button-base ng-star-inserted']")

    # TODO - Удаление пользователя
    BUTTON_OK = (By.XPATH, "//span[contains(text(), 'ОК')]")
    FIND_VISITORS = (By.CSS_SELECTOR, 'input[id="mat-input-4"]')
    FIND_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and contains(@class, 'mdc-checkbox__native-control')]")
    BUTTON_DEL = (By.CSS_SELECTOR,
                  "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div:nth-child(2) > div > button.mat-mdc-tooltip-trigger.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted > span.mat-mdc-button-touch-target")
    # TODO - END

    # TODO - Удаление заявки
    FIND_APPLICATION = (By.NAME, "filter-input")
    CHECKBOX_APPLICATION = (By.XPATH, "//input[@type='checkbox' and contains(@class, 'mdc-checkbox__native-control')]")
    DEL_APPLICATION = (By.CSS_SELECTOR,
                       "#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div:nth-child(2) > div > button:nth-child(2) > span.mat-mdc-button-touch-target")
    APPLICATION_OK = (By.XPATH, "//span[contains(text(), 'ОК')]")
    #TODO - END

    LAST_NAME = (By.XPATH,
                 '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-person/lib-base-panel/section/div[2]/div[2]/div/div[1]/div/mat-form-field[1]/div[1]/div[2]/div/input')
    VISITORS_FRAME = (By.CSS_SELECTOR, 'div[class="content ng-star-inserted"]')
    FIRST_NAME = (By.XPATH,
                  '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-person/lib-base-panel/section/div[2]/div[2]/div/div[1]/div/mat-form-field[2]/div[1]/div[2]/div/input')
    SAVE_PERSON = (By.XPATH,
                   '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-person/lib-base-panel/section/div[2]/mat-dialog-actions/button[1]')

    ACCESS_GROUP = (By.XPATH,
                    '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[2]/table/tr[10]/td/mat-nav-list/a[1]')
    BUTTON_ADD_ACCESS_GROUP = (By.XPATH,
                               '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav-content/div/app-listed-data/app-paged-object-list2/mat-drawer-container/mat-drawer-content/div/div[2]/div/button[1]')
    NAME_ACCESS_GROUP = (By.XPATH,
                         '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-access/lib-base-panel/section/div[2]/div[2]/div/div/mat-form-field/div[1]/div[2]/div/input')
    SAVE_AG = (By.XPATH,
               '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-access/lib-base-panel/section/div[2]/mat-dialog-actions/button[1]')

    MY_APPLICATION = (By.XPATH,
                      '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[2]/table/tr[1]/td/mat-nav-list/a[1]')
    VISITORS_IN_MY_APP = (By.XPATH,
                          '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[2]/div/div[1]/app-person-list-control/mat-form-field/div[1]/div[2]/div[1]/mat-chip-grid/div/input')

    ACCESS_GROUP_IN_MY_APP = (By.XPATH,
                              '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[2]/div/div[1]/div[2]/app-access-group-list-control/mat-form-field/div[1]/div[2]/div[1]/mat-chip-grid/div/input')

    BUTTON_IN_PROCESSING = (By.XPATH,
                            '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[3]/mat-dialog-actions/app-btn-plain[1]/button')
    INPUT_VISITORS = (By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div/mat-option[5]/span/div')
    BUTTON_DAWN_DROP = (By.XPATH,
                        '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[2]/div/div[1]/app-person-list-control/mat-form-field/div[1]/div[2]/div[2]/button[1]/span[4]')
    INPUT_ACCESS_GROUP_IN_MY_APP = (By.XPATH, '/html/body/div[4]/div[3]/div/div/mat-option/span')
    CLOSE_WINDOW_MY_APP = (By.XPATH,
                           '/html/body/div[4]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[1]/div[2]/button[2]/span[4]')

    INCOMING = (By.XPATH,
                '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav/div/div/div[1]/div[2]/table/tr[2]/td/mat-nav-list/a[1]')

    FIRST_STRING_IN_TABLE = (By.XPATH,
                             '/html/body/app-root/div/app-content/mat-sidenav-container/mat-sidenav-content/div/app-listed-data/app-paged-object-list2/mat-drawer-container/mat-drawer-content/div/div[4]/table/tbody/tr[1]')

    THREE_POINT_INCOMING = (By.CSS_SELECTOR,
                            ' div > div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.content.ng-star-inserted > div.content-wrapper > div.wrapper.ng-star-inserted > div:nth-child(1) > app-cardholders-table > div > table > tbody > tr > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.actions.cdk-column-actions.mat-column-actions.ng-star-inserted > button > span.mat-mdc-button-touch-target')

    ISSUE_PASS = (By.XPATH, '/html/body/div[4]/div[4]/div/div/div/div/button')

    REJECT_BUTTON = (By.XPATH,
                     '/html/body/div[6]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[3]/mat-dialog-actions/app-btn-plain[2]/button')
    AGREEMENT_BUTTON = (By.CSS_SELECTOR,
                        'div > div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.content.ng-star-inserted > div.custom-actions > mat-dialog-actions > app-btn-plain:nth-child(1) > button')
    ANNUL_BUTTON = (By.XPATH,
                    '/html/body/div[6]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[3]/mat-dialog-actions/button[1]')

    STATUS_AGREEMENT = (By.CSS_SELECTOR,
                        ' div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.cdk-drag.cdk-drag-handle.left-side > h3')
    THREE_POINT_AGREEMENT = (By.CSS_SELECTOR,
                             'div > div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.content.ng-star-inserted > div.content-wrapper > div.wrapper.ng-star-inserted > div:nth-child(1) > app-cardholders-table > div > table > tbody > tr > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.actions.cdk-column-actions.mat-column-actions.ng-star-inserted > button')
    BUTTON_ISSUE_PASS = (By.CSS_SELECTOR,
                         '#body > div.cdk-overlay-container > div.cdk-overlay-connected-position-bounding-box > div > div > div > div > button')

    APPROVE_PATTERN = (By.XPATH,
                       '/html/body/div[6]/div[4]/div/mat-dialog-container/div/div/app-show-msg-component/section/app-dialog-header/div/div/div[1]/h2')
    BUTTON_OK_PATTERN_APPROVE = (By.CSS_SELECTOR,
                                 ' div > div > app-show-msg-component > section > mat-dialog-actions > app-btn-dialog:nth-child(1) > button > span.mdc-button__label')

    CHECK_BOX_APPROVE = (By.CSS_SELECTOR, 'div.mdc-checkbox >  input.mdc-checkbox__native-control')
    SAVE_APPROVE = (By.XPATH,
                    '/html/body/div[6]/div[4]/div/mat-dialog-container/div/div/app-consent-dialog/mat-dialog-actions/button[1]')

    INPUT_NUMBER_PASS = (By.CSS_SELECTOR,
                         'div > div > app-issue-pass-component > div > mat-dialog-content > div > app-pass-number > app-pass-number-control > mat-form-field > div.mat-mdc-text-field-wrapper.mdc-text-field--filled.mdc-text-field--invalid > div.mat-mdc-form-field-flex > div.mat-mdc-form-field-infix > input')  # v
    BUTTON_OK_NUMBER_PASS = (
    By.CSS_SELECTOR, 'div > div > app-issue-pass-component > div > mat-dialog-actions > button')

    COPY_APPLICATION_BUTTON = (By.CSS_SELECTOR,
                               'div > div > app-show-obj-component > section > app-common-object-editor > div > app-request > lib-base-panel > section > div.content.ng-star-inserted > div.content-wrapper > div.toolbar.ng-star-inserted > app-action-toolbar > div > button:nth-child(5)')
    COPY_APPLICATION_BUTTON_XPATH = (By.XPATH,
                                     '/html/body/div[6]/div[2]/div/mat-dialog-container/div/div/app-show-obj-component/section/app-common-object-editor/div/app-request/lib-base-panel/section/div[2]/div[2]/div[1]/app-action-toolbar/div/button[3]')
    CHOOSE_FIRST_LINE = (By.CSS_SELECTOR,
                         '#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav-content > div > app-listed-data > app-paged-object-list2 > mat-drawer-container > mat-drawer-content > div > div.table-container > table > tbody > tr:nth-child(1)')

    BUTTON_ISSUE_ANOTHER_PASS = (By.CSS_SELECTOR, 'div > div > button > span.mdc-list-item__primary-text')

    BUTTON_WITHDROW = (By.CSS_SELECTOR,
                       ' div > div > app-show-obj-component > section > app-common-object-editor > div > app-pass > lib-base-panel > section > div.content.ng-star-inserted > mat-dialog-actions > app-btn-plain:nth-child(2) > button')
    BUTTON_ACTIVE_PASS = (By.CSS_SELECTOR,
                          '#body > app-root > div > app-content > mat-sidenav-container > mat-sidenav > div > div > div:nth-child(1) > div.divLtr.ng-star-inserted > table > tr:nth-child(6) > td > mat-nav-list > a:nth-child(1) > span > span > div > div > div')
    CLOSE_WINDOW_ACTIVATE_PASS = (By.CSS_SELECTOR,
                                  ' div > div > app-show-obj-component > section > app-common-object-editor > div > app-pass > lib-base-panel > section > div.content.ng-star-inserted > div.cdk-drag.cdk-drag-handle.top > div.top__actions > button:nth-child(2)')

    BUTTON_YES_PO = (By.CSS_SELECTOR,
                     'div > div > app-show-msg-component > section > mat-dialog-actions > app-btn-dialog:nth-child(1) > button')
