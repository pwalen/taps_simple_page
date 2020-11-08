from tests.helpers.support_functions import *
import requests

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'

status_codes_elements_id = ['200siteAnchor', '305siteAnchor','404siteAnchor','500siteAnchor']
codes = [200, 305, 404, 500]


def click_status_codes_tab(driver_instance):
    elem = driver_instance.find_element_by_id(status_codes_tab)
    elem.click()


def status_codes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, status_codes_content)
    return elem.is_displayed()


def status_codes_checking(driver_instance):
    codes_appended = []
    for element_id in status_codes_elements_id:
        elem = driver_instance.find_element_by_id(element_id)
        url = elem.get_attribute("href")
        x = requests.get(url)
        status_code = x.status_code
        codes_appended.append(status_code)
    if codes_appended == codes:
        return True
    else:
        return False