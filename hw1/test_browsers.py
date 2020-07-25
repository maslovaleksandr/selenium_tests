import selenium.webdriver


def test_browser(browser_check):
    if browser_check == "chrome":
        return selenium.webdriver.Chrome()
    elif browser_check == "firefox":
        return selenium.webdriver.Firefox()
    else:
        print("Wrong param")

