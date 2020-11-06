from tests.helpers.support_functions import *

result_text = 'You are logged in!'
return_button = 'retrun button'
homepage = 'http://simpletestsite.fabrykatestow.pl/index.html'


def result_text_displayed(driver_instance):
    if result_text in driver_instance.page_source:
        return True
    else:
        return False


def click_return_button(driver_instance):
    wait_for_visibility_of_element(driver_instance, return_button)
    elem = driver_instance.find_element_by_id(return_button)
    elem.click()


def homepage_displayed(driver_instance):
    if driver_instance.current_url == homepage:
        return True
    else:
        return False