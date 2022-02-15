import email
import time

from page_functions.about import MoreAboutUsPage
from locators.locators_news import *
from locators.locators_about_us import *

from utils.log import logger
from utils.utilities import SeleniumUtilities


class BaseAboutUsPage(MoreAboutUsPage, SeleniumUtilities):
    """
    Base class for the flows that the user can encounter when interacting with our homepage. For example, logging into
    a new account, or start ordering a flow using the dropdown menu. Flow starts at the website homepage.
    """

    def aboutus_page(self):
        self.open_aboutuspage()
        self.assert_aboutus_learnmore()
