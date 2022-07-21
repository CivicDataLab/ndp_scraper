import logging
import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import requests
import re
from variables import *
import urllib.parse
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until_loading(driver_instance: WebDriver, xpath: str, delay = 3):
    WebDriverWait(driver_instance, delay).until(
        EC.presence_of_element_located((By.XPATH, xpath)))

def calculate_num_of_pages(driver_instance: WebDriver):
    wait_until_loading(driver_instance, "//div[@class='search_num_result d-block float-left']")
    count_info = driver_instance.find_element(By.XPATH, "//div[@class='search_num_result d-block float-left']").text
    total_count = int(re.findall('\d+', "".join(count_info.split("of")[1].split()))[0])
    print(total_count)
    records_in_page = len(driver_instance.find_elements(By.XPATH, "//div[@class = 'card']"))
    print(records_in_page)
    num_of_pages = math.ceil(total_count / records_in_page)
    return num_of_pages


def get_nids(driver: WebDriver):
    pass


def get_resource_details(driver_instance: WebDriver):
    wait_until_loading(driver_instance, "//a[@class='btn-preview']")
    buttons = driver_instance.find_elements(By.XPATH, "//a[@class='btn-preview']")
    heading_list = []
    for i in buttons:
        driver_instance.execute_script("arguments[0].click();", i)
        wait_until_loading(driver_instance, "//h5[@class = 'modal-title']")
        heading_list.append(driver_instance.find_element(By.XPATH, "//h5[@class = 'modal-title']").text)
        wait_until_loading(driver_instance, "//h5[@class = 'modal-title']")
        close_button = driver_instance.find_element(By.XPATH, "//button[@class = 'close']")
        driver_instance.execute_script("arguments[0].click();", close_button)
        time.sleep(2)
    return heading_list


options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument('disable-infobars')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-gpu')
options.add_argument("headless")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)

site_url = "https://data.gov.in/catalogs?"

driver.get("https://data.gov.in/catalogs?page=1")

detail_nid_tuple = ()
for page in range(2, 4):  # TODO change the upper limit to total num of pages while prod run
    try:
        print("inside main page loop..")
        wait_until_loading(driver, "//div[@class='card-header']/a")
        card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
        # [link1, link2, link3....]
        for card_link in card_link_by_xpath:
            print("traversing all the cards of the page...")
            sub_driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
            master_resource_url = card_link.get_attribute("href")
            # [link1, link2, link3....] in above list
            try:
                sub_driver.get(master_resource_url)
            except:
                logging.info("Error Loading ", master_resource_url)
                continue
            #time.sleep(8)
            # open link1, link2 and so on...
            try:
                num_of_pages = calculate_num_of_pages(sub_driver)
            except:
                logging.info("No resources under ", master_resource_url)
                continue  # if it can't calculate any page -> no data inside that link
            # calculate num of pages in each opened link...as first link is opened get all nids..
            wait_until_loading(sub_driver, NID_XPATH, 5)
            page_nid_list = sub_driver.find_elements(By.XPATH, NID_XPATH)
            # resource_detail = sub_driver.find_elements(By.XPATH, RESOURCE_DETAIL_XPATH)
            try:
                resource_detail_list = get_resource_details(sub_driver)
            except:
                logging.info("Error getting details from the page.. ",master_resource_url," moving on to the next page..")
                continue
            list_of_nids = []
            for nid in page_nid_list:
                list_of_nids.append(nid.get_attribute("nid"))  # once calculated, get nids by
                # visiting all the other pages...
            print("CHECKING LENGTH%%%%%", len(resource_detail_list), len(list_of_nids))
            detail_nid_tuple = detail_nid_tuple + tuple(zip(resource_detail_list, list_of_nids))
            for j in range(2, num_of_pages+1):
                # TODO remove the following 'if' after test
                if j > 3:
                    break
                print("going to the next page under same resource....")
                sub_sub_driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
                master_resource_params = {'page': j}
                master_resource_page_to_get = master_resource_url + "?" + urllib.parse.urlencode(master_resource_params)
                try:
                    sub_sub_driver.get(master_resource_page_to_get)  # open next page
                except:
                    logging.info("Error loading ", master_resource_page_to_get, " continuing with the next..")
                    continue
                wait_until_loading(sub_sub_driver, NID_XPATH, 5)
                page_nid_list = sub_sub_driver.find_elements(By.XPATH, NID_XPATH)
                for nid_index in range(len(page_nid_list)):
                    list_of_nids.append(page_nid_list[nid_index].get_attribute("nid"))
                resource_detail_list = get_resource_details(sub_sub_driver)
                detail_nid_tuple = detail_nid_tuple + tuple(zip(resource_detail_list, list_of_nids))
                sub_sub_driver.close()

            sub_driver.close()
        params = {'page': page}
        url_to_get = site_url + urllib.parse.urlencode(params)
        driver.close()
        driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
        driver.get(url_to_get)
        time.sleep(2)
    except:
        continue

print(len(detail_nid_tuple))
print(set(detail_nid_tuple))

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

res = requests.post('https://data.gov.in/backend/dms/v1/ogdp/download_purpose?_format=json', data=payload,
                    headers=header_dict)
print(res.content)
print("$$$$$$$$")
