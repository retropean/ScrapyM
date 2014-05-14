from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://www.boltbus.com")
#assert "Python" in driver.title
elem = driver.find_element_by_name("ctl00$cphM$forwardRouteUC$lstRegion$textBox")
elem.click()
elem = driver.find_element_by_id("ctl00_cphM_forwardRouteUC_lstRegion_repeater_ctl00_link")
elem.click()
time.sleep(2.5)
elem = driver.find_element_by_id("ctl00_cphM_forwardRouteUC_lstOrigin_textBox")
elem.click()
elem = driver.find_element_by_id("ctl00_cphM_forwardRouteUC_lstOrigin_repeater_ctl00_link")
elem.click()
time.sleep(2.5)
elem = driver.find_element_by_id("ctl00_cphM_forwardRouteUC_lstDestination_textBox")
elem.click()
elem = driver.find_element_by_id("ctl00_cphM_forwardRouteUC_lstDestination_repeater_ctl00_link")
elem.click()
time.sleep(2.5)

#elem.send_keys("selenium")
#elem.send_keys(Keys.RETURN)
#driver.close()