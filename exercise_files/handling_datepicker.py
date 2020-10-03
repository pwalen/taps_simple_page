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

datepicker_tab = 'datepicker-header'
datepicker_content = 'datepicker-content'
datepicker_input = 'start'

datepicker_tab_elem = driver.find_element_by_id(datepicker_tab)
datepicker_input_elem = driver.find_element_by_id(datepicker_input)

datepicker_tab_elem.click()
wait_for_visibility_of_element(driver, datepicker_input)

datepicker_input_elem.send_keys('1209')

sleep(1)
driver.quit()