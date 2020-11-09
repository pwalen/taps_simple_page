from tests.helpers.support_functions import *

iframe_tab = 'iframe-header'
iframe_content = '//*[@id="iframe-content"]/div/div/iframe'
button_1 = 'simpleButton1'
button_2 = 'simpleButton2'


def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()


def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, iframe_content)
    return elem.is_displayed()


def click_button_1(driver_instance):
    WebDriverWait(driver_instance, 10).until(
        EC.frame_to_be_available_and_switch_to_it(driver_instance.find_element_by_xpath(iframe_content)))
    elem = wait_for_visibility_of_element(driver_instance, button_1)
    elem.click()
    result_text = 'Button 1 was clicked!'
    if result_text in driver_instance.page_source:
        return True
    else:
        return False


def click_button_2(driver_instance):
    WebDriverWait(driver_instance, 10).until(
        EC.frame_to_be_available_and_switch_to_it(driver_instance.find_element_by_xpath(iframe_content)))
    elem = wait_for_visibility_of_element(driver_instance, button_2)
    elem.click()
    result_text = 'Button 2 was clicked!'
    if result_text in driver_instance.page_source:
        return True
    else:
        return False
