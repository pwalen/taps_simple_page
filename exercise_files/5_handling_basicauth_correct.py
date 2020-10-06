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

The test is considered passed when the page titled "You are logged in!" displays.
"""

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

basicauth_tab = 'basicauth-header'
username = 'ba_username'
password = 'ba_password'

login_button = '//*[@id="content"]/button'

basicauth_tab_elem = driver.find_element_by_id(basicauth_tab)
username_elem = driver.find_element_by_id(username)
password_elem = driver.find_element_by_id(password)
login_button_elem = driver.find_element_by_xpath(login_button)

basicauth_tab_elem.click()
wait_for_visibility_of_element(driver, username, time_to_wait=1)
elem_username = driver.find_element_by_id(username)
elem_username.send_keys('admin')
wait_for_visibility_of_element(driver, password, time_to_wait=1)
elem_password = driver.find_element_by_id(password)
elem_password.send_keys('admin')
wait_for_visibility_of_element_by_xpath(driver, login_button, time_to_wait=1)
login_button_elem.click()

result_text = 'You are logged in!'
if result_text in driver.page_source:
    print('Test 1 is passed')
else:
    print('Test 1 is NOT passed')


"""
TEST 2

The user is taken to the homepage after clicking the button titled "Return to main page." 
Then the test is passed.
"""


return_button = 'retrun button'
return_button_elem = driver.find_element_by_id(return_button)

wait_for_visibility_of_element_by_xpath(driver, login_button, time_to_wait=1)
return_button_elem.click()

return_page_url = (driver.current_url)
home_page_url = 'http://simpletestsite.fabrykatestow.pl/index.html'

if return_page_url == home_page_url:
    print('Test 2 is passed')
else:
    print('Test 2 is NOT passed')

sleep(1)
driver.quit()
