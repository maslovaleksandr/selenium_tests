from selenium import webdriver
import time
import pytest


@pytest.fixture
def test_driver(request):
    wd = webdriver.Chrome()
    wd.get(request)
    time.sleep(2)


