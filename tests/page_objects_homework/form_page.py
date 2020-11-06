from tests.helpers.support_functions import *

form_tab = 'form-header'
form_content = 'form-content'
first_name = 'fname'
last_name = 'lname'
submit_button = 'formSubmitButton'
success_message = 'success'
warning_message = 'Please fill in this field.'


def click_form_tab(driver_instance):
    elem = driver_instance.find_element_by_id(form_tab)
    elem.click()


def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()


def send_keys_to_first_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(first_name)
    elem1.send_keys('nice')


def send_keys_to_last_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, last_name, time_to_wait=1)
    elem1 = driver_instance.find_element_by_id(last_name)
    elem1.send_keys('weather')


def click_submit_button(driver_instance):
    wait_for_visibility_of_element(driver_instance, submit_button)
    elem = driver_instance.find_element_by_id(submit_button)
    elem.click()


def success_message_displayed(driver_instance):
    if driver_instance.switch_to.alert.text == success_message:
        return True
    else:
        return False


def warning_message_displayed(driver_instance):
    if driver_instance.switch_to.alert.text == warning_message:
        return True
    else:
        return False