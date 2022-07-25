#kcc

import logging
import math
import time

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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until_loading(driver_instance: WebDriver, xpath: str, delay = 3):
    if delay == 3:
        print("new delay is : ", delay)
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


def get_metadata(driver: WebDriver):
    wait_until_loading(driver, "//span[@title='Click Here To View Info']")
    catalog_info_button = driver.find_element(By.XPATH, "//span[@title='Click Here To View Info']")
    driver.execute_script("arguments[0].click();", catalog_info_button)
    metadata = metadata_dict
    metadata["Catalog Name"] = driver.find_element(By.XPATH, "//li[@class = 'breadcrumb-item active']/span").text
    metadata["Catalog Info"] = driver.find_element(By.XPATH, "//span[@class = 'mb-2 mt-4 catalog_info_desc']/p").text
    metadata["Released Under"] = driver.find_element(By.XPATH, "//*[@id='accordion-1']/div/div/div/ul/li/a").text
    wait_until_loading(driver, "//*[@id='accordion-2']/div/p/div/*/*/a")
    contributor_elements = driver.find_elements(By.XPATH, "//*[@id='accordion-2']/div/p/div/*/*/a")
    for element in contributor_elements:
        print(element.get_attribute("innerHTML"))

    metadata["Contributor"] ="",
    metadata["Keywords"] = "",
    metadata["Group"] = "",
    metadata["Sectors"] =  "",
    metadata["Published On"] = "",
    metadata["Updated On"] = ""
    metadata["Domain"] =  "",
    metadata["CDO Name"] = driver.find_element(By.XPATH, "//h3[@class = 'cdo_name m-0']").text
    metadata["CDO Post"] = driver.find_element(By.XPATH, "//p[@class='cdo_post m-0']").text,

    # Ministry name can be long and can only be extracted when hovered over it
    wait_until_loading(driver, "//div[@class='details col-6']/h3")
    toolTip = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='details col-6']/h3")))
    hov = ActionChains(driver).move_to_element(toolTip)
    txt = hov.perform()
    wait_until_loading(driver, "//div[@class='popover-body']")
    ministry_name = driver.find_element(By.XPATH, "//div[@class='popover-body']").text
    metadata["Ministry/State/Department"] =  ministry_name,
    metadata["Phone"] = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/h3").text,
    metadata["Email"] = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[3]/h3").text,
    # even address is extracted by hovering
    toolTip = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[4]/div[3]")))
    hov = ActionChains(driver).move_to_element(toolTip)
    txt = hov.perform()
    wait_until_loading(driver, "//div[@class='popover-body']")
    address = driver.find_element(By.XPATH, "//div[@class='popover-body']").text
    metadata["Address"] = address
    print(metadata)
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
##options.add_argument("headless")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
#phantom
site_url = "https://data.gov.in/catalogs?"

driver.get("https://data.gov.in/catalogs?page=1")

detail_nid_tuple = ()
for page in range(2, 4):  # TODO change the upper limit to total num of pages while prod run
    print("inside main page loop..")
    wait_until_loading(driver, "//div[@class='card-header']/a")
    card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
    logging.info("recieved resource links ->", card_link_by_xpath)
    # [link1, link2, link3....]
    for card_link in card_link_by_xpath:
        print("traversing all the cards of the page...")
        sub_driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
        master_resource_url = card_link.get_attribute("href")
        logging.info("scraped ", card_link)
        # [link1, link2, link3....] in above list
        try:
            sub_driver.get(master_resource_url)
        except:
            logging.warning("Error Loading ", master_resource_url)
            sub_driver.close()
            continue
        get_metadata(sub_driver)
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
            logging.warning("Error getting details from the page.. ",master_resource_url," moving on to the next page..")
            sub_driver.close()
            continue
        list_of_nids = []
        for nid in page_nid_list:
            list_of_nids.append(nid.get_attribute("nid"))  # once calculated, get nids by
            # visiting all the other pages...
        print("CHECKING LENGTH%%%%%", len(resource_detail_list), len(list_of_nids))
        detail_nid_tuple = detail_nid_tuple + tuple(zip(resource_detail_list, list_of_nids))
        for j in range(2, num_of_pages+1):
            if j > 3:
                break # TODO remove the following 'if' after test
            print("going to the next page under same resource....")
            sub_sub_driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
            master_resource_params = {'page': j}
            master_resource_page_to_get = master_resource_url + "?" + urllib.parse.urlencode(master_resource_params)
            try:
                sub_sub_driver.get(master_resource_page_to_get)  # open next page
            except:
                logging.warning("Error loading ", master_resource_page_to_get, " continuing with the next..")
                sub_sub_driver.close()
                continue
            try:
                wait_until_loading(sub_sub_driver, NID_XPATH, 5)
            except: # TODO this is the possible failure point.. try to make a request by sleeping once
                logging.warning("error while waiting for... ", master_resource_page_to_get, " trying once more ")
                try:
                    wait_until_loading(sub_sub_driver, NID_XPATH, 15)
                except:
                    logging.warning("The url ", master_resource_url, " didn't load.. continuing with next")
                    sub_sub_driver.close()
                    continue
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
