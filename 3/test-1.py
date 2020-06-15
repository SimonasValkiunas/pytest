import numpy as np
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome('/home/simonas/Downloads/chromedriver')
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    time.sleep(2)
    price = WebDriverWait(browser,30).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"100")
    )

    button = browser.find_element_by_id("book")
    button.click()
    x = float(browser.find_element_by_id("input_value").text)
    equation = str(np.log(abs(12*np.sin(x))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(equation)
    button = browser.find_element_by_id("solve")
    button.click()
    print("Test succesfull")
except:
    print("Test failed")
finally:
    print("Test over")
browser.quit()
