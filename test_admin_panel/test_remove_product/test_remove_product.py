from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..locators.LoginPage import LoginPage
from ..locators.ProductsPage import ProductsPage
from ..URL import *
from selenium.webdriver.common.alert import Alert


def test_remove_product(browser):
    driver = browser
    driver.get(OPENCART_ADMIN)
    try:
        username = driver.find_element(By.CSS_SELECTOR, LoginPage.user_input)
        password = driver.find_element(By.CSS_SELECTOR, LoginPage.password_input)
        username.send_keys(USER)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)
        try:
            catalog = WebDriverWait(driver, 5)\
                .until(EC.presence_of_element_located((By.ID, ProductsPage.Catalog)))
            catalog.click()
            product = WebDriverWait(driver, 5)\
                .until(EC.presence_of_element_located((By.LINK_TEXT, ProductsPage.Product)))
            product.click()
            check_box = WebDriverWait(driver, 5)\
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, ProductsPage.Top_checkbox)))
            check_box.click()
            delete_button = WebDriverWait(driver, 5).\
                until(EC.presence_of_element_located((By.CSS_SELECTOR, ProductsPage.Delete_button)))
            delete_button.click()
            Alert(driver).dismiss()
        except NoSuchElementException:
            driver.quit()
    except TimeoutException:
        driver.quit()





