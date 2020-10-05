from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
from exercise_files.handling_key_press_special_keys import *

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://the-internet.herokuapp.com/key_presses'
driver.get(url)

target = 'target'
target_elem = driver.find_element_by_id(target)



_special_keys_verified = special_keys_verified
_keys_key_list_verified = keys_key_list_verified


for key, keys_key in zip(special_keys_verified, keys_key_list_verified):
    target_elem.send_keys(keys_key)
    result_text = "You entered: " + key
    if result_text in driver.page_source:
        print(key, True, sep=' --> ')
    else:
        print(key, False, sep=' --> ')


sleep(1)
driver.quit()