import time

from Pages.login_page import LoginPage, StartPage

"""Авторизация  Обдумать над чеком автоизации"""


def test_login_form(driver):
    login_page = LoginPage(driver, 'http://localhost/auth/login')
    login_page.open()
    time.sleep(0.1)
    login_page.filing_login_pass()
    time.sleep(0.1)
    # now_url = driver.getCurrenUrl
    # answer = login_page.check_login()
    # assert answer in 'Выход'
    return driver.current_url
    # TODO  - сделать проверку что авторизация прошла успешна - можно по урл


"""Создание посетителя"""


def test_add_visitor(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_visitors()
    return driver.current_url


"""Удаление посетителя"""


def test_del_visitor(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.del_visitors()
    return driver.current_url


"""Создание Группы Доступа"""


def test_add_access_group(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_access_group()


"""Создание заявки"""


def test_create_my_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_my_application()

    start_page.open_incoming()
    """Перевод заявки в согласие и выдача заявки"""
    start_page.agreement_application()
    txt_1 = start_page.issue_pass()
    start_page.signing_receiving_pass(txt_1)

    # time.sleep(2)


"""Удаление заявки"""


def test_del_my_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.del_my_application()

    # TODO - сделать проверку что создалась заявка и то что она в обработке
    # TODO - допилить тест для создание заявки

"""делает изъятие выдачи"""
def test_withdraw_pass(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.open_menu()
    start_page.withdraw_pass()

def test_copy_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.copy_application()
    start_page.open_incoming()
    start_page.add_another_pass()
    start_page.signing_receiving_pass('a')

