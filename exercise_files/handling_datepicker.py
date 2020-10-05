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

The test is considered passed when the entered date displays in the date-picker field.
"""

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

datepicker_tab = 'datepicker-header'
datepicker_content = 'datepicker-content'
datepicker_input = 'start'

datepicker_tab_elem = driver.find_element_by_id(datepicker_tab)
datepicker_input_elem = driver.find_element_by_id(datepicker_input)

wait_for_visibility_of_element(driver, datepicker_tab, time_to_wait=1)
datepicker_tab_elem.click()
wait_for_visibility_of_element(driver, datepicker_content, time_to_wait=1)
wait_for_visibility_of_element(driver, datepicker_input, time_to_wait=1)


_day = '12'
_month = '9'
day_month_entered = _day, _month
datepicker_input_elem.send_keys(day_month_entered)
datepicker_tab_elem.click()


if _day and _month in driver.page_source:
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')

sleep(1)
driver.quit()