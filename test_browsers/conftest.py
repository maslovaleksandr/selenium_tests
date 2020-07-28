import pytest
from MY_SITE import MY_SITE


def pytest_addoption(parser):
    parser.addoption(
        "--b",
        action='store',
        default='chrome',
        help='Chose browser you want to use. Chrome or FireFox')
    parser.addoption(
        "--url",
        action='store',
        default=MY_SITE,
        help='URL'
    )


@pytest.fixture
def browser_check(request):
    return request.config.getoption("--b")


@pytest.fixture
def url_check(request):
    return request.config.getoption("--url")
