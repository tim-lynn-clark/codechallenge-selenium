import time

from pytest import mark

from base_case_flows.base_more_news import BaseNewspageFlows
from locators.locators_news import *


class MoreNewsPageTest(BaseNewspageFlows):

    @mark.sanity
    @mark.e2e
    def test_newspage_more_nav(self):
        self.newspage_more_nav()
