from ..locators.MainPage import MainPage
from selenium.webdriver.common.keys import Keys
import time


def test_swiper(browser_select):
    driver = browser_select
    driver.find_element_by_class_name(MainPage.footer_promo)
    driver.quit()


def test_search(browser_select):
    driver = browser_select
    search = driver.find_element_by_name(MainPage.search)
    search.send_keys("iphone")
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.quit()
