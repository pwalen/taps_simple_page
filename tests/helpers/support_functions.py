from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element(driver_instance, xpath):
    elem = driver_instance.find_element_by_xpath(xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def wait_for_visibility_of_element(driver_instance, id, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


# I added here a support function for 'xpath' :
def wait_for_visibility_of_element_by_xpath(driver_instance, xpath, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element(inv_driver_instance, id, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.ID, id)))
    return inv_elem


def wait_for_invisibility_of_element_by_xpath(inv_driver_instance, xpath, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(
        EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_elem


def wait_for_element_to_be_clickable(drive_instance, id, time_to_wait=8):
    elem = WebDriverWait(drive_instance, time_to_wait).until(EC.element_to_be_clickable((By.ID)))
    return elem


# I added here a support function for 'class_name' :
def wait_for_invisibility_of_elements_by_class_name(inv_driver_instance, class_name, time_to_wait=10):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, class_name)))
    return inv_elem

