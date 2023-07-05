import time

from Pages.login_page import LoginPage, StartPage

"""Авторизация"""


def test_login_form(driver):
    login_page = LoginPage(driver, 'http://localhost/auth/login')
    login_page.open()
    login_page.filing_login_pass()
    answer = login_page.check_login()
    assert answer == 'http://localhost/listedData/userRequestsAll', "Произошла ошибка авторизации"
    return driver.current_url


"""Создание посетителя"""


def test_add_visitor(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    id_visitor = start_page.add_visitors()
    assert start_page.check_visitor_id(id_visitor), "Ошибка при добавлении посетителя"


"""Удаление посетителя"""


def test_del_visitor(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    last_name, first_name = start_page.del_visitors()
    assert not start_page.check_visitor_fio(last_name, first_name), "Ошибка при удалении посетителя"


"""Создание Группы Доступа"""


def test_add_access_group(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_access_group()


"""Создание заявки"""


def test_create_my_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    # txt = 'Постоянный'
    txt = 'Гостевой'
    if txt != 'Гостевой':
        start_page.add_employee()
    else:
        start_page.add_visitors()
    start_page.add_my_application(txt)
    start_page.open_incoming()
    # """Перевод заявки в согласие и выдача заявки"""
    start_page.agreement_application()
    start_page.issue_pass()
    test_1 = start_page.signing_receiving_pass(txt)
    assert test_1 == 'Разрешено', "\nПроизошла ошибка"
    test_2 = start_page.check_status()
    assert test_2 == 'Обработано', "\nПроизошла ошибка"


"""Кейс_7"""


# проверка вылета оператора после деактивации
def test_case_7(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_employee()
    start_page.add_operator()
    old_url = start_page.open_new_url()
    new_url = start_page.active_off()
    assert old_url != new_url, "\nПроизошла ошибка"


"""Удаление заявки"""


def test_del_my_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.del_my_application()


"""делает изъятие выдачи"""


def test_withdraw_pass(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.open_only_menu()
    start_page.withdraw_pass()


# Валится
def test_copy_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.copy_application()
    start_page.open_incoming()
    start_page.add_another_pass()
    start_page.signing_receiving_pass('a')


"""Удаление оператора"""


# TODO - добавить проверку на удаление
def test_del_operator(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    assert start_page.del_operator('Операторы'), f"Ошибка при удалении в разделе Операторы"


def test_integration(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    name = 'LyriX'
    var = '✓'
    assert start_page.switch_integration(name) == var, f"Произошла ошибка интеграции {name}"


"""Удаление сотрудника"""


def test_del_employee(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    assert start_page.del_operator('Сотрудники'), "Ошибка при удалении в разделе Сотрудники"


"""Кейс №7 с удалением всего созданного за собой"""


def test_case_7_all(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_employee()
    last_name = start_page.add_operator()
    old_url = start_page.open_new_url()
    new_url = start_page.active_off(last_name)
    assert old_url != new_url, "Произошла ошибка"
    driver.switch_to.window(driver.window_handles[0])
    assert start_page.del_operator('Операторы'), "Ошибка при удалении в разделе Операторы"
    assert start_page.del_operator('Сотрудники'), "Ошибка при удалении в разделе Сотрудники"


def test_case_unknown(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    assert start_page.switch_integration('LyriX') == '✓', "Произошла ошибка интеграции LyriX"
    start_page.open_only_menu()
    assert start_page.switch_integration('Active Directory') == '✓', "Произошла ошибка интеграции Active Directory"
    assert start_page.synchron() == 'Объекты успешно импортированы.', 'Произошла ошибка синхронизации'
    assert start_page.check_operator() != (True, True), 'Ошибка импортирования'  # TODO - неккоректно работает функция
    start_page.login_AD()
