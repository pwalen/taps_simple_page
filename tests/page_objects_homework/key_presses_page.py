import string

from selenium.webdriver.common.keys import Keys

from tests.helpers.support_functions import *

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


def press_digits(driver_instance):
    wait_for_visibility_of_element(driver_instance, target, time_to_wait=1)
    elem = driver_instance.find_element_by_id(target)

    letters_displayed = ''
    for digit in string.digits:
        elem.send_keys(digit)
        result_text = f"You entered: {digit}"
        if result_text in driver_instance.page_source:
            letters_displayed += digit

    if letters_displayed == string.digits:
        return True
    else:
        return False


"""
Selection of SPECIAL KEYS for the test - steps:

1. I opened the following URL: https://selenium-python.readthedocs.io/api.html?highlight=keys#module-selenium.webdriver.common.keys
2. I scrolled down to Chapter 7.4. Special Keys.
3. Based on the Chapter, I selected keys matching my computer keyboard.
4. Then, I created the list of the keys names as a list of strings ['TAB', 'ADD' ...etc.] -> 'special_keys_by_names'
5. Next, I manually converted this list to be ready to loop through it and use its elements in the "send_keys()" method -> 'special_keys_by_implementations'

"""

special_keys_by_names = ['TAB', 'ADD', 'ALT', 'BACK_SPACE', 'CANCEL', 'CLEAR', 'CONTROL', 'DECIMAL', 'DELETE', 'DIVIDE',
                         'DOWN', 'END', 'ESCAPE', 'PAGE_DOWN', 'PAGE_UP', 'PAUSE', 'RIGHT', 'SHIFT', 'SPACE',
                         'SUBTRACT', 'UP']
special_keys_by_implementations = [Keys.TAB, Keys.ADD, Keys.ALT, Keys.BACK_SPACE, Keys.CANCEL, Keys.CLEAR, Keys.CONTROL,
                                   Keys.DECIMAL, Keys.DELETE, Keys.DIVIDE, Keys.DOWN, Keys.END, Keys.ESCAPE,
                                   Keys.PAGE_DOWN, Keys.PAGE_UP, Keys.PAUSE, Keys.RIGHT, Keys.SHIFT, Keys.SPACE,
                                   Keys.SUBTRACT, Keys.UP]


def press_special_keys(driver_instance):
    wait_for_visibility_of_element(driver_instance, target, time_to_wait=1)
    elem = driver_instance.find_element_by_id(target)
    special_keys_by_names_appended = []
    special_keys_by_implementations_appended = []
    for key_by_name, key_by_implementation in zip(special_keys_by_names, special_keys_by_implementations):
        elem.send_keys(key_by_implementation)
        result_text = f"You entered: {key_by_name}"
        if result_text in driver_instance.page_source:
            special_keys_by_names_appended.append(key_by_name)
            special_keys_by_implementations_appended.append(key_by_implementation)
    if special_keys_by_names_appended == special_keys_by_names and special_keys_by_implementations_appended == special_keys_by_implementations:
        return True
    else:
        return False
