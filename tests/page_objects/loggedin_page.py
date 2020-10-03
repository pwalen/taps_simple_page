from tests.helpers.support_functions import *

loggedin_message = 'loggedInMessage'

def loggedin_message_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, loggedin_message)
    return elem.is_displayed()