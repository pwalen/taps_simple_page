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


driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
url = 'http://simpletestsite.fabrykatestow.pl/'
driver.get(url)

statuscodes_tab = 'statuscodes-header'
statuscodes_content = 'statuscodes-content'
link_200 = '200siteAnchor'
link_305 = '305siteAnchor'
link_404 = '404siteAnchor'
link_500 = '500siteAnchor'

statuscodes_tab_elem = driver.find_element_by_id(statuscodes_tab)
statuscodes_tab_elem.click()

wait_for_visibility_of_element(driver, statuscodes_content)

link_200_elem = driver.find_element_by_id(link_200)
wait_for_visibility_of_element(driver, link_200)
link_200_elem.click()


sleep(3)
driver.quit()