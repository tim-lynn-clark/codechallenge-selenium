from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from seleniumbase import BaseCase

from utils.log import logger
from utils.utilities import SeleniumUtilities


# LOADING_MASK XPATH encompasses all loading masks that appear throughout the website - not a specific one (thus "or").
LOADING_MASK = "//*[contains(@class, 'loading-mask' and @style='display: block;') or (@alt='Loading...' and " \
               "@style='position: absolute;') or (@data-role='loader') or @class='admin__form-loading-mask' or (" \
               "contains(@data-component, 'referred') and contains(@class, 'loading-mask'))]"
SCROLL_ELEMENT_INTO_MIDDLE = "var viewPortHeight = Math.max(document.documentElement.clientHeight, " \
                             "window.innerHeight || 0); var elementTop = arguments[0].getBoundingClientRect(" \
                             ").top; window.scrollBy(0, elementTop-(viewPortHeight/2));"


class CommonUIActions(SeleniumUtilities, BaseCase):

    def wait_for_loading_mask_to_disappear(self):
        """
        I'm adding this function in places where the loading mask is present for long enough to throw an exception
        since it will try to click on the original element, but will get blocked by said mask.
        The thread sleeps for three seconds before checking whether the loading mask is present. If it's still there,
        it will wait for it to become not visible based on the timeout setting set by SeleniumBase.
        """
        logger.info('Waiting for loading mask to disappear')
        self.wait_for_page_to_load()
        self.sleep(3)
        if self.is_element_visible(LOADING_MASK) is True:
            self.wait_for_element_not_visible(LOADING_MASK)

    def scroll_into_middle_of_page_and_click(self, xpath):
        """
        When clicking on an element, SeleniumBase scrolls the element into view so it will be at the top of the
        browser, causing scenarios where instead of clicking on the element, it might click on another element
        that might be on top of it. This function makes it so the the element will be scrolled into the middle of the
        page and then clicked on.
        """
        try:
            element = WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        except(ValueError, WebDriverException):
            return
        self.driver.execute_script(SCROLL_ELEMENT_INTO_MIDDLE, element)  # Executes a JavaScript
        ActionChains(self.driver).click(element).perform()

    def slow_type(self, element, text: str, sleep_timer=0.1):
        """
        Similar to seleniumbase's slow_click, the tests will sleep for the amount passed to the sleep_timer value (0.1
        seconds by default) before continuing with the next character in the string passed in text. Useful in areas
        where a mask gets auto applied as the the string is being written in the UI.
        """
        char_array = [char for char in text]
        self.clear(element)
        for char in char_array:
            self.add_text(element, char)
            self.sleep(sleep_timer)

    def trigger_ajax(self, element):
        """
        I've noticed that for pages like /subscriptions, the email field won't load when page is visited until AJAX
        is triggered by clicking on a random element. This function (hopefully) will trigger AJAX to render the page
        elements. Please experiment with when elements are missing when page is visited. Might be AJAX.
        """
        self.wait_for_element_visible(element)
        self.scroll_into_middle_of_page_and_click(element)
