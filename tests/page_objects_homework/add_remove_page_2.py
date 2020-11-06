from tests.helpers.support_functions import *

add_remove_element_tab = 'addremoveelements-header'
add_remove_element_content = 'addremoveelements-content'
new_element = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = 'added-manually'

def click_add_remove_tab(driver_instance):
    elem = driver_instance.find_element_by_id(add_remove_element_tab)
    elem.click()


def add_remove_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, add_remove_element_content)
    return elem.is_displayed()


def add_fifteen_elements(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, new_element)
    elem = driver_instance.find_element_by_xpath(new_element)
    for _i in range(1, 16):
        elem.click()


def delete_fifteen_elements(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, new_element)
    for _x in range(15, 0, -1):
        added_element = ('//*[@id="elements"]/button[{}]'.format(_x))
        wait_for_visibility_of_element_by_xpath(driver_instance, added_element)
        elem = driver_instance.find_element_by_xpath(added_element)
        elem.click()

def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_elements_by_class_name(driver_instance, added_element)
        return True
    except NoSuchElementException:
        return False