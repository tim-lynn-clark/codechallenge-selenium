import json
import os
from quopri import decodestring
from urllib.parse import quote

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.command import Command
from seleniumbase import BaseCase

from utils.log import logger

# TODO: Switch to using catsdk for repeated functions like parsing JSON

NETWORK_LOG_JS_SCRIPT = "var performance = window.performance || window.mozPerformance || window.msPerformance || " \
                        "window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"


def is_aws_profile_prod():
    if os.environ["AWS_PROFILE"] == 'credo-prod':
        return True


def convert_s3_body_to_browser_readable_html(html):
    """
    Encodes text into bytes, decodes the MIME-stylized HTML into normal HTML, and then replaces special characters
    in the string using %xx escape. The result can be opened using driver.get(html)
    :param html The piece of HTML code to convert to readable code.
    """
    index = html.find('<!DOCTYPE')
    html = decodestring(str.encode(html[index:]))
    logger.info('Construct data URI out of S3 body')
    return f'data:text/html;charset=utf-8,{quote(html)}'


def create_abs_path(file_location):
    """
    Creates an absolute path to a file based on the root directory.
    """
    this_file_path = os.path.dirname(__file__)
    # Remove one level of the directory since this file is one deep.
    # If this script is moved to another sub-directory, then the next code line will need to change.
    absolute_script_dir = os.path.split(this_file_path)[0]
    absolute_file_path = os.path.join(absolute_script_dir, file_location)
    return absolute_file_path


def read_json(file_location, absolute=False):
    if absolute is True:
        file_path = create_abs_path(file_location)
    else:
        file_path = file_location

    with open(file_path, mode="r") as json_file:
        try:
            contents = json.load(json_file)
        except ValueError:
            raise ValueError(f"Error parsing JSON file {file_path} so check formatting issues.")
        else:
            return contents


class SeleniumUtilities(BaseCase):
    """
    Class containing functions that interact with the Chrome driver, but do not touch the UI itself.
    """

    def get_driver_status(self):
        """
        Checks the current status of driver. An exception will be thrown by Command.STATUS and returned as a false
        boolean if the driver is currently dead.
        """
        try:
            self.driver.execute(Command.STATUS)
            return True
        except Exception:
            return False

    def wait_for_page_to_load(self):
        """
        Similar to get_network_logs, it's an easy way to wait for the page to load. For sake of code readability,
        this function doesn't return anything. Just keeps cycling until returned logs from JS = saved logs in string.

        Please use where it's crucial to the page to load before doing something (e.g. the plans page - buttons don't
        work if clicked immediately on page visit)
        """
        logger.info('Waiting for page to finish loading.')
        self.sleep(0.5)
        log = self.execute_script(NETWORK_LOG_JS_SCRIPT)
        network_logs = ''
        while network_logs != log:
            network_logs = log
            self.sleep(1)
            log = self.execute_script(NETWORK_LOG_JS_SCRIPT)

    def get_network_logs(self):
        """
        Selenium doesn't have a built-in ability to log requests that are coming through, so I've created a custom
        JS (thanks StackOverflow) that will collect all network requests when the command is called.
        The script is placed in a while loop as a way to wait until the page fully loads. The stdout is chaotic,
        so whoever will print the logs should probably search for the expected request using Control/Command + F.
        """

        try:
            logger.info('Gathering network logs.')
            log = self.execute_script(NETWORK_LOG_JS_SCRIPT)
            network_logs = ''
            while network_logs != log:
                network_logs = log
                self.sleep(2)
                log = self.execute_script(NETWORK_LOG_JS_SCRIPT)
        except ValueError:
            return  # Throws exception if there was problem gathering the logs
        return str(log)  # An exception gets thrown if the logs are not converted to string

    def get_console_logs(self):
        """
        Used in tearDown - print the browser console. The entry gets manipulated to remove the placeholder
        'level' before each entry and the timestamp. The resulting entry would looks something along the lines of:

        {'SEVERE', 'message': 'Failed to load resource: server responded with a status of 400 ()', 'source': 'network'}

        Code related to Allure is commented out for now until we decide which reporting tool we'd like to use.
        """
        try:
            # full_log = ''
            browser_logs = self.driver.get_log('browser')
        except (ValueError, WebDriverException):
            return  # Throws exception if there was problem gathering the logs
        for entry in browser_logs:
            if entry['level'] == 'SEVERE' or entry['level'] == 'WARNING':
                logger.error(str(entry).replace("'level': ", "").split(", 'timestamp':")[0].__add__('}'))
                # full_log = full_log + entry
        # allure.attach(full_log, name="Browser Log", attachment_type=AttachmentType.TEXT)
        # allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def save_cookie_value(self, cookie_key):
        """
        get_cookies() returns a set of dictionaries that contains the cookies of the current page. This function returns
        a specific value of a cookie passed through the cookie_key parameter.
        """
        cookies_dict = {}
        for cookie in self.driver.get_cookies():
            cookies_dict[cookie['name']] = cookie['value']
        logger.info(f'Saving cookies and returning value for {cookie_key}: {cookies_dict.get(cookie_key)}')
        return str(cookies_dict.get(cookie_key))
