from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import Common


class DefaultPage:

    def __init__(self, browser):
        self.browser = browser
    
    def __elements(self, selector: dict, index: int):
        by = None
        selector = selector['css']
        by = By.CSS_SELECTOR
        return self.browser.find_element(by, selector)[index]

    def __click(self, selector, index):
        return AC(self.browser).move_to_element(self.__elements(selector, index)) \
            .click().perform()

    def __input(self, selector, index, value):
        elemenet = self.__elements(selector, index)
        elemenet.clear()
        elemenet.send_keys(value)

    def back_to_main_page(self, selector, index):
        return self.__click(Common.logo, 0)
    
    def _get_text(self, selector, index):
        return self.__elements(selector, index).text

    def is_visible(self, selector, index, timeout = 3):
        return WebDriverWait(self.browser, timeout) \
            .until(EC.invisibility_of_element(self.__elements(selector, index)))
