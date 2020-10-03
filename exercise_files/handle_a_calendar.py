# import re for reges
import re
import time
from bs4 import BeautifulSoup

# Import webdriver to initialise a browser
from selenium import webdriver
from selenium.webdriver import ActionChains

url = 'http://www.sp336.szkolnastrona.pl/'

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')

driver.get(url)





time.sleep(3)
driver.quit()
