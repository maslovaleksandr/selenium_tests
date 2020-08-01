from ..locators import Menu
from selenium import webdriver


def test_drop_down_menu(browser_select):
    wd = browser_select
    action = webdriver.ActionChains(wd)
    dropdown_elements = wd.find_elements_by_class_name(Menu.Menu.dropdown_toggle)
    for element in dropdown_elements:
        action.move_to_element(element).pause(0.5)
        action.perform()
    wd.quit()

