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

def get_nids(driver: WebDriver):
    pass

def get_resource_details(driver: WebDriver):
    pass


options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument('disable-infobars')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-gpu')

path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)

site_url = "https://data.gov.in/catalogs?"

driver.get("https://data.gov.in/catalogs?page=1")

detail_nid_tuple = ()
for page in range(2, 4):
    print("inside main page loop..")
    card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
    # [link1, link2, link3....]
    for i in range(0, len(card_link_by_xpath)):
        print("traversing all the cards of the page...")
        sub_driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
        master_resource_url = card_link_by_xpath[i].get_attribute("href")
        # [link1, link2, link3....] in above list
        sub_driver.get(master_resource_url)
        # open link1, link2 and so on...
        try:
            num_of_pages = calculate_num_of_pages(sub_driver)
        except:
            continue  # if it can't calculate any page -> no data inside that link
        # calculate num of pages in each opened link...as first link is opened get all nids..
        page_nid_list = sub_driver.find_elements(By.XPATH, NID_XPATH)
        resource_detail = sub_driver.find_elements(By.XPATH, RESOURCE_DETAIL_XPATH)
        resource_detail_list = []
        list_of_nids = []
        for detail_index in range(len(resource_detail)):
            resource_detail_list.append(resource_detail[detail_index].text)
        resource_detail_list.remove("")# TODO On examining the page, it is noticed that the resource detail will be found from the second element in the list
        # First element is always empty
        for nid in range(len(page_nid_list)):
            list_of_nids.append(page_nid_list[nid].get_attribute("nid"))  # once calculated, get nids by
            # visiting all the other pages...
        print("CHECKING LENGTH%%%%%", len(resource_detail_list), len(list_of_nids))
        detail_nid_tuple = detail_nid_tuple + tuple(zip(resource_detail_list, list_of_nids))
        for j in range(2, num_of_pages):
            # TODO remove the following 'if' after test
            if num_of_pages > 3:
                break
            print("going to the next page under same resource....")
            sub_sub_driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
            master_resource_params = {'page': j}
            master_resource_page_to_get = master_resource_url + "?" + urllib.parse.urlencode(master_resource_params)
            sub_sub_driver.get(master_resource_page_to_get)  # open next page
            page_nid_list = sub_sub_driver.find_elements(By.XPATH, NID_XPATH)
            for nid_index in range(len(page_nid_list)):
                list_of_nids.append(page_nid_list[nid_index].get_attribute("nid"))
            resource_detail = sub_sub_driver.find_elements(By.XPATH, RESOURCE_DETAIL_XPATH)
            resource_detail_list = []
            for detail_index in range(len(resource_detail)):
                resource_detail_list.append(resource_detail[detail_index].text)
            resource_detail_list.remove("")  # TODO On examining the page, it is noticed that the resource detail will be found from the second element in the list
            # First element is always empty
            detail_nid_tuple = detail_nid_tuple + tuple(zip(resource_detail_list, list_of_nids))
            sub_sub_driver.close()

        sub_driver.close()
    params = {'page': page}
    url_to_get = site_url + urllib.parse.urlencode(params)
    print("closing driver")
    driver.close()
    print("opening driver..")
    driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
    driver.get(url_to_get)

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
