import email
import time

import pytest_check as check

from page_functions.video import CovidCarePage
from locators.locators_covidcare import *
from locators.locators_homepage import *
from locators.locators_news import *
from utils.log import logger
from utils.utilities import SeleniumUtilities
from utils.utilities import read_json


class BaseCOVIDpageFlows(CovidCarePage, SeleniumUtilities):
    """
    Base class for the flows that the user can encounter when interacting with our homepage. For example, logging into
    a new account, or start ordering a flow using the dropdown menu. Flow starts at the website homepage.
    """

    def base_open_covid_care_page(self):
        self.open_covid_care_page()
