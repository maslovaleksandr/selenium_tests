from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--b",
        action = "store",
        default = "chrome",
        help = "Chose your browser"
    )



@pytest.fixture
def browser(request):
    param = request.config.getoption("--b")
    if param == "chrome":
        wd = webdriver.Chrome()
    elif param == "firefox":
        wd = webdriver.Firefox()
    else:
        raise("Browser is not supported")
    wd.implicitly_wait(5)
    return wd
