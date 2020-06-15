 
import numpy as np
from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome('/home/simonas/Downloads/chromedriver')
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    x = float(browser.find_element_by_id("input_value").text)
    answer = str(np.log(abs(12*np.sin(x))))
    answerInput = browser.find_element_by_id("answer")
    answerInput.send_keys(answer)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()