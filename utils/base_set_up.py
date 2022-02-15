import os

from base_case_flows.base_magento_agent_flows import BaseMagentoAgentFlows
from utils.aws import update_ssm_parameter, get_list_of_s3_objects, delete_s3_object
from utils.log import logger
from utils.utilities import SeleniumUtilities

AWS_REGION = "us-east-2"
AWS_PROFILE = os.environ["AWS_PROFILE"]


class BaseSetUp(BaseMagentoAgentFlows, SeleniumUtilities):
    """
    The BaseSetUp class is required to be added as a parameter to tests case classes for the custom setUp to start.
    setUp is using PYTEST_CURRENT_TEST to get the current tests and apply the setUp depending on the tests running.
    """

    def setUp(self, masterqa_mode=False):

        logger.info('~~~~~~~~~~SETUP START~~~~~~~~~~')

        if AWS_PROFILE != 'credo-qa' and AWS_PROFILE != 'credo-dev' and AWS_PROFILE != 'credo-prod':
            raise ValueError('Missing or invalid environment variable for AWS_PROFILE.')
        if AWS_REGION != 'us-east-2':
            raise ValueError('Missing or invalid environment variable for AWS_REGION.')

        """
        Doing setUps with driver is gnarly. If we do Selenium code inside the setUp, the tests will try to use that
        same driver to do the tests, causing situations the tests might encounter get(x) =/= x and throw an exception.
        To circumvent that, the driver will quit after doing Selenium code and start up a new driver. Horrible.
        """

        super(BaseSetUp, self).setUp()
        current_test = str(os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])
        if 'hotlead' in current_test:
            self.hotlead_setup()
        if 'byod' in current_test:
            self.byod_setup()
        if 'email_confirmation' in current_test:
            self.email_setup()

        logger.info('~~~~~~~~~~SETUP END~~~~~~~~~~')

    def byod_setup(self):
        self.agent_change_captcha_value(100)
        self.driver.quit()
        self.get_new_driver()
        update_ssm_parameter('verizonintegration', '/verizonintegration/config/api/baseurl',
                             'https://internal.credoqa.dev/mock/verizon')

    @staticmethod
    def hotlead_setup():
        update_ssm_parameter('sca', '/sca/activitygraph/minutesback_to_end_of_window', '1')

    @staticmethod
    def email_setup():
        list_of_emails = get_list_of_s3_objects('qais-tests-bucket', 'email/inbound')
        if list_of_emails is not None:
            for s3_objects in list_of_emails['Contents']:
                list_of_keys = [s3_objects['Key']]
                for key in list_of_keys:
                    delete_s3_object('qais-tests-bucket', key)
