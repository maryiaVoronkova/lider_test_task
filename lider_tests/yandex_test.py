import unittest

from driver import Driver
from data.yandex_data import *
from pages.yandex_pages.home_page import HomePage
from pages.yandex_pages.login_page import LoginPage
from pages.yandex_pages.inbox_mail_page import InboxMailPage


class YandexTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver(URL)
        self.home_page = HomePage(self.driver)

    def test_login(self):
        self.home_page.click_login_button()
        self.driver.switch_to_new_tab()
        login_page = LoginPage(self.driver)
        login_page.login(USERNAME, PASSWORD)

        inbox_mail_page = InboxMailPage(self.driver)
        assert inbox_mail_page.is_page_opened(), 'Inbox Mail page is not displayed or a user is not logged in'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
