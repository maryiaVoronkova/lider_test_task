from pages.base_page import BasePage
from locators.google_locators import SearchResultPageLocators


class SearchResultPage(BasePage):

    def get_results_count(self):
        adv_result_count = len(self.driver.find_elements(SearchResultPageLocators.ADV_RESULT_LINKS))
        result_count = len(self.driver.find_elements(SearchResultPageLocators.RESULT_LINKS))
        return adv_result_count + result_count

    def is_link_with_url_present(self, url):
        return self.driver.find_element(SearchResultPageLocators.get_link_with_url(url)).is_displayed()
