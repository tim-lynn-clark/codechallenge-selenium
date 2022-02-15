
from pytest import mark

from base_case_flows.base_homepage_flow import BaseHomepageFlows
from locators.locators_homepage import header_button
from data_json.json_file_paths import CONTACT_US

contactinfo = CONTACT_US

class HomepageTests(BaseHomepageFlows):

    @mark.sanity
    @mark.e2e
    def test_homepage_links(self):
        self.homepage_about()
        self.homepage_mission()
        self.homepage_latestnews()
        self.homepage_covid_cancercare()
        self.homepage_CRD()

    def test_navigation_links(self):
        self.homepage_check_links_flow(contactinfo)
        self.private_policy()



