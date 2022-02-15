import time

from pytest import mark

from base_case_flows.base_covid_care import BaseCOVIDpageFlows
from locators.locators_covidcare import *
from locators.locators_homepage import *
from locators.locators_news import *


class CovidCarePageTest(BaseCOVIDpageFlows):

    @mark.sanity
    @mark.e2e
    def test_covidcarepage_more_nav(self):
        self.base_open_covid_care_page()
