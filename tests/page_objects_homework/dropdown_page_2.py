from tests.helpers.support_functions import *

dropdown_tab = 'dropdownlist-header'
dropdown_content = 'dropdownlist-content'
dropdown_list = 'dropdown'
option_1 = '//*[@id="dropdown"]/option[2]'
option_2 = '//*[@id="dropdown"]/option[3]'


def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element_by_id(dropdown_tab)
    elem.click()


def dropdown_list_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, dropdown_list)
    return elem.is_displayed()


def get_first_dropdown_value(driver_instance):
    elem = driver_instance.find_element_by_xpath(option_1)
    elem.click()
    if 'Option 1' in driver_instance.page_source:
        return True
    else:
        return False


def get_second_dropdown_value(driver_instance):
    elem = driver_instance.find_element_by_xpath(option_2)
    elem.click()
    if 'Option 2' in driver_instance.page_source:
        return True
    else:
        return False
