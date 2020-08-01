from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.Common import Common
from .UserLogin import UserLogin


class DefaultPage:

    def __init__(self, browser):
        self.browser = browser
        self.login = UserLogin(browser)

    def __elements(self, selector: dict, index: int):
        index = index - 1
        selector = selector['css']
        by = By.CSS_SELECTOR
        return self.browser.find_elements(by, selector)[index]

    def _click(self, selector, index=1):
        self.__elements(selector, index).click()

    def _input(self, selector, value, index=0):
        element = self.__elements(selector, index)
        element.clear()
        element.send_keys(value)

    def back_to_main_page(self):
        return self._click(Common.logo, 0)
    
    def _get_text(self, selector, index):
        return self.__elements(selector, index).text

    def is_visible(self, selector, index, timeout = 3):
        return WebDriverWait(self.browser, timeout) \
            .until(EC.invisibility_of_element(self.__elements(selector, index)))
