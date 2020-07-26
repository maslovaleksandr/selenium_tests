from ..locators.MainPage import MainPage
from selenium.webdriver.common.keys import Keys
import time


def test_swiper(browser_select):
    driver = browser_select
    driver.find_element_by_class_name(MainPage.footer_promo)
    driver.find_element_by_class_name(MainPage.footer_buttons_prev).click()
    driver.quit()


def test_search(browser_select):
    driver = browser_select
    search = driver.find_element_by_name(MainPage.search)
    search.send_keys("iphone")
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.quit()


def test_add_to_cart(browser_select):
    driver = browser_select
    