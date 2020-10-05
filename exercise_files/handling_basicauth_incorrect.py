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

The test is considered passed when the red 'Invalid credentials' string displays beneath the 'Login' button.
"""

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

basicauth_tab = 'basicauth-header'
# basicauth_content = 'basicauth-content'
username = 'ba_username'
password = 'ba_password'

login_button = '//*[@id="content"]/button'

basicauth_tab_elem = driver.find_element_by_id(basicauth_tab)
# basicauth_content_elem = driver.find_element_by_id(basicauth_content)
username_elem = driver.find_element_by_id(username)
password_elem = driver.find_element_by_id(password)
login_button_elem = driver.find_element_by_xpath(login_button)

basicauth_tab_elem.click()
wait_for_visibility_of_element(driver, username, time_to_wait=1)
elem_username = driver.find_element_by_id(username)
elem_username.send_keys('sdsds')
wait_for_visibility_of_element(driver, password, time_to_wait=1)
elem_password = driver.find_element_by_id(password)
elem_password.send_keys('uouiu')
wait_for_visibility_of_element_by_xpath(driver, login_button, time_to_wait=1)
login_button_elem.click()

invalid_credentials_text = 'loginFormMessage'

if invalid_credentials_text in driver.page_source:
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')

sleep(1)
driver.quit()
