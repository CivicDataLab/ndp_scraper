import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import requests
import re

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from variables import *
import urllib.parse
from selenium.webdriver.remote.webelement import WebElement


options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument('disable-infobars')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-gpu')

path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)

site_url = "https://data.gov.in/catalogs?"

driver.get("https://data.gov.in/catalog/answers-data-rajya-sabha-questions-session-255")

WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='btn-preview']")))
buttons = driver.find_elements(By.XPATH, "//a[@class='btn-preview']")
for i in buttons:
    print(i.text)
heading_list = []
for i in buttons:
    driver.execute_script("arguments[0].click();", i)
    heading_list.append(driver.find_element(By.XPATH, "//h5[@class = 'modal-title']").text)
    close_button = driver.find_element(By.XPATH, "//button[@class = 'close']")
    driver.execute_script("arguments[0].click();", close_button)
    time.sleep(10)

#print(driver.page_source)
#print(driver.execute_script("arguments[0].click();", button))
print(heading_list)
# a = ActionChains(driver)
# m= driver.find_element(By.XPATH, "")
# a.move_to_element(m).click()

# driver.execute_script("document.getElementsByClassName('btn-preview')[0].click()")
# print(driver.execute_script("document.getElementsByClassName('btn-preview')[0].click()"))
# print(driver.page_source)
#print(driver.page_source)