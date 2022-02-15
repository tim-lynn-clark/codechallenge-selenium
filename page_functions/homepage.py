import email

from seleniumbase import BaseCase

from data_json.json_file_paths import HEADER_LINKS,CONTACT_US
from locators.locators_homepage import *
from locators.locators_news import *
from locators.locators_why import *
from locators.locators_covidcare import *

from utils.common_ui_actions import CommonUIActions
from utils.utilities import read_json, SeleniumUtilities

HEADER_RANGE = range(1, 7)


class Homepage(CommonUIActions, SeleniumUtilities, BaseCase):

    def open_homepage(self):
        self.open(HOMEPAGE_URL)
        self.assert_title(HOMEPAGE_TITLE)
        self.wait_for_page_to_load()  # Wait for homepage to fully load

    def click_banner(self):
        self.wait_for_element_visible(BANNER)
        self.click(BANNER)
        self.wait_for_page_to_load()
        self.assert_title(HOMEPAGE_TITLE)

    def click_mission_learn_more(self):
        self.assert_element_present(CANCER_PATIENTS_TITLE)
        self.click(LEARNMORE_ABOUT_BUTTON)
        self.wait_for_page_to_load()

        self.assert_element_present(CANCER_DISTRESS_TITLE)

    def click_more_news(self):
        self.assert_element_present(LATEST_NEWS_TITLE)
        self.click(MORE_NEWS)
        self.wait_for_page_to_load()
        get_news_url = self.get_current_url()
        self.assert_equal(get_news_url, NEWS_URL1)
        self.assert_true("news" in get_news_url)

    def click_covid_cancercare(self):
        self.assert_element_present(COVID_CARE_PROGRAM_TITLE)
        self.click(TRYIT_HERE)
        self.wait_for_page_to_load()
        get_covid_care_url = self.get_current_url()
        self.assert_equal(get_covid_care_url, COVID_CARE_URL)
        self.assert_true("covid" in get_covid_care_url)

    def click_cancer_related_distress(self):
        self.scroll_to_bottom()
        self.assert_element_present(CANCER_DISTRESS_TITLE)
        self.click(LEARNMORE_WHY_BUTTON)
        self.wait_for_page_to_load()
        self.assert_element_present(CANCER_RELATED_DISTRESS_TITLE)
        get_why_url = self.get_current_url()
        self.assert_equal(get_why_url, WHY_URL)
        self.assert_true("why" in get_why_url)

    def contact_us(self, first_name, last_name, emailid):
        self.wait_for_element_present(CONTACT_US)
        self.wait_for_element_present(CONTACT_US)
        self.type(FIRST_NAME, first_name)
        self.type(LAST_NAME, last_name)
        self.type(EMAIL, emailid)
        self.click(SUBMIT)
        contact_success_url = self.get_current_url()
        self.assert_equal(contact_success_url, CONTACT_US_REDIRECT)
        self.assert_true("success" in contact_success_url)

    def private_policy(self):
        self.wait_for_element_present(PRIVATE_POLICY)
        self.click(PRIVATE_POLICY)
        self.wait_for_page_to_load()
        private_policy_url = self.get_current_url()
        self.assert_equal(private_policy_url, PRIVATE_POLICY_REDIRECT)
        self.assert_true("policy" in private_policy_url)

    def assert_mission_learnmore(self):
        self.assert_element_present(LEARNMORE_ABOUT_BUTTON)

    def assert_tryit_here(self):
        self.assert_element_present(TRYIT_HERE)

    def assert_CRD_learn_more(self):
        self.assert_element_present(LEARNMORE_CRD_BUTTON)

    def assert_header_pages_load(self):
        data = read_json(HEADER_LINKS)
        for x in HEADER_RANGE:
            self.click(header_button(x))
            self.wait_for_page_to_load()

    def assert_footer_pages_load(self):
        self.assert_element_present(FOOTER_HELP)
        self.wait_for_page_to_load()

    def assert_footer_links(self, email1):
        self.assert_element_present(FOOTER_EMAIL, email)
        self.assert_footer_pages_load()

    def assert_header_links(self):
        self.assert_header_buttons_present()
        self.assert_header_pages_load()

    def assert_header_buttons_present(self):
        for x in HEADER_RANGE:
            self.assert_element_visible(header_button(x))

    def assert_footer_buttons_present(self, email1):
        self.assert_element_visible(FOOTER_EMAIL, email)

