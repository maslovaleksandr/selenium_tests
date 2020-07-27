from ..locators.ProductPage import ProductPage


def test_add_to_cart(browser_select):
    driver = browser_select
    product_link = driver.find_element_by_link_text("iPhone")
    product_link.click()
    driver.find_element_by_id(ProductPage.add_to_cart).click()
    driver.quit()


def test_open_photo(browser_select):
    driver = browser_select
    driver.find_element_by_link_text("iPhone").click()
    driver.find_element_by_xpath(ProductPage.photo).click()
    driver.find_element_by_xpath(ProductPage.full_screen_photo_button).click()
    driver.quit()
