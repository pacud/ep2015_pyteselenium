# coding:utf8
from selenium.webdriver.common.keys import Keys
from fixture import browser


def test_title(browser):
    assert 'EP 2015' in browser.title


def test_title_fail(browser):
    assert 'NOT MY TITLE' in browser.title


def test_login(browser):
    field = browser.find_element_by_name('my_input')
    field.send_keys("coconut")
    field.send_keys(Keys.RETURN)
    assert "coconut" in browser.page_source


def test_link(browser):
    link = browser.find_element_by_name('my_link')
    link.click()
    assert "numberly" in browser.page_source
