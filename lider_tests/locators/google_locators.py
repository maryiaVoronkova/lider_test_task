from selenium.webdriver.common.by import By


class HomePageLocators:
    SEARCH_INPUT = (By.NAME, 'q')


class SearchResultPageLocators:
    ADV_RESULT_LINKS = (By.CLASS_NAME, 'uEierd')
    RESULT_LINKS = (By.CLASS_NAME, 'g')

    @staticmethod
    def get_link_with_url(url):
        result_with_url = (By.XPATH, f"//*[@class='g'][contains(., '{url}')]")
        return result_with_url
