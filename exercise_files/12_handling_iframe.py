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
The test is considered passed when the 'Button 1 was clicked!' string  displays.

TEST 2
The test is considered passed when the 'Button 2 was clicked!' string  displays.
"""

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

iframe_tab = 'iframe-header'
iframe_content = '//*[@id="iframe-content"]/div/div/iframe'
button1 = 'simpleButton1'
button2 = 'simpleButton2'


iframe_tab_elem = driver.find_element_by_id(iframe_tab)
wait_for_visibility_of_element(driver, iframe_tab, time_to_wait=1)
iframe_tab_elem.click()

WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath(iframe_content)))

button1_elem = driver.find_element_by_id(button1)
wait_for_visibility_of_element(driver, button1, time_to_wait=2)
button1_elem.click()

button1_result_text = 'Button 1 was clicked!'
if button1_result_text in driver.page_source:
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')

sleep(1)

button2_elem = driver.find_element_by_id(button2)
wait_for_visibility_of_element(driver, button2, time_to_wait=2)
button2_elem.click()

button2_result_text = 'Button 2 was clicked!'
if button2_result_text in driver.page_source:
    print('Test 2 is passed')
else:
    print('Test 2 is NOT passed')

sleep(1)
driver.quit()
