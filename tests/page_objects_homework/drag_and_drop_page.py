import os

from tests.helpers.support_functions import *

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'


def click_drag_and_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_and_drop_content)
    return elem.is_displayed()


def drag_and_drop_move_elements(driver_instance):
    with open(os.path.abspath('../helpers/drag_and_drop_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()
    # drag column a and drop on column b
    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")

    # drag column b and drop on column a
    driver_instance.execute_script(script + "jQuery('#column-b').simulateDragDrop({ dropTarget: '#column-a'});")
    return True
