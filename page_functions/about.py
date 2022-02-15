import self
from pytest_check import check
from seleniumbase import BaseCase

from locators.locators_homepage import *
from locators.locators_about_us import *
from utils.common_ui_actions import CommonUIActions
from utils.utilities import read_json, SeleniumUtilities

class MoreAboutUsPage(CommonUIActions, SeleniumUtilities, BaseCase):

    def open_aboutuspage(self):
        self.open(ABOUT_US_URL)
        self.wait_for_page_to_load()  # Wait for homepage to fully load
        self.assert_element_present(ABOUT_US_TITLE)
        self.assert_element_visible(ABOUT_US_LEARNMORE_BUTTON)

    def assert_aboutus_learnmore(self):
        self.click(ABOUT_US_LEARNMORE_BUTTON)
        self.wait_for_page_to_load()
        self.assert_element_present(ABOUS_US_ORG)