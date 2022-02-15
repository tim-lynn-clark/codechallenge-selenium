import email
import time

from page_functions.clinicaltrials import Clinicaltrials
from locators.locators_clinical_trials import *

from utils.log import logger
from utils.utilities import SeleniumUtilities


class BaseClinicalTrialsPage(Clinicaltrials, SeleniumUtilities):
    """
    Base class for the flows that the user can encounter when interacting with our homepage. For example, logging into
    a new account, or start ordering a flow using the dropdown menu. Flow starts at the website homepage.
    """

    def clinical_trials_page(self):
        self.open_clinicaltrialspage()
        self.assert_clinicaltrials_learnmore()
