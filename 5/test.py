import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def fillAndGetValue(browser, selector, value):
    try:
        first_name = browser.find_element_by_css_selector(selector)
        first_name.send_keys(value)
        return first_name.get_attribute("value")
    except NoSuchElementException:
        return ""

class TestClass:
    @pytest.fixture(scope="function", autouse=True)
    def browser(self):
        self.browser = webdriver.Chrome('/home/simonas/Downloads/chromedriver')
        yield self.browser
        self.browser.quit()

    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        first_name = fillAndGetValue(self.browser, ".first_block .first", "test")
        last_name = fillAndGetValue(self.browser, ".first_block .second", "test")
        email = fillAndGetValue(self.browser, ".first_block .third", "test@gmail.com")
        phone_number = fillAndGetValue(self.browser, ".second_block .first", "test")
        address = fillAndGetValue(self.browser, ".second_block .second", "test")
        button = self.browser.find_element_by_tag_name("button")
        button.click()
        congratsText = self.browser.find_element_by_css_selector(".container h1").text
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
        self.browser.get(link)
        first_name = fillAndGetValue(self.browser, ".first_block .first", "test")
        last_name = fillAndGetValue(self.browser, ".first_block .second", "test")
        email = fillAndGetValue(self.browser, ".first_block .third", "test@gmail.com")
        phone_number = fillAndGetValue(self.browser, ".second_block .first", "test")
        address = fillAndGetValue(self.browser, ".second_block .second", "test")
        button = self.browsergt.find_element_by_tag_name("button")
        button.click()
        congratsText = self.browser.find_element_by_css_selector(".container h1").text
        assert (
            first_name == "test" and
            last_name == "test" and
            email == "test@gmail.com" and
            phone_number == "test" and
            address == "test" and
            congratsText == 'Congratulations! You have successfully registered!'
        )
