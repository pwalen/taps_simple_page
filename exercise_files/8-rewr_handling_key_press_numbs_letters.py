from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from tests.helpers.support_functions import *
# from selenium.webdriver.common.keys import Keys
from time import sleep
import string

"""
TEST 1

The test is considered passed when the list of keys pressed is equal to the list of keys displayed.
"""

driver = webdriver.Chrome('/Users/pawelwalenda/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

keypresses_tab = 'keypresses-header'
keypresses_content = 'keypresses-content'
target = 'target'

keypresses_tab_elem = driver.find_element_by_id(keypresses_tab)
wait_for_visibility_of_element(driver, keypresses_tab)
keypresses_tab_elem.click()

wait_for_visibility_of_element(driver, keypresses_content)

target_elem = driver.find_element_by_id(target)
wait_for_visibility_of_element(driver, target, time_to_wait=1)

# letters_numbers_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters_displayed = ''

for letter in string.ascii_letters:
    target_elem.send_keys(letter)
    result_text = f"You entered: {letter.upper()}"
    if result_text in driver.page_source:
        letters_displayed += letter.upper()

if letters_displayed == string.ascii_letters.upper():
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')

print(string.ascii_letters)
print(letters_displayed)

sleep(1)
driver.quit()






