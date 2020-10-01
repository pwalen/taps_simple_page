from tests.helpers.support_functions import *
from time import sleep


date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
picker = 'start'


def date_picker_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()

def date_picker_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker_tab)
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()

# def click_checkboxes(driver_instance):
#     elem = driver_instance.find_element_by_xpath(checkbox_1)
#     elem.click()
#     elem1 = driver_instance.find_element_by_xpath(checkbox_2)
#     elem1.click()
