import numpy as np
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome('/home/simonas/Downloads/chromedriver')
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    WebDriverWait(browser, 3).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
    x = float(browser.find_element_by_id("input_value").text)
    answer = str(np.log(abs(12*np.sin(x))))
    answerInput = browser.find_element_by_id("answer")
    answerInput.send_keys(answer)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()