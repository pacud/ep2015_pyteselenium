# conftest.py

import pytest
from selenium import webdriver


@pytest.yield_fixture
def browser(request):
    driver = webdriver.Firefox()
    driver.get('http://localhost:5000/test_page')
    yield driver
    driver.quit()
