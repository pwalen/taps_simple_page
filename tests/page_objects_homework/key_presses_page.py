from tests.helpers.support_functions import *
import string

key_presses_tab = 'keypresses-header'
key_presses_content = 'keypresses-content'
target = 'target'


def click_key_presses_tab(driver_instance):
    elem = driver_instance.find_element_by_id(key_presses_tab)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, key_presses_content)
    return elem.is_displayed()


def press_ascii_letters(driver_instance):
    wait_for_visibility_of_element(driver_instance, target, time_to_wait=1)
    elem = driver_instance.find_element_by_id(target)

    letters_displayed = ''
    for letter in string.ascii_letters:
        elem.send_keys(letter)
        result_text = f"You entered: {letter.upper()}"
        if result_text in driver_instance.page_source:
            letters_displayed += letter.upper()

    if letters_displayed == string.ascii_letters.upper():
        return True
    else:
        return False

