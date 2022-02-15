import email
import pytest_check as check

from page_functions.homepage import Homepage
from utils.log import logger
from utils.utilities import SeleniumUtilities
from utils.utilities import read_json

class BaseHomepageFlows(Homepage, SeleniumUtilities):
    """
    Base class for the flows that the user can encounter when interacting with our homepage. For example, logging into
    a new account, or start ordering a flow using the dropdown menu. Flow starts at the website homepage.
    """

    def homepage_about(self):
        self.open_homepage()
        self.click_banner()

    def homepage_mission(self):
        self.open_homepage()
        self.click_mission_learn_more()
        self.assert_mission_learnmore()

    def homepage_latestnews(self):
        self.open_homepage()
        self.click_more_news()
        """self.assert_more_news()"""

    def homepage_covid_cancercare(self):
        self.open_homepage()
        self.click_covid_cancercare()

    def homepage_CRD(self):
        self.open_homepage()
        self.click_cancer_related_distress()

    def homepage_check_links_flow(self, json_file):
        logger.info('Assert all header and footer links')
        data = read_json(json_file)
        self.open_homepage()
        self.assert_header_buttons_present()
        self.assert_header_links()
        self.assert_header_pages_load()
        self.assert_footer_buttons_present(email)
        self.assert_footer_links(email)
        self.assert_footer_pages_load()
        self.private_policy()
        self.contact_us(data['first_name'], data['last_name'], data['emailid'])



