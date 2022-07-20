from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import requests
import re
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

driver.get("https://data.gov.in/catalog/coverage-anganwadis-tap-connection-under-jal-jeevan-mission-jjm")

card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']")

a = ActionChains(driver)
m= driver.find_element(By.XPATH, "//div[@class='card-header']/span")
a.move_to_element(m)
print(driver.page_source)