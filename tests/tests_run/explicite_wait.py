from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
driver.get('http://simpletestsite.fabrykatestow.pl/')
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'checkbox-header')))
finally:
    driver.quit()