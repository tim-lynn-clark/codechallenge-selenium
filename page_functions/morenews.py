import self
from seleniumbase import BaseCase

from data_json.json_file_paths import HEADER_LINKS
from locators.locators_homepage import *
from locators.locators_news import *

from utils.common_ui_actions import CommonUIActions
from utils.utilities import read_json, SeleniumUtilities

HEADER_RANGE = range(1, 10)
FOOTER_RANGE = range(1, 4)


class MoreNewsPage(CommonUIActions, SeleniumUtilities, BaseCase):

    def open_newspage(self):
        self.open(NEWS_URL1)
        self.wait_for_page_to_load()  # Wait for homepage to fully load

    def assert_news_pages_load_page1(self):
        self.assert_element_present(NEWS_LATESTNEWS_TITLE)
        self.wait_for_page_to_load()
        self.scroll_to_bottom()
        self.click(PREVIOUS_PAGE)
        get_newspage_url = self.get_current_url()
        self.assert_equal(get_newspage_url, NEWS_URL2)
        self.assert_true("news/page/2" in get_newspage_url)

    def assert_news_pages_load_page2(self):
        self.scroll_to_bottom()
        self.click(NEXT_PAGE)
        self.wait_for_page_to_load()
        self.assert_element_present(NEWS_LATESTNEWS_TITLE)
        get_newspage_url = self.get_current_url()
        self.assert_equal(get_newspage_url, NEWS_URL1)
        self.assert_true("news/" in get_newspage_url)

        self.wait_for_page_to_load()
        self.click(PREVIOUS_PAGE)
        self.wait_for_page_to_load()

        self.wait_for_page_to_load()
