from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[class*='login-enter']")


class LoginPageLocators:
    USER_TEXTBOX = (By.NAME, "login")
    PASSWORD_TEXTBOX = (By.NAME, "passwd")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "*[type='submit']")


class InboxMailPageLocators:
    INBOX_ACTIVE_FOLDER = (By.XPATH, "//a[contains(@class, 'inbox') and contains(@class, 'current')]")
    USER_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[class*='user-account_left-name']")
