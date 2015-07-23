from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://localhost:5000/test_page")
assert "EP 2015" in driver.title
elem = driver.find_element_by_name("my_input")
elem.send_keys("coconut")
elem.send_keys(Keys.RETURN)
assert "coconut" in driver.page_source
driver.close()
