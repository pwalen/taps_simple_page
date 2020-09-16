import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))
