import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--b",
        action="store",
        default="firefox",
        help="Chose your browser"
    )
    parser.addoption(
        "--url",
        action="store",
        default="http://192.168.0.102",
        help="Insert yout URL"
    )


@pytest.fixture
def browser(request):
    param = request.config.getoption("--b")
    if param == "chrome":
        wd = webdriver.Chrome()
    elif param == "firefox":
        wd = webdriver.Firefox()
    else:
        raise ("Browser is not supported")
    wd.implicitly_wait(5)
    wd.get(request.config.getoption("--url"))
    return wd
