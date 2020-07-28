from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..locators.LoginPage import LoginPage
from ..locators.ProductsPage import ProductsPage
from ..URL import *
import time


def test_modify_product(browser):
    driver = browser
    driver.get(OPENCART_ADMIN)
    try:
        username = driver.find_element(By.CSS_SELECTOR, LoginPage.user_input)
        password = driver.find_element(By.CSS_SELECTOR, LoginPage.password_input)
        username.send_keys(USER)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)
        catalog = WebDriverWait(driver, 5) \
            .until(EC.presence_of_element_located((By.ID, ProductsPage.Catalog)))
        catalog.click()
        product = WebDriverWait(driver, 5) \
            .until(EC.presence_of_element_located((By.LINK_TEXT, ProductsPage.Product)))
        product.click()
        modify_button = driver.find_element(By.CSS_SELECTOR, ProductsPage.Modify_button)
        modify_button.click()
        description = driver.find_element(By.CSS_SELECTOR, ProductsPage.Description_input)
        description.clear()
        description.send_keys("THIS IS NEW DESCRIPTION FROM SELENIUM!!!")
        save_button = driver.find_element(By.CSS_SELECTOR, ProductsPage.Save_button)
        save_button.click()
    except NoSuchElementException:
        driver.quit()
