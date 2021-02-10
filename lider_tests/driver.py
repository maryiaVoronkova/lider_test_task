from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver:

    def __init__(self, url):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe",
                                       options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    def find_element(self, locator, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator),
                                                      message=f"Element with locator {locator} is not present")

    def find_elements(self, locator, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Elements with locator {locator} are not present")

    def switch_to_new_tab(self):
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)

    def quit(self):
        self.driver.quit()
