from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://the-internet.herokuapp.com/key_presses'
driver.get(url)

target = 'target'


target_elem = driver.find_element_by_id(target)

letters_numbers_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for sign in letters_numbers_list:
    target_elem.send_keys(sign)
    result_text = "You entered: " + sign
    if (result_text in driver.page_source):
        print(sign)
    else:
        print(False)

sleep(1)
driver.quit()




