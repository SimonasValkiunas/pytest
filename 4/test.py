import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome('/home/simonas/Downloads/chromedriver')

def fillAndGetValue(browser, selector, value):
    try:
        first_name = browser.find_element_by_css_selector(selector)
        first_name.send_keys(value)
        return first_name.get_attribute("value")
    except NoSuchElementException:
        return ""

class TestClass:
    def test_one(self):
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)
            first_name = fillAndGetValue(browser, ".first_block .first", "test")
            last_name = fillAndGetValue(browser, ".first_block .second", "test")
            email = fillAndGetValue(browser, ".first_block .third", "test@gmail.com")
            phone_number = fillAndGetValue(browser, ".second_block .first", "test")
            address = fillAndGetValue(browser, ".second_block .second", "test")
            button = browser.find_element_by_tag_name("button")
            button.click()
            congratsText = browser.find_element_by_css_selector(".container h1").text
            assert (
                first_name == "test" and
                last_name == "test" and
                email == "test@gmail.com" and
                phone_number == "test" and
                address == "test" and
                congratsText == 'Congratulations! You have successfully registered!'
            )

    def test_two(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)
            first_name = fillAndGetValue(browser, ".first_block .first", "test")
            last_name = fillAndGetValue(browser, ".first_block .second", "test")
            email = fillAndGetValue(browser, ".first_block .third", "test@gmail.com")
            phone_number = fillAndGetValue(browser, ".second_block .first", "test")
            address = fillAndGetValue(browser, ".second_block .second", "test")
            button = browser.find_element_by_tag_name("button")
            button.click()
            congratsText = browser.find_element_by_css_selector(".container h1").text
            assert (
                first_name == "test" and
                last_name == "test" and
                email == "test" and
                phone_number == "test" and
                address == "test" and
                congratsText == 'Congratulations! You have successfully registered!'
            )