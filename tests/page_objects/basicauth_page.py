from tests.helpers.support_functions import *

basicauth_tab = 'basicauth-header'
basicauth_content = 'basicauth-content'
username = 'ba_username'
password = 'ba_password'
invalid_credentials = 'loginFormMessage'
login_button = '//*[@id="content"]/button'


def click_basicauth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(basicauth_tab)
    elem.click()

def basicauth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, basicauth_content)
    return elem.is_displayed()

def send_correct_keys_to_basicauth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username, time_to_wait=1)
    elem_username = driver_instance.find_element_by_id(username)
    elem_username.send_keys('admin')
    wait_for_visibility_of_element(driver_instance, password, time_to_wait=1)
    elem_password = driver_instance.find_element_by_id(password)
    elem_password.send_keys('admin')
    wait_for_visibility_of_element_by_xpath(driver_instance, login_button, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(login_button)
    elem.click()

def send_incorrect_keys_to_basicauth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username, time_to_wait=1)
    elem_username = driver_instance.find_element_by_id(username)
    elem_username.send_keys('abcdefgh')
    wait_for_visibility_of_element(driver_instance, password, time_to_wait=1)
    elem_password = driver_instance.find_element_by_id(password)
    elem_password.send_keys('abcdefgh')
    wait_for_visibility_of_element_by_xpath(driver_instance, login_button, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(login_button)
    elem.click()

def invalid_credentials_message_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, invalid_credentials)
    return elem.is_displayed()