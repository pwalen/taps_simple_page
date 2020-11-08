from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from tests.helpers.support_functions import *
from time import sleep

driver = webdriver.Chrome('/Users/pawelwalenda/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

draganddrop_tab = 'draganddrop-header'
draganddrop_content = 'draganddrop-content'
column_a = 'column-a'
column_b = 'column-b'

column_a_xpath = '//*[@id="column-a"]'
column_b_xpath = '//*[@id="column-b"]'

click_draganddrop_tab = driver.find_element_by_id(draganddrop_tab)
click_draganddrop_tab.click()

wait_for_visibility_of_element(driver, draganddrop_content)

draggable = driver.find_element(By.XPATH, column_a_xpath)
droppable = driver.find_element(By.XPATH, column_b_xpath)

builder.drag_and_drop()
# ActionChains(driver).drag_and_drop(draggable, droppable).perform()
ActionChains(driver).click_and_hold(draggable)\
    .move_to_element(droppable)\
    .release(draggable)\
    .perform()

sleep(5)
driver.quit()

