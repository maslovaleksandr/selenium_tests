import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--b",
        action='store',
        default='chrome',
        help='Chose browser you want to use. Chrome or FireFox')


@pytest.fixture
def browser_check(request):
    return request.config.getoption("--b")
