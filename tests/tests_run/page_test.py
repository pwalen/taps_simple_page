import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, \
    add_remove_page
from tests.page_objects_homework import dropdown_page_2, add_remove_page_2, datepicker_page, basicauth_page, \
    basicauth_logged_in_page, form_page, key_presses_page, drag_and_drop_page, status_codes_page
from time import sleep

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/pawelwalenda/chromedriver')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

#       ====    H O M E W O R K    ======

    def test10_dropdown_select(self):
        dropdown_page_2.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page_2.dropdown_list_visible(self.driver))
        dropdown_page_2.get_first_dropdown_value(self.driver)
        dropdown_page_2.get_second_dropdown_value(self.driver)

    def test11_add_fifteen_elements(self):
        add_remove_page_2.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page_2.add_remove_content_visible(self.driver))
        add_remove_page_2.add_fifteen_elements(self.driver)

    def test12_delete_fifteen_elements(self):
        add_remove_page_2.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page_2.add_remove_content_visible(self.driver))
        add_remove_page_2.add_fifteen_elements(self.driver)
        add_remove_page_2.delete_fifteen_elements(self.driver)
        self.assertTrue(add_remove_page_2.element_invisible(self.driver))

    def test13_datepicker_visibility(self):
        datepicker_page.click_datepicker_tab(self.driver)
        self.assertTrue(datepicker_page.datepicker_content_visible(self.driver))

    def test14_datepicker_input(self):
        datepicker_page.click_datepicker_tab(self.driver)
        self.assertTrue(datepicker_page.send_keys_to_datepicker_field(self.driver))

    def test15_basicauth_visibility(self):
        basicauth_page.click_basicauth_tab(self.driver)
        self.assertTrue(basicauth_page.basicauth_content_visible(self.driver))

    def test16_basicauth_successful_login(self):
        basicauth_page.click_basicauth_tab(self.driver)
        basicauth_page.send_correct_keys_to_basicauth(self.driver)
        basicauth_page.click_login_button(self.driver)
        self.assertTrue(basicauth_logged_in_page.result_text_displayed(self.driver))

    def test17_basicauth_successful_login_and_return_to_homepage(self):
        basicauth_page.click_basicauth_tab(self.driver)
        basicauth_page.send_correct_keys_to_basicauth(self.driver)
        basicauth_page.click_login_button(self.driver)
        basicauth_logged_in_page.click_return_button(self.driver)
        self.assertTrue(basicauth_logged_in_page.homepage_displayed(self.driver))

    def test18_basicauth_unsuccessful_login(self):
        basicauth_page.click_basicauth_tab(self.driver)
        basicauth_page.send_incorrect_keys_to_basicauth(self.driver)
        basicauth_page.click_login_button(self.driver)
        self.assertTrue(basicauth_page.invalid_credentials_displayed(self.driver))

    def test19_form_visibility(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))

    # The test is considered passed when the 'Success' popup displays.
    def test20_form_successful_submit(self):
        form_page.click_form_tab(self.driver)
        form_page.send_keys_to_first_name(self.driver)
        form_page.send_keys_to_last_name(self.driver)
        form_page.click_submit_button(self.driver)
        self.assertTrue(form_page.success_message_displayed(self.driver))

    # def test21_form_unsuccessful_submit(self):
    #     form_page.click_form_tab(self.driver)
    #     form_page.send_keys_to_first_name(self.driver)
    #     form_page.click_submit_button(self.driver)
    #     self.assertTrue(form_page.warning_message_displayed(self.driver))

    def test22_key_presses_visibility(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visible(self.driver))

    # The test is considered passed when the list of keys pressed is equal to the keys displayed.
    def test23_key_presses_ascii_letters(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.press_ascii_letters((self.driver)))

    # The test is considered passed when the list of keys pressed is equal to the keys displayed.
    def test24_key_presses_digits(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.press_digits((self.driver)))

    # The list of the special keys pressed must be equal to the keys' names displayed.
    def test25_key_presses_special_keys(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.press_special_keys((self.driver)))

    def test26_drag_and_drop_visibility(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visible(self.driver))

    # Drag and Drop from source to destination and vice versa.
    def test27_drag_and_drop_elements_on_page(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_move_elements(self.driver))

    def test28_status_codes_visibility(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))

    def test29_status_code_checking(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue((status_codes_page.status_codes_checking(self.driver)))

if __name__ == '__main__':
    unittest.main()
