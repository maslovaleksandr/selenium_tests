import pytest
# from selenium_tests.test_browsers.MY_SITE import MY_SITE
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--b',
        action='store',
        default='chrome',
        help='Chose available browser'
    )
    parser.addoption(
        '--url',
        action='store',
        default="http://192.168.0.102",
        help='Url for tests'
    )


@pytest.fixture
def browser_select(request):
    from selenium.webdriver.common.keys import Keys
    param = request.config.getoption("--b")
    if param == 'chrome':
        wd = webdriver.Chrome()
    elif param == 'firefox':
        wd = webdriver.Firefox()
    else:
        raise Exception("Browser is supported")
    wd.get(request.config.getoption("--url"))
    return wd
