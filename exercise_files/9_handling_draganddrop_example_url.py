import subprocess
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

# JQuery Example

driver = webdriver.Chrome('/Users/pawelwalenda/chromedriver')
driver.get('http://jqueryui.com/resources/demos/sortable/connect-lists.html')
draggable = driver.find_element(By.XPATH, '//*[@id="sortable1"]/li[1]')
droppable = driver.find_element(By.XPATH, '//*[@id="sortable2"]/li[1]')

# Option 1
ActionChains(driver).drag_and_drop(draggable, droppable).perform()

draggable2 = driver.find_element(By.XPATH, '//*[@id="sortable1"]/li[1]')
# Option 2

sleep(2)
ActionChains(driver).click_and_hold(draggable2)\
    .move_to_element(droppable)\
    .release(draggable2)\
    .perform()


