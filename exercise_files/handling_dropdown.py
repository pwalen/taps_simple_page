from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from tests.helpers.support_functions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

dropdown_tab = 'dropdownlist-header'
dropdown_content = 'dropdownlist-content'
option_1 = '//*[@id="dropdown"]/option[2]'
option_2 = '//*[@id="dropdown"]/option[3]'
dropdown_selector = 'dropdown'

dropdown_tab_elem = driver.find_element_by_id(dropdown_tab)
dropdown_selector_elem = driver.find_element_by_id(dropdown_selector)


dropdown_tab_elem.click()
wait_for_visibility_of_element(driver, dropdown_selector)

option_1_elem = driver.find_element_by_xpath(option_1)
option_1_elem.click()
sleep(1)
option_2_elem = driver.find_element_by_xpath(option_2)
option_2_elem.click()

sleep(1)
driver.quit()




