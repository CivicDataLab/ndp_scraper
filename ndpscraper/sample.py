import math

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import requests
import re
from variables import *
import urllib.parse
from selenium.webdriver.remote.webelement import WebElement

def calculate_num_of_pages(driver: WebDriver):
    count_info = driver.find_element(By.XPATH, "//div[@class='search_num_result d-block float-left']").text
    total_count = int(re.findall('\d+', "".join(count_info.split("of")[1].split()))[0])
    print(total_count)
    records_in_page = len(driver.find_elements(By.XPATH, "//div[@class = 'card']"))
    print(records_in_page)
    num_of_pages = math.ceil(total_count / records_in_page)
    return num_of_pages


options = Options()
options.add_argument("--window-size=1920,1200")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options = options, executable_path = path_to_chrome_driver)
sub_driver = webdriver.Chrome(options = options, executable_path = path_to_chrome_driver)

site_url = "https://data.gov.in/catalogs?"


driver.get("https://data.gov.in/catalogs?page=1")


card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
for card in card_link_by_xpath:
    print(card.text)

# link_text = card_link_by_xpath[0].text
# link = driver.find_element(By.LINK_TEXT, link_text)
# link.click()
# print(len(driver.window_handles))
# window_after = driver.window_handles[0]
# driver.switch_to.window(window_after)
# print(driver.page_source)

# Get the url of the resource into a list
master_resource_url = card_link_by_xpath[1].get_attribute("href")
sub_driver.get(master_resource_url)
master_resource_page_number = 1
num_of_pages = calculate_num_of_pages(sub_driver)
# getting NID
nid = sub_driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]").get_attribute("nid")


for page in range(1, PAGES_TO_TRAVERSE_IN_SITE):
    params = {'page': page}
    url_to_get = site_url + urllib.parse.urlencode(params)


# while(next_page_exists(sub_driver)):
#     master_resource_page_number += 1
#     master_resource_url_new = master_resource_url + "?page=" + str(master_resource_page_number)
#     page_driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
#     page_driver.get(master_resource_url_new)
#     sub_driver = page_driver

""" This loop should be kept !!!!!"""
# for card_link in card_link_by_xpath:
#     master_resource_url = card_link.get_attribute("href")
#     sub_driver.get(master_resource_url)

#sub_driver.close()
driver.close()


"""Making a request ... Headers are to be updated using selectors """
payload = '{"name":[{"value":"zcc"}],' \
          '"uid":[{"value":0}],' \
          '"ip":[{"value":""}],' \
          '"usage":[{"value":"2"}],' \
          '"purpose":[{"value":"5"}],' \
          '"file_type":[{"value":"csv"}],' \
          '"export_status":[{"value":"url"}],' \
          '"email":[{"value":"awd@g.co"}],' \
          '"catalog_id":[{"target_id":""}],' \
          '"resource_id":[{"target_id":6720073}]}'

header = header_dict

res = requests.post('https://data.gov.in/backend/dms/v1/ogdp/download_purpose?_format=json', data = payload,
                    headers = header_dict)
print(res.content)
print("$$$$$$$$")



