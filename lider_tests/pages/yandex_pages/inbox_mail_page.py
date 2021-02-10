from pages.base_page import BasePage
from locators.yandex_locators import InboxMailPageLocators


class InboxMailPage(BasePage):

    def is_page_opened(self):
        is_inbox_folder_displayed = self.driver.find_element(InboxMailPageLocators.INBOX_ACTIVE_FOLDER).is_displayed()
        is_username_displayed = self.driver.find_element(InboxMailPageLocators.USER_ACCOUNT_LINK).is_displayed()
        return is_inbox_folder_displayed and is_username_displayed
