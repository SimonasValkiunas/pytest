from selenium import webdriver
import time
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome('/home/simonas/Downloads/chromedriver')
    browser.get(link)
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Test")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Test")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Test")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Test")
    button = browser.find_element_by_id("submit_button")
    button.click()
    h1 = find_element_by_css_selector("h1").text
    print(h1)

finally:
    time.sleep(3)
    browser.quit()