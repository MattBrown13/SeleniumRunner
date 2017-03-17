import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import platform

def run(logger):
    logger.error("Start driver")
    if (platform.system() == "Windows"):
        chromedriver = sys.path[0] + "\chromedriverWindows"
    else:
        chromedriver = sys.path[0] + "\chromedriverLinux"

    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("http://google.com")
    actions = ActionChains(driver)
    logger.error("Driver is succesfully started")
    
    logger.step("One")
    logger.step("Two")
    logger.step("Three")
    
    time.sleep(3)
    actions.send_keys('miluju Petuldu')
    actions.perform()
    driver.find_element_by_id("_fZl").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(text(),'jste na mysli:')]/following-sibling::*").click()
    time.sleep(3)
    driver.quit()
'''    driver.
    driver.find_element_by_name("btnK").click()
    driver.quit()'''
#    browser = webdriver.Firefox()
#    browser.get('http://google.com')
    