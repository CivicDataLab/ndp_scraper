""" All rough scripts here.. """

import logging
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import requests
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_loading(driver_instance: WebDriver, xpath: str, delay=3):
    if delay == 3:
        print("new delay is : ", delay)
    WebDriverWait(driver_instance, delay).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-gpu")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Remote(
  desired_capabilities=webdriver.DesiredCapabilities.HTMLUNITWITHJS)

site_url = "https://data.gov.in/catalogs?"

driver.get(
    "https://data.gov.in/catalog/coverage-schools-tap-connection-under-jal-jeevan-mission-jjm"
)

notes_list = []
names_list = []
ref_url_list = []

reference_url_xpath = "//div[@class='CR_strip col-12'][1]"
note_xpath = "//div[@class='pr-0 col-12']/div/div/div"
name_xpath = "//div[@class='card-header']/span"

ref_url_elements = driver.find_elements(By.XPATH, reference_url_xpath)
note_elements = driver.find_elements(By.XPATH, note_xpath)
name_elements = driver.find_elements(By.XPATH, name_xpath)
if len(ref_url_elements) == len(note_elements) == len(name_elements):
    for i in range(len(name_elements)):
        element_not_found = True
        y = 10
        while element_not_found:
            try:
                ActionChains(driver).scroll_by_amount(0, y).perform()
                time.sleep(1)
                hov = ActionChains(driver).move_to_element(name_elements[i]).perform()
                wait_until_loading(driver, "//div[@class='popover-body']")
                name = driver.find_element(
                    By.XPATH, "//div[@class='popover-body']"
                ).text
                names_list.append(name)
                element_not_found = False
            except:
                y += 35

print(notes_list)
'''
na_xpath = "//div[@class='CR_strip col-12'][2]/div/div[3]"
nna_xpath = "//div[@class='CR_strip col-12'][2]/div/div[3]/*/*/a"
k = driver.find_elements(By.XPATH, na_xpath)
list_of_apis = []
for i in k:
    api_name = i.text
    print(api_name)
    if api_name == "NA":
        list_of_apis.append((api_name, "No link"))
    elif api_name != "NA":
        api_link = i.find_element(By.XPATH, "./*/*/a").get_attribute("href")
        list_of_apis.append((api_name, api_link))
print(list_of_apis)
'''










# resource_name_list = []
# tool_tips_real = driver.find_elements(By.XPATH, "//div[@class='card-header']/span")
# tool_tips_real.pop(0)
# for element in tool_tips_real:
#     finding_element = True
#     y = 10
#     while finding_element:
#         try:
#             print("y is now ", y)
#             ActionChains(driver).scroll_by_amount(0, y).perform()
#             time.sleep(1)
#             hov = ActionChains(driver).move_to_element(element).perform()
#             wait_until_loading(driver, "//div[@class='popover-body']")
#             name = driver.find_element(By.XPATH, "//div[@class='popover-body']").text
#             resource_name_list.append(name)
#             finding_element = False
#         except:
#             y += 35
# print(resource_name_list)
# print(len(resource_name_list))
#
#
# def get_resource_details(driver_instance: WebDriver):
#     wait_until_loading(driver_instance, "//a[@class='btn-preview']")
#     buttons = driver_instance.find_elements(By.XPATH, "//a[@class='btn-preview']")
#     heading_list = []
#     for i in buttons:
#         driver_instance.execute_script("arguments[0].click();", i)
#         wait_until_loading(driver_instance, "//h5[@class = 'modal-title']")
#         heading_list.append(
#             driver_instance.find_element(By.XPATH, "//h5[@class = 'modal-title']").text
#         )
#         wait_until_loading(driver_instance, "//h5[@class = 'modal-title']")
#         close_button = driver_instance.find_element(
#             By.XPATH, "//button[@class = 'close']"
#         )
#         driver_instance.execute_script("arguments[0].click();", close_button)
#         time.sleep(2)
#     return heading_list
