from Pages.applicatoin_page import ApplicationPage
from Pages.base_page import BasePage
from Pages.group_page import GroupPage
from Pages.integration_page import IntegrationPage
from Pages.login_page import LoginPage
from Pages.operator_page import OperatorPage
from Pages.supporting_page import SupportingPage
from Pages.visitor_page import VisitorsPage


class AllPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.login_page = LoginPage(driver, url)
        self.visitors_page = VisitorsPage(driver, url)
        self.supporting_page = SupportingPage(driver, url)
        self.application_page = ApplicationPage(driver, url)
        self.group_page = GroupPage(driver, url)
        self.integration_page = IntegrationPage(driver, url)
        self.operators_page = OperatorPage(driver, url)
