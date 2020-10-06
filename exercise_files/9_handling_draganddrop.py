from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from tests.helpers.support_functions import *
from time import sleep

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

draganddrop_tab = 'draganddrop-header'
draganddrop_content = 'draganddrop-content'
square_a = 'column-a'
square_b = 'column-b'


draganddrop_tab_elem = driver.find_element_by_id(draganddrop_tab)
wait_for_visibility_of_element(driver, draganddrop_tab, time_to_wait=1)
draganddrop_tab_elem.click()

wait_for_visibility_of_element(driver, draganddrop_content, time_to_wait=1)

square_a_elem = driver.find_element_by_id(square_a)
square_b_elem = driver.find_element_by_id(square_b)

action = webdriver.ActionChains(driver)

action.click_and_hold(square_a_elem).move_by_offset(154, 0).perform()

print(square_a_elem.size)
print(square_a_elem.location)

print(square_b_elem.size)
print(square_b_elem.location)


sleep(3)
driver.quit()

