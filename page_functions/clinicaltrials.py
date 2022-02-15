import self
from pytest_check import check
from seleniumbase import BaseCase

from locators.locators_homepage import *
from locators.locators_clinical_trials import *
from utils.common_ui_actions import CommonUIActions
from utils.utilities import read_json, SeleniumUtilities

class Clinicaltrials(CommonUIActions, SeleniumUtilities, BaseCase):

    def open_clinicaltrialspage(self):
        self.open(CLINICAL_TRIALS_URL)
        self.wait_for_page_to_load()  # Wait for homepage to fully load
        self.assert_element_present(CLINICAL_TRIALS_TITLE)




    def assert_clinicaltrials_learnmore(self):
        self.assert_element_present(VIEW_CURRENT_TRIALS_GOV)
        self.click(VIEW_CURRENT_TRIALS_GOV)
        self.wait_for_page_to_load()
        self.scroll_to_bottom()
        self.wait_for_page_to_load()

        get_news_url = self.get_current_url()
        self.assert_equal(get_news_url, CURRENT_TRIALS_REDIRECT)
        self.assert_true("clinicaltrials" in get_news_url)