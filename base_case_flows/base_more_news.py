import email
import time

import pytest_check as check

from page_functions.morenews import MoreNewsPage
from locators.locators_homepage import *
from locators.locators_news import *
from utils.log import logger
from utils.utilities import SeleniumUtilities
from utils.utilities import read_json



class BaseNewspageFlows(MoreNewsPage, SeleniumUtilities):
    """
    Base class for the flows that the user can encounter when interacting with our homepage. For example, logging into
    a new account, or start ordering a flow using the dropdown menu. Flow starts at the website homepage.
    """

    def newspage_more_nav(self):
        self.open_newspage()
        self.assert_news_pages_load_page1()
        self.assert_news_pages_load_page2()
