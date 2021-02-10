from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.google_locators import HomePageLocators


class HomePage(BasePage):

    def enter_search_request(self, message):
        search_input = self.driver.find_element(HomePageLocators.SEARCH_INPUT)
        search_input.send_keys(message)
        search_input.send_keys(Keys.ENTER)
