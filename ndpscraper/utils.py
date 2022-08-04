""" The file contains the methods that are used to get various information from any given page of
data.gov.in website.
"""

import json
import math
import re
import time

import requests
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ndpscraper import variables


def wait_until_loading(driver_instance: WebDriver, xpath: str, delay=3):
    """This method waits for 'delay' seconds until a particular element is loaded"""
    WebDriverWait(driver_instance, delay).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def scroll_to_top(driver_instance: WebDriver):
    """Scrolls to the top of the page"""
    driver_instance.find_element(By.TAG_NAME, "body").send_keys(
        Keys.CONTROL + Keys.HOME
    )


def xpath_exists(driver_instance: WebDriver, xpath: str):
    """Checks if the given xpath exists in the driver"""
    try:
        driver_instance.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def calculate_num_of_pages(driver_instance: WebDriver):
    """
    This method searches for total number of resources for a given catalog using the xpath.
    Then it divides the total number of resources by the number of resources per page there by getting
    the total number of pages.
    Ex:The xpath text looks something like 1-9 of 7843 resources
    So the total number of resources is 7843 and resources per page is 9, num of pages returned is
    ceil(7843/9) = ceil(871.4) = 872 pages.

    :param driver_instance: WebDriver
    :return: Number of pages for the given resource
    """
    count_info_xpath = "//div[@class='search_num_result d-block float-left']"
    if xpath_exists(driver_instance, count_info_xpath):
        wait_until_loading(driver_instance, count_info_xpath)
        count_info = driver_instance.find_element(By.XPATH, count_info_xpath).text
        total_count = int(
            re.findall("\d+", "".join(count_info.split("of")[1].split()))[0]
        )
        print(total_count)
        records_in_page = len(
            driver_instance.find_elements(By.XPATH, "//div[@class = 'card']")
        )
        total_num_of_pages = math.ceil(total_count / records_in_page)
        print("Num of pages is...", total_num_of_pages)
        return total_num_of_pages
    else:
        return 0


def get_nids(driver_instance: WebDriver):
    """
    Note: NID is crucial to get the resource URL. It's unique to the resource.
    NID is passed in the request payload which returns the resource URL in the response.
    :param driver_instance:WebDriver
    :return: List of NIDs of the resources present in the driver
    """
    nid_list = []
    nid_xpath = "//*[@id='app']/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]"
    if xpath_exists(driver_instance, nid_xpath):
        nid_elements = driver_instance.find_elements(By.XPATH, nid_xpath)
        for element in nid_elements:
            nid_list.append(element.get_attribute("nid"))
    return nid_list


def get_file_sizes(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of file sizes of all the resources present in a page
    """
    file_sizes = []
    file_size_xpath = "//label[@title = 'File Size']/following::strong[1]"
    if xpath_exists(driver_instance, file_size_xpath):
        file_size_elements = driver_instance.find_elements(By.XPATH, file_size_xpath)
        for element in file_size_elements:
            file_sizes.append(element.text)
    return file_sizes


def get_download_counts(driver_instance: WebDriver):
    """
    :param driver_instance: WebDriver
    :return: list of download counts of all the resources in a page
    """
    downloads_count = []
    downloads_xpath = "//label[@title = 'Download']/following::strong[1]"
    if xpath_exists(driver_instance, downloads_xpath):
        download_count_elements = driver_instance.find_elements(
            By.XPATH, downloads_xpath
        )
        for element in download_count_elements:
            downloads_count.append(element.text)
    return downloads_count


def get_granularity_of_all(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of granularity of all the resources in the given page.
    """
    resource_granularity_list = []
    granularity_xpath = "//label[@title = 'Granularity']/following::strong[1]"
    if xpath_exists(driver_instance, granularity_xpath):
        granularity = driver_instance.find_elements(By.XPATH, granularity_xpath)
        for element in granularity:
            resource_granularity_list.append(element.text)
    return resource_granularity_list


def get_published_dates(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of published dates of all the resources in the given page.
    """
    published_dates_list = []
    published_date_xpath = "//label[@title = 'Published on:']/following::strong[1]"
    if xpath_exists(driver_instance, published_date_xpath):
        published_dates_elements = driver_instance.find_elements(
            By.XPATH, published_date_xpath
        )
        for element in published_dates_elements:
            published_dates_list.append(element.text)
    return published_dates_list


def get_updated_dates(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of updated dates of all the resources in the given page.
    """
    updated_dates_list = []
    updated_date_xpath = "//label[@title = 'Updated on:']/following::strong[1]"
    if xpath_exists(driver_instance, updated_date_xpath):
        updated_dates_elements = driver_instance.find_elements(
            By.XPATH, updated_date_xpath
        )
        for element in updated_dates_elements:
            updated_dates_list.append(element.text)
    return updated_dates_list


def get_reference_urls(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of reference URLs of all the resources in the given page.
    """
    catalog_reference_urls = []
    reference_url_xpath = "//div[@class='CR_strip col-12'][1]/div/div[3]"
    if xpath_exists(driver_instance, reference_url_xpath):
        reference_url_elements = driver_instance.find_elements(
            By.XPATH, reference_url_xpath
        )
        for element in reference_url_elements:
            catalog_reference_urls.append(element.text)
    return catalog_reference_urls


def get_api_details(driver_instance: WebDriver):
    """
    The returned list contains tuples where the first element of the tuple corresponds to the name of the
    API and the second element is the link to API.
    :param driver_instance:WebDriver
    :return: list of tuples containing api details of all the resources in the given page.
    """
    api_list = []
    api_xpath = "//div[@class='CR_strip col-12'][2]/div/div[3]"
    if xpath_exists(driver_instance, api_xpath):
        api_elements = driver_instance.find_elements(By.XPATH, api_xpath)
        for element in api_elements:
            api_name = element.text
            # usually the name will be NA or something else. If na - no link else some link will be there
            if len(api_name) > 2:
                api_link = element.find_element(By.XPATH, "./*/*/a").get_attribute(
                    "href"
                )
                api_list.append((api_name, api_link))
            else:
                api_list.append((api_name, "No link available"))
    return api_list


def get_notes(driver_instance: WebDriver):
    """
    Note: Notes is usually truncated if it's too long. So it's necessary to hover over the notes element to
    fetch the complete text.
    :param driver_instance: WebDriver
    :return: List of Notes describing what the resource is all about.
    """
    notes_list = []
    notes_xpath = "//div[@class='pr-0 col-12']/div/div/div"
    scroll_to_top(driver_instance)
    if xpath_exists(driver_instance, notes_xpath):
        time.sleep(1)
        notes_elements = driver_instance.find_elements(By.XPATH, notes_xpath)
        for element in notes_elements:
            element_not_found = True
            y = 10
            while element_not_found:
                try:
                    ActionChains(driver_instance).scroll_by_amount(0, y).perform()
                    time.sleep(1)
                    hov = (
                        ActionChains(driver_instance).move_to_element(element).perform()
                    )
                    wait_until_loading(driver_instance, "//div[@class='popover-body']")
                    note = driver_instance.find_element(
                        By.XPATH, "//div[@class='popover-body']"
                    ).text
                    notes_list.append(note)
                    element_not_found = False
                except:
                    y += 35
    return notes_list


def get_resource_names(driver_instance: WebDriver):
    """
    The method fetches the resource names present in the page. The names should be hovered over as they are
    truncated if too long.
    :param driver_instance:WebDriver
    :return: list of resource names
    """
    resource_name_list = []
    card_header_xpath = "//div[@class='card-header']/span"
    if xpath_exists(driver_instance, card_header_xpath):
        tool_tips_real = driver_instance.find_elements(By.XPATH, card_header_xpath)
        tool_tips_real.pop(0)
        # The following for loop scrolls the page until it gets all the desired elements i.e. resource names
        for element in tool_tips_real:
            element_not_found = True
            y = 10  # Initial pixel
            while element_not_found:
                try:
                    ActionChains(driver_instance).scroll_by_amount(0, y).perform()
                    time.sleep(1)
                    hov = (
                        ActionChains(driver_instance).move_to_element(element).perform()
                    )
                    wait_until_loading(driver_instance, "//div[@class='popover-body']")
                    name = driver_instance.find_element(
                        By.XPATH, "//div[@class='popover-body']"
                    ).text
                    resource_name_list.append(name)
                    element_not_found = False
                except:
                    y += 35  # Pixels to scroll if the element is not found.
    return resource_name_list


def get_resource_urls(nids: list):
    """
    The method requests the server with list of NIDs and fetches the resource URLs pertaining to the
    corresponding NID.
    NID is passed in the request payload.
    :param nids: List
    :return: List of resource URLs
    """
    resource_url_list = []
    for nid in nids:
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
    return resource_url_list
