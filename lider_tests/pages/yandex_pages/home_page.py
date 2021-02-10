from pages.base_page import BasePage
from locators.yandex_locators import HomePageLocators


class HomePage(BasePage):

    def click_login_button(self):
        self.driver.find_element(HomePageLocators.LOGIN_BUTTON).click()
