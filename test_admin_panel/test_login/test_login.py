from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from ..locators.LoginPage import LoginPage
from ..URL import *
import time


def test_login(browser):
    driver = browser
    driver.get(OPENCART_ADMIN)
    try:
        login = WebDriverWait(driver, 3).\
            until(EC.presence_of_element_located((By.CSS_SELECTOR, LoginPage.user_input)))
        password = WebDriverWait(driver, 3).\
            until(EC.presence_of_element_located((By.CSS_SELECTOR, LoginPage.password_input)))
        login.send_keys(USER)
        password.send_keys(PASSWORD)
        password.submit()
        time.sleep(5)
        driver.quit()
    except TimeoutException:
        driver.quit()
