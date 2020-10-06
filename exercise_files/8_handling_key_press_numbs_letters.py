from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from tests.helpers.support_functions import *
# from selenium.webdriver.common.keys import Keys
from time import sleep

"""
TEST 1

The test is considered passed when the list of keys pressed is equal to the list of keys displayed.
"""

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

keypresses_tab = 'keypresses-header'
keypresses_content = 'keypresses-content'
target = 'target'

keypresses_tab_elem = driver.find_element_by_id(keypresses_tab)
wait_for_visibility_of_element(driver, keypresses_tab, time_to_wait=2)
keypresses_tab_elem.click()

wait_for_visibility_of_element(driver, keypresses_content, time_to_wait=2)

target_elem = driver.find_element_by_id(target)
wait_for_visibility_of_element(driver, target, time_to_wait=2)

letters_numbers_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters_numbers_list_verified = []

for sign in letters_numbers_list:
    target_elem.send_keys(sign)
    result_text = "You entered: " + sign
    if (result_text in driver.page_source):
        letters_numbers_list_verified.append(sign)
    else:
        print(False)

if (letters_numbers_list_verified  == letters_numbers_list):
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')

sleep(1)
driver.quit()




