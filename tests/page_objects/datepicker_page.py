from tests.helpers.support_functions import *
from time import sleep


date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
picker = 'start'


def date_picker_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()

def click_date_picker_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker_tab)
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()

# def click_date(driver_instance):
#     wait_for_visibility_of_element(driver_instance, picker)
#     elem = driver_instance.find_element_by_id(picker)
#     elem.click()

def send_correct_keys_to_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, picker, time_to_wait=1)
    elem = driver_instance.find_element_by_id(picker)
    elem.send_keys('0808')
    value = '0808'
    if value == elem.get_attribute('value'):
        return True
    else:
        return False
