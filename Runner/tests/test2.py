import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def run():
    chromedriver = "/home/matt/Dokumenty/eclipse_workspace/SeleniumP/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("http://google.com")
    actions = ActionChains(driver)
    
    time.sleep(3)
    actions.send_keys('Matej je nej!!!')
    actions.perform()
    driver.find_element_by_id("_fZl").click()
    time.sleep(3)
    driver.quit()
    