from tests.helpers.support_functions import *

datepicker_tab = 'datepicker-header'
datepicker_content = 'datepicker-content'
datepicker_field = 'start'


def datepicker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, datepicker_content)
    return elem.is_displayed()


def click_datepicker_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_tab)
    elem = driver_instance.find_element_by_id(datepicker_tab)
    elem.click()


def send_keys_to_datepicker_field(driver_instance):
    wait_for_visibility_of_element(driver_instance, datepicker_field, time_to_wait=1)
    elem = driver_instance.find_element_by_id(datepicker_field)
    _day = '12'
    _month = '9'
    elem.send_keys(_day, _month)
    if _day and _month in driver_instance.page_source:
        return True
    else:
        return False
