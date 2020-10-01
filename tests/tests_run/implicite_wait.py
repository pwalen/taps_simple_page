from selenium import webdriver

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/taps_simple_page/chromedriver')
driver.implicitly_wait(10)
driver.get('http://simpletestsite.fabrykatestow.pl/')
myDynamicElement = driver.find_element_by_id('checkbox-header')
driver.quit()