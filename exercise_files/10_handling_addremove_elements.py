from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from tests.helpers.support_functions import *
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
from time import sleep

"""
TEST A
We will add fifteen elements.

TEST B
We will remove the fifteen elements previously added.

"""

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

addremoveelements_tab = 'addremoveelements-header'
addremoveelements_content = 'addremoveelements-content'
addelement_button = '//*[@id="addremoveelements-content"]/div/div/button'

addremoveelements_tab_elem = driver.find_element_by_id(addremoveelements_tab)
addremoveelements_tab_elem.click()

wait_for_visibility_of_element(driver, addremoveelements_content)

addelement_button_elem = driver.find_element_by_xpath(addelement_button)
wait_for_visibility_of_element_by_xpath(driver, addelement_button)
for x in range(1, 16):
    addelement_button_elem.click()


for x in range(1, 16):
    try:
        delete_button_xpath = ('//*[@id="elements"]/button[{}]'.format(x))
        wait_for_visibility_of_element_by_xpath(driver, delete_button_xpath)
        delete_button_elem = driver.find_element_by_xpath(delete_button_xpath)
        print('Test A {} is passed'.format(x))
    except NoSuchElementException:
        print('Test A {} is NOT passed'.format(x))
        pass


for x in range(15, 0, -1):
    try:
        delete_button_xpath = ('//*[@id="elements"]/button[{}]'.format(x))
        wait_for_visibility_of_element_by_xpath(driver, delete_button_xpath, time_to_wait=1)
        delete_button_elem = driver.find_element_by_xpath(delete_button_xpath)
        delete_button_elem.click()
        print('Test B {} is passed'.format(x))
    except NoSuchElementException:
        print('Test B {} is NOT passed'.format(x))
        pass


sleep(3)
driver.quit()