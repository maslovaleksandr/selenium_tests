from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions


def test_browser(browser_check, url_check):
    if browser_check == "chrome":
        options = ChromeOptions()
        options.add_argument("--kiosk")
        wd = webdriver.Chrome(chrome_options=options)
        wd.get(url_check)
        wd.quit()
    elif browser_check == "firefox":
        options = FirefoxOptions()
        options.add_argument("--kiosk")
        wd = webdriver.Firefox(firefox_options=options)
        wd.get(url_check)
        wd.quit()
    else:
        raise Exception("Wrong browser parameter")

