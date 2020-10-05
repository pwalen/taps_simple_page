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

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://the-internet.herokuapp.com/key_presses'
driver.get(url)

target = 'target'
target_elem = driver.find_element_by_id(target)


# !!! keys 'ENTER' (Keys.ENTER) and  'RETURN'( Keys.RETURN) result with 'StaleElementReferenceException'
# Message: stale element reference: element is not attached to the page document

special_keys = ['TAB', 'ADD', 'ALT', 'ARROW_DOWN', 'ARROW_LEFT', 'ARROW_RIGHT', 'ARROW_UP', 'BACKSPACE', 'BACK_SPACE', 'CANCEL', 'CLEAR', 'COMMAND', 'CONTROL', 'DECIMAL', 'DELETE', 'DIVIDE', 'DOWN', 'END', 'EQUALS', 'ESCAPE', 'PAGE_DOWN', 'PAGE_UP', 'PAUSE', 'RIGHT', 'SEMICOLON', 'SEPARATOR', 'SHIFT', 'SPACE', 'SUBTRACT', 'UP']
keys_key_list  = [Keys.TAB, Keys.ADD, Keys.ALT, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_UP, Keys.BACKSPACE, Keys.BACK_SPACE, Keys.CANCEL, Keys.CLEAR, Keys.COMMAND, Keys.CONTROL, Keys.DECIMAL, Keys.DELETE, Keys.DIVIDE, Keys.DOWN, Keys.END, Keys.EQUALS, Keys.ESCAPE, Keys.PAGE_DOWN, Keys.PAGE_UP, Keys.PAUSE, Keys.RIGHT, Keys.SEMICOLON, Keys.SEPARATOR, Keys.SHIFT, Keys.SPACE, Keys.SUBTRACT, Keys.UP]

special_keys_verified = []
keys_key_list_verified =[]

for key, keys_key in zip(special_keys, keys_key_list):
    target_elem.send_keys(keys_key)
    result_text = "You entered: " + key
    if result_text in driver.page_source:
        print(key, True, sep=' --> ')
        special_keys_verified.append(key)
        keys_key_list_verified.append(keys_key)
    else:
        print(key, False, sep=' --> ')


sleep(1)
driver.quit()


print(special_keys_verified)
print(keys_key_list_verified)

#!!! second verification FAILED
# urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=58064): Max retries exceeded with url: /session/bec49edfe03314a649001159d32201d1/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fa790a8f550>: Failed to establish a new connection: [Errno 61] Connection refused'))



# driver.get(url)
#
# target = 'target'
# target_elem = driver.find_element_by_id(target)
#
# for key, keys_key in zip(special_keys_verified, keys_key_list_verified):
#     target_elem.send_keys(keys_key)
#     result_text = "You entered: " + key
#     if result_text in driver.page_source:
#         print(key, True, sep=' --> ')
#     else:
#         print(key, False, sep=' --> ')
#
#
# sleep(1)
# driver.quit()