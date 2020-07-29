from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def test_drag_n_drop(browser):
    driver = browser
    driver.get("https://marcojakob.github.io/dart-dnd/basic/")
    elements = driver.find_elements(By.CLASS_NAME, "document")
    trash = driver.find_element(By.CSS_SELECTOR, ".trash")
    AC = ActionChains(driver)
    for element in range(len(elements)):
        AC.drag_and_drop(elements[element], trash)
    AC.perform()
