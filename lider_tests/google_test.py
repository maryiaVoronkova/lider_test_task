import unittest

from driver import Driver
from data.google_data import *
from pages.google_pages.home_page import HomePage
from pages.google_pages.search_result_page import SearchResultPage


class GoogleTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver(URL)
        self.home_page = HomePage(self.driver)

    def test_search_coffee_machine(self):
        expected_results_count = 10
        expected_search_url = 'www.mvideo.ru'

        self.home_page.enter_search_request(SEARCH_MESSAGE)

        search_result_page = SearchResultPage(self.driver)
        actual_results_count = search_result_page.get_results_count()

        assert actual_results_count > expected_results_count, \
            f"Search results count is less than {expected_results_count}"
        assert search_result_page.is_link_with_url_present(expected_search_url),\
            f"Search result with url {expected_search_url} is not displayed"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
