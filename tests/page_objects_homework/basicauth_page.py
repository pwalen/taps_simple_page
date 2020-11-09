from tests.helpers.support_functions import *

basicauth_tab = 'basicauth-header'
basicauth_content = "basicauth-content"
username = 'ba_username'
password = 'ba_password'
login_button = '//*[@id="content"]/button'
invalid_credentials = 'loginFormMessage'


def click_basicauth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(basicauth_tab)
    elem.click()


def basicauth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, basicauth_content)
    return elem.is_displayed()


def send_correct_keys_to_basicauth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(username)
    elem1.send_keys('admin')
    wait_for_visibility_of_element(driver_instance, password, time_to_wait=1)
    elem2 = driver_instance.find_element_by_id(password)
    elem2.send_keys('admin')


def send_incorrect_keys_to_basicauth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(username)
    elem1.send_keys('sdsds')
    wait_for_visibility_of_element(driver_instance, password, time_to_wait=1)
    elem2 = driver_instance.find_element_by_id(password)
    elem2.send_keys('uouiu')


def click_login_button(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, login_button)
    elem = driver_instance.find_element_by_xpath(login_button)
    elem.click()


def invalid_credentials_displayed(driver_instance):
    if invalid_credentials in driver_instance.page_source:
        return True
    else:
        return False
