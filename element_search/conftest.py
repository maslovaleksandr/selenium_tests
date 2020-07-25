import pytest


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
        default='http://192.168.0.102',
        help='Url for tests'
    )


@pytest.fixture(params=['chrome','safari','firefox'])
def browser_select(request):
    return request.getoption('--b')


@pytest.fixture
def url_select(request):
    return request.getoption('--url')
