from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from tests.helpers.support_functions import *
from time import sleep

"""
TEST 1

The test is considered passed when the 'Success' popup displays.
"""

driver = webdriver.Chrome('/Users/pawelwalenda/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

form_tab = 'form-header'
form_content = 'form-content'
first_name = 'fname'
last_name = 'lname'
submit_button = 'formSubmitButton'

form_tab_elem = driver.find_element_by_id(form_tab)
form_content_elem = driver.find_element_by_id(form_content)
first_name_elem = driver.find_element_by_id(first_name)
last_name_elem = driver.find_element_by_id(last_name)
submit_button_elem = driver.find_element_by_id(submit_button)

form_tab_elem.click()
wait_for_visibility_of_element(driver, form_content)
wait_for_visibility_of_element(driver, first_name_elem, time_to_wait=1)
first_name_elem.send_keys('nice')
wait_for_visibility_of_element(driver, last_name_elem, time_to_wait=1)
last_name_elem.send_keys('weather')
wait_for_visibility_of_element(driver, submit_button, time_to_wait=1)
submit_button_elem.click()

alert_obj = driver.switch_to.alert.text
print(alert_obj)

if alert_obj == 'success':
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')

sleep(1)
driver.quit()
