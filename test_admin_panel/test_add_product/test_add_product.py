from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..locators.LoginPage import LoginPage
from ..locators.ProductsPage import ProductsPage
from ..URL import *
import time


def test_remove_product(browser):
    """Testing adding product. Elements from locators.py
    Description from dict in ProductPage.py"""

    driver = browser
    driver.get(OPENCART_ADMIN)
    try:
        username = driver.find_element(By.CSS_SELECTOR, LoginPage.user_input)
        password = driver.find_element(By.CSS_SELECTOR, LoginPage.password_input)
        username.send_keys(USER)
        password.send_keys(PASSWORD)
        password.submit()
        try:
            catalog = WebDriverWait(driver, 5)\
                .until(EC.presence_of_element_located((By.ID, ProductsPage.Catalog)))
            catalog.click()
            product = WebDriverWait(driver, 5) \
                .until(EC.presence_of_element_located((By.LINK_TEXT, ProductsPage.Product)))
            product.click()
            add_button = WebDriverWait(driver, 5)\
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, ProductsPage.Add_button)))
            add_button.click()
            product_name = driver.find_element(By.CSS_SELECTOR, ProductsPage.Product_name_input)
            product_name.send_keys(ProductsPage.Product_info["Product name"])
            description = driver.find_element(By.CSS_SELECTOR, ProductsPage.Description_input)
            description.send_keys(ProductsPage.Product_info["Description"])
            meta_teg_title = driver.find_element(By.CSS_SELECTOR, ProductsPage.Meta_teg_title_input)
            meta_teg_title.send_keys(ProductsPage.Product_info["Meta teg title"])
            data_page = driver.find_element(By.CSS_SELECTOR, ProductsPage.Data_page)
            data_page.click()
            data = driver.find_element(By.CSS_SELECTOR, ProductsPage.Model_input)
            data.send_keys(ProductsPage.Data["Model"])
            save_button = driver.find_element(By.CSS_SELECTOR, ProductsPage.Save_button)
            save_button.click()
            time.sleep(5)
            driver.quit()
        except NoSuchElementException:
            pass
    except TimeoutException:
        driver.quit()
