from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

"""
SELECTION OF SPECIAL KEYS for the test

1. I opened the following URL: https://selenium-python.readthedocs.io/api.html?highlight=keys#module-selenium.webdriver.common.keys
2. I scrolled down to Chapter 7.4. Special Keys.
3. I prepared a custom list of special keys, based on the Chapter.
4. Then, I selected only these keys, which after pressing, match the keys displayed.
5. Moreover, I had to exclude the keys 'ENTER' (Keys.ENTER) and 'RETURN'( Keys.RETURN) as they resulted in the following error:
" 'StaleElementReferenceException' # Message: stale element reference: element is not attached to the page document "

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

special_keys = ['TAB', 'ADD', 'ALT', 'ARROW_DOWN', 'ARROW_LEFT', 'ARROW_RIGHT', 'ARROW_UP', 'BACKSPACE', 'BACK_SPACE', 'CANCEL', 'CLEAR', 'COMMAND', 'CONTROL', 'DECIMAL', 'DELETE', 'DIVIDE', 'DOWN', 'END', 'EQUALS', 'ESCAPE', 'PAGE_DOWN', 'PAGE_UP', 'PAUSE', 'RIGHT', 'SEMICOLON', 'SEPARATOR', 'SHIFT', 'SPACE', 'SUBTRACT', 'UP']
keys_special_keys  = [Keys.TAB, Keys.ADD, Keys.ALT, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_UP, Keys.BACKSPACE, Keys.BACK_SPACE, Keys.CANCEL, Keys.CLEAR, Keys.COMMAND, Keys.CONTROL, Keys.DECIMAL, Keys.DELETE, Keys.DIVIDE, Keys.DOWN, Keys.END, Keys.EQUALS, Keys.ESCAPE, Keys.PAGE_DOWN, Keys.PAGE_UP, Keys.PAUSE, Keys.RIGHT, Keys.SEMICOLON, Keys.SEPARATOR, Keys.SHIFT, Keys.SPACE, Keys.SUBTRACT, Keys.UP]


special_keys_selected = []
keys_special_keys_selected =[]

for key, keys_key in zip(special_keys, keys_special_keys):
    target_elem.send_keys(keys_key)
    result_text = "You entered: " + key
    if result_text in driver.page_source:
        special_keys_selected.append(key)
        keys_special_keys_selected.append(keys_key)
    else:
        continue

sleep(1)

"""
TEST 1

The test is considered passed when the list of keys pressed is equal to the list of keys displayed.
"""


special_keys_verified = []
keys_special_keys_verified = []


for key, keys_key in zip(special_keys_selected, keys_special_keys_selected):
    target_elem.send_keys(keys_key)
    result_text = "You entered: " + key
    if result_text in driver.page_source:
        special_keys_verified.append(key)
        keys_special_keys_verified.append(keys_key)
    else:
        continue

if special_keys_verified == special_keys_selected and keys_special_keys_verified == keys_special_keys_selected:
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')

sleep(1)
driver.quit()
