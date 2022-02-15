import time

from pytest import mark

from base_case_flows.base_clinical_trials import BaseClinicalTrialsPage
from locators.locators_news import *


class ClinicalTrialsPage(BaseClinicalTrialsPage):

    @mark.sanity
    @mark.e2e
    def test_clinical_trials_page(self):
        self.clinical_trials_page()
