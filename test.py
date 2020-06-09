import numpy as np
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('/Users/simonas/Desktop/chromedriver')
browser.get('http://suninjuly.github.io/explicit_wait2.html')
time.sleep(2)

price = WebDriverWait(browser,5).until(
    EC.text_to_be_present_in_element((By.ID,"price"),"100")
)


#price_el = browser.find_element_by_id('price')
#print(price_el.text)

#browser.find_element_by_id("price")
browser.quit()
