import time

from pytest import mark

from base_case_flows.base_about_us import BaseAboutUsPage
from locators.locators_news import *


class AboutUsPage(BaseAboutUsPage):

    @mark.sanity
    @mark.e2e
    def test_aboutus_nav(self):
        self.aboutus_page()
