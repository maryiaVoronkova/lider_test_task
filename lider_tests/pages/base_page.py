from driver import Driver


class BasePage:

    def __init__(self, driver: Driver):
        self.driver = driver
