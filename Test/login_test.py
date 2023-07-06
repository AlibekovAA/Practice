from Pages.all_page import AllPage

"""Авторизация"""


def test_login_form(driver):
    page = AllPage(driver, 'http://localhost/auth/login')
    page.open()
    page.login_page.filing_login_pass()
    answer = page.login_page.check_login()
    assert answer == 'http://localhost/listedData/userRequestsAll', "Произошла ошибка авторизации"
    return driver.current_url


"""Создание посетителя"""


def test_add_visitor(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    id_visitor = page.visitors_page.add_visitors()
    assert page.supporting_page.check_visitor_id(id_visitor), "Ошибка при добавлении посетителя"


"""Удаление посетителя"""


def test_del_visitor(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    last_name, first_name = page.visitors_page.del_visitors()
    assert not page.supporting_page.check_visitor_fio(last_name, first_name), "Ошибка при удалении посетителя"


"""Создание Группы Доступа"""


def test_add_access_group(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    page.group_page.add_access_group()


"""Удаление Группы Доступа"""


def test_del_access_group(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    page.group_page.del_access_group()


"""Создание заявки"""


def test_create_my_application(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    # txt = 'Постоянный'
    txt = 'Гостевой'
    if txt != 'Гостевой':
        page.visitors_page.add_employee()
    else:
        page.visitors_page.add_visitors()
    page.application_page.add_my_application(txt)
    page.application_page.open_incoming()
    # """Перевод заявки в согласие и выдача заявки"""
    page.application_page.agreement_application()
    page.application_page.issue_pass()
    test_1 = page.application_page.signing_receiving_pass(txt)
    assert test_1 == 'Разрешено', "\nПроизошла ошибка"
    test_2 = page.application_page.check_status()
    assert test_2 == 'Обработано', "\nПроизошла ошибка"


"""Кейс_7 проверка вылета оператора после деактивации"""


def test_case_7(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    page.visitors_page.add_employee()
    last_name = page.operators_page.add_operator()
    old_url = page.operators_page.open_new_url()
    new_url = page.operators_page.active_off(last_name)
    assert old_url != new_url, "\nПроизошла ошибка"


"""Удаление заявки"""


def test_del_my_application(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    page.application_page.del_my_application()


"""делает изъятие выдачи"""


def test_withdraw_pass(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    page.supporting_page.open_only_menu()
    page.application_page.withdraw_pass()


# Валится
def test_copy_application(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    page.application_page.copy_application()
    page.application_page.open_incoming()
    page.application_page.add_another_pass()
    page.application_page.signing_receiving_pass('a')


"""Удаление оператора"""


def test_del_operator(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    last_name, first_name = page.operators_page.del_operator('операторы')
    assert not page.supporting_page.check_visitor_fio(last_name, first_name), f"Ошибка при удалении в разделе Операторы"


def test_integration(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    name = 'LyriX'
    var = '✓'
    assert page.integration_page.switch_integration(name) == var, f"Произошла ошибка интеграции {name}"


"""Удаление сотрудника"""


def test_del_employee(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    assert page.operators_page.del_operator('Сотрудники'), "Ошибка при удалении в разделе Сотрудники"


"""Кейс №7 с удалением всего созданного за собой"""


def test_case_7_all(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    page.visitors_page.add_employee()
    last_name = page.operators_page.add_operator()
    old_url = page.operators_page.open_new_url()
    new_url = page.operators_page.active_off(last_name)
    assert old_url != new_url, "Произошла ошибка"
    driver.switch_to.window(driver.window_handles[0])
    assert page.operators_page.del_operator('Операторы'), "Ошибка при удалении в разделе Операторы"


def test_case_unknown(driver):
    url = test_login_form(driver)
    page = AllPage(driver, url)
    assert page.integration_page.switch_integration('LyriX') == '✓', "Произошла ошибка интеграции LyriX"
    page.supporting_page.open_only_menu()
    assert page.integration_page.switch_integration('Active Directory') == '✓', "Произошла ошибка интеграции Active Directory"
    status, id_person = page.integration_page.synchron()
    assert status == 'Объекты успешно импортированы.', 'Произошла ошибка синхронизации'
    assert page.integration_page.check_operator(id_person) == (True, True), 'Ошибка импортирования'
    page.integration_page.login_AD()
