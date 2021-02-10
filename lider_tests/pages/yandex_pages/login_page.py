from pages.base_page import BasePage
from locators.yandex_locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(LoginPageLocators.USER_TEXTBOX).send_keys(username)
        self.click_submit_button()
        self.driver.find_element(LoginPageLocators.PASSWORD_TEXTBOX).send_keys(password)
        self.click_submit_button()

    def click_submit_button(self):
        self.driver.find_element(LoginPageLocators.SUBMIT_BUTTON).click()
