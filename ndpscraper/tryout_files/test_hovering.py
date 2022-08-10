""" All rough scripts here.. """
import json
import logging
import re
import time

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ndpscraper import variables


def wait_until_loading(driver_instance: WebDriver, xpath: str, delay=3):
    if delay == 3:
        print("new delay is : ", delay)
    WebDriverWait(driver_instance, delay).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def xpath_exists(driver: WebDriver, xpath: str):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-gpu")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
site_url = "https://data.gov.in/catalogs?"

driver.get("https://data.gov.in/catalog/surat-citizen-centric-services")


def get_resource_urls(list_of_nids: list):
    """
    The method requests the server with list of NIDs and fetches the resource URLs pertaining to the
    corresponding NID.
    NID is passed in the request payload.
    :param list_of_nids: List
    :return: List of resource URLs
    """
    resource_url_list = []
    for nid in list_of_nids:
        json_payload = json.loads(variables.payload)
        json_payload["resource_id"][0]["target_id"] = nid
        request_payload = json.dumps(json_payload)
        response = requests.post(
            "https://data.gov.in/backend/dms/v1/ogdp/download_purpose?_format=json",
            data=request_payload,
            headers=variables.header_dict,
        ).content
        json_response = json.loads(response)
        resource_url_list.append(json_response["download_url"])
    print(resource_url_list)
    return resource_url_list

    # for nid in nid_list:
    #     json_payload = json.loads(variables.payload)
    #


nid_list = ["804661"]
get_resource_urls(nid_list)


# def get_metadata(driver_instance: WebDriver):
#     wait_until_loading(driver_instance, "//span[@title='Click Here To View Info']")
#     catalog_info_button = driver_instance.find_element(
#         By.XPATH, "//span[@title='Click Here To View Info']"
#     )
#     catalog_name_xpath = "//li[@class = 'breadcrumb-item active']/span"
#     catalog_info_xpath = "//span[@class = 'mb-2 mt-4 catalog_info_desc']"
#     released_under_xpath = "//*[@id='accordion-1']/div/div/div/ul/li/a"
#     contributor_xpath = "//*[@id='accordion-2']/div/p/div/*/*/a"
#     keywords_xpath = "//*[@id='accordion-3']/div/p/div/a"
#     group_xpath = "//*[@id='accordion-4']/div/p/div"
#     sector_xpath = "//*[@id='accordion-5']/div/p/div/a"
#     published_on_xpath = "//*[@id='accordion-6']/div/div/div/ul/li"
#     updated_on_xpath = "//*[@id='accordion-7']/div/div/div/ul/li"
#     domain_xpath = "//*[@id='accordion-8']/div/div/div/div/p"
#     # //*[@id="accordion-8"]/div/div/div/div/p
#     cdo_name_xpath = "//h3[@class = 'cdo_name m-0']"
#     cdo_post_xpath = "//p[@class='cdo_post m-0']"
#     ministry_name_xpath = "//div[@class='details col-6']/h3"
#     phone_number_xpath = (
#         "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/h3"
#     )
#     email_xpath = (
#         "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[3]/h3"
#     )
#     address_xpath = (
#         "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[4]/div[3]"
#     )
#     metadata = variables.metadata_dict
#     try:
#         driver_instance.execute_script("arguments[0].click();", catalog_info_button)
#         if xpath_exists(driver_instance, catalog_name_xpath):
#             metadata["Catalog Name"] = driver_instance.find_element(
#                 By.XPATH, catalog_name_xpath
#             ).text
#         if xpath_exists(driver_instance, catalog_info_xpath):
#             if xpath_exists(driver_instance, catalog_info_xpath + "/following::a") and \
#                     driver_instance.find_element(By.XPATH, catalog_info_xpath + "/following::a").text.startswith(
#                         "More"):
#                 more_button = driver_instance.find_element(By.XPATH, catalog_info_xpath + "/following::a")
#                 clk = ActionChains(driver_instance).move_to_element(more_button).click().perform()
#                 descriptive_info_xpath = "//p[@class = 'mb-2 catalog_info_desc']/p"
#                 wait_until_loading(driver_instance, descriptive_info_xpath)
#                 metadata["Catalog Info"] = driver_instance.find_element(By.XPATH, descriptive_info_xpath).text
#             elif xpath_exists(driver_instance, catalog_info_xpath + "/p"):
#                 metadata["Catalog Info"] = driver_instance.find_element(
#                     By.XPATH, catalog_info_xpath + "/p"
#                 ).text
#
#         if xpath_exists(driver_instance, released_under_xpath):
#             metadata["Released Under"] = driver_instance.find_element(
#                 By.XPATH, released_under_xpath
#             ).text
#
#         wait_until_loading(driver_instance, contributor_xpath)  # xpath for contributor
#         if xpath_exists(driver_instance, contributor_xpath):
#             contributor_elements = driver_instance.find_elements(By.XPATH, contributor_xpath)
#             contributors_list = []
#             for element in contributor_elements:
#                 contributors_list.append(element.get_attribute("innerHTML"))
#             metadata["Contributor"] = contributors_list
#
#         if xpath_exists(driver_instance, keywords_xpath):
#             keyword_elements = driver_instance.find_elements(By.XPATH, keywords_xpath)
#             keywords_list = []
#             for element in keyword_elements:
#                 keywords_list.append(element.get_attribute("innerHTML"))
#             metadata["Keywords"] = keywords_list
#
#         if xpath_exists(driver_instance, group_xpath):
#             group_elements = driver_instance.find_elements(By.XPATH, group_xpath)
#             groups_list = []
#             for element in group_elements:
#                 groups_list.append(element.text)
#             metadata["Group"] = groups_list
#
#         if xpath_exists(driver_instance, sector_xpath):
#             sector_elements = driver_instance.find_elements(By.XPATH, sector_xpath)
#             sectors_list = []
#             for element in sector_elements:
#                 sectors_list.append(element.get_attribute("innerHTML"))
#             metadata["Sectors"] = sectors_list
#
#         if xpath_exists(driver_instance, published_on_xpath):
#             metadata["Published On"] = driver_instance.find_element(
#                 By.XPATH, published_on_xpath
#             ).get_attribute("innerHTML")
#
#         if xpath_exists(driver_instance, updated_on_xpath):
#             metadata["Updated On"] = driver_instance.find_element(
#                 By.XPATH, updated_on_xpath
#             ).get_attribute("innerHTML")
#
#         if xpath_exists(driver_instance, domain_xpath):
#             metadata["Domain"] = driver_instance.find_element(
#                 By.XPATH, domain_xpath
#             ).get_attribute("innerHTML")
#
#         if xpath_exists(driver_instance, cdo_name_xpath):
#             metadata["CDO Name"] = driver_instance.find_element(By.XPATH, cdo_name_xpath).text
#         if xpath_exists(driver_instance, cdo_post_xpath):
#             metadata["CDO Post"] = (driver_instance.find_element(By.XPATH, cdo_post_xpath).text,)
#
#         # Ministry name can be long and can only be extracted when hovered over it
#         if xpath_exists(driver_instance, ministry_name_xpath):
#             try:
#                 toolTip = WebDriverWait(driver_instance, 3).until(
#                     EC.presence_of_element_located(
#                         (By.XPATH, "//div[@class='details col-6']/h3")
#                     )
#                 )
#                 hov = ActionChains(driver_instance).move_to_element(toolTip).perform()
#                 wait_until_loading(driver_instance, "//div[@class='popover-body']")
#                 ministry_name = driver_instance.find_element(
#                     By.XPATH, "//div[@class='popover-body']"
#                 ).text
#                 metadata["Ministry/State/Department"] = ministry_name
#             except:
#                 logging.warning("Ministry name isn't intractable")
#         if xpath_exists(driver_instance, phone_number_xpath):
#             metadata["Phone"] = (
#                 driver_instance.find_element(By.XPATH, phone_number_xpath).text,
#             )
#         if xpath_exists(driver_instance, email_xpath):
#             metadata["Email"] = (driver_instance.find_element(By.XPATH, email_xpath).text,)
#         # even address is extracted by hovering
#         if xpath_exists(driver_instance, address_xpath):
#             try:
#                 toolTip = WebDriverWait(driver_instance, 3).until(
#                     EC.presence_of_element_located((By.XPATH, address_xpath))
#                 )
#                 hov = ActionChains(driver_instance).move_to_element(toolTip).perform()
#                 wait_until_loading(driver_instance, "//div[@class='popover-body']")
#                 address = driver_instance.find_element(
#                     By.XPATH, "//div[@class='popover-body']"
#                 ).text
#                 metadata["Address"] = address
#             except:
#                 logging.warning("Address not intractable")
#         print("########", metadata)
#         return metadata
#     except:
#         logging.warning("Catalog button isn't clickable..")
#
#
# get_metadata(driver)

"""
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
"""

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
