import requests
from seleniumbase import BaseCase
import cv2
import numpy as np

from data_json.json_file_paths import *
from locators.locators_covidcare import *
from locators.locators_homepage import *
from locators.locators_news import *

from utils.common_ui_actions import CommonUIActions
from utils.utilities import read_json, SeleniumUtilities


class CovidCarePage(CommonUIActions, SeleniumUtilities, BaseCase):

    def open_covid_care_page(self):
        self.open(COVID_CARE_URL)
        self.wait_for_page_to_load()  # Wait for homepage to fully load
        self.assert_element_present(HELLO_DIALOG)
        self.click(READ_DIALOG)
        self.click(AGREE_DIALOG)
        self.click(HELLO_DIALOG_CONTINUE)
        self.wait_for_page_to_load()  # Wait for homepage to fully load

        self.wait_for_element_visible(COVID_WELCOME)
        self.assert_element_present(COVID_ABOUT)
        self.click(COVID_ABOUT)
        self.scroll_into_middle_of_page_and_click(COVID_ABOUT_CLOSE)

        self.wait_for_element_visible(COVID_HELP)
        self.click(COVID_HELP)
        self.wait_for_element_visible(HELP_DIALOG)
        self.click(COVID_ABOUT_CLOSE)



