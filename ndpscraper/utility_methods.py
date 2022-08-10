""" The file contains the methods that are used to get various information from any given page of
data.gov.in website.
"""
import json
from typing import Any

import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ndpscraper import const_variables


def wait_until_loading(driver_instance: WebDriver, xpath: str, delay=10):
    """waits until an element is loaded"""

    WebDriverWait(driver_instance, delay).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def get_text_without_stale_element_exception(
    driver_instance: WebDriver, xpath: str, index: int
):
    """Even if waited for some time, there are chances of getting stale element exception
    This method overcomes it by retrying until the text is found.
    """
    required_text = ""
    stale_element = True
    while stale_element:
        try:
            required_text = (
                WebDriverWait(driver_instance, 10)
                .until(
                    EC.presence_of_element_located(
                        (By.XPATH, xpath + "[" + str(index) + "]")
                    )
                )
                .text
            )
            stale_element = False
        except:
            stale_element = True
    return required_text


def get_elem_without_stale_element_exception(
    driver_instance: WebDriver, xpath: str, index: int
):
    """Even if waited for some time, there are chances of getting stale element exception
    This method overcomes it by retrying until the element is found."""

    required_elem = Any
    stale_element = True
    while stale_element:
        try:
            required_elem = WebDriverWait(driver_instance, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, xpath + "[" + str(index) + "]")
                )
            )
            stale_element = False
        except:
            stale_element = True
    return required_elem


def xpath_exists(driver_instance: WebDriver, xpath: str):
    """Checks for the presence of an xpath in the given driver"""
    try:
        driver_instance.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def get_resource_names(driver_instance: WebDriver):
    """
    The method fetches the resource names present in the page. The names should be hovered over as they are
    truncated if too long.
    :param driver_instance:WebDriver
    :return: list of resource names
    """
    resource_name_list = []
    card_header_xpath = "(//div[@class='card-header']/span)"
    if xpath_exists(driver_instance, card_header_xpath):
        name_elements = driver_instance.find_elements(By.XPATH, card_header_xpath)
        name_elements.pop(0)
        list_size = 0
        if len(name_elements) == 1 or len(name_elements) == 2:
            list_size = len(name_elements) + 1
        else:
            list_size = len(name_elements) + 1
        for name_idx in range(2, list_size + 1):
            name = get_text_without_stale_element_exception(
                driver_instance, card_header_xpath, name_idx
            )
            resource_name_list.append(name)
        # The following for loop scrolls the page until it gets all the desired elements i.e. resource names
    return resource_name_list


def get_notes(driver_instance: WebDriver):
    """
    Note: Notes is usually truncated if it's too long. So it's necessary to hover over the notes element to
    fetch the complete text.
    :param driver_instance: WebDriver
    :return: List of Notes describing what the resource is all about.
    """
    notes_list = []
    notes_xpath = "(//span[@class='note_text'])"
    if xpath_exists(driver_instance, notes_xpath):
        notes_elements = driver_instance.find_elements(By.XPATH, notes_xpath)
        for note_idx in range(1, len(notes_elements) + 1):
            note = get_text_without_stale_element_exception(
                driver_instance, notes_xpath, note_idx
            )
            notes_list.append(note)
    return notes_list


def get_reference_urls(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of reference URLs of all the resources in the given page.
    """
    catalog_reference_urls = []
    reference_url_xpath = "(//div[@class='CR_strip col-12'][1]/div/div[3])"
    if xpath_exists(driver_instance, reference_url_xpath):
        reference_url_elements = driver_instance.find_elements(
            By.XPATH, reference_url_xpath
        )
        for url_idx in range(1, len(reference_url_elements) + 1):
            ref_url = get_text_without_stale_element_exception(
                driver_instance, reference_url_xpath, url_idx
            )
            catalog_reference_urls.append(ref_url)
    return catalog_reference_urls


def get_api_details(driver_instance: WebDriver):
    """
    The returned list contains tuples where the first element of the tuple corresponds to the name of the
    API and the second element is the link to API.
    :param driver_instance:WebDriver
    :return: list of tuples containing api details of all the resources in the given page.
    """
    api_list = []
    api_xpath = "(//div[@class='CR_strip col-12'][2]/div/div[3])"
    if xpath_exists(driver_instance, api_xpath):
        api_elements = driver_instance.find_elements(By.XPATH, api_xpath)
        for api_idx in range(1, len(api_elements) + 1):
            api_name = get_text_without_stale_element_exception(
                driver_instance, api_xpath, api_idx
            )
            # usually the name will be NA or something else. If na - no link else some link will be there
            if len(api_name) > 2:
                api_link = (
                    api_elements[api_idx - 1]
                    .find_element(By.XPATH, "./*/*/a")
                    .get_attribute("href")
                )
                api_list.append((api_name, api_link))
            else:
                api_list.append((api_name, "No link available"))
    return api_list


def get_nids(driver_instance: WebDriver):
    """
    Note: NID is crucial to get the resource URL. It's unique to the resource.
    NID is passed in the request payload which returns the resource URL in the response.
    :param driver_instance:WebDriver
    :return: List of NIDs of the resources present in the driver
    """
    nid_list = []
    nid_xpath = "(//*[@id='app']/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2])"
    if xpath_exists(driver_instance, nid_xpath):
        nid_elements = driver_instance.find_elements(By.XPATH, nid_xpath)
        for nid_idx in range(1, len(nid_elements) + 1):
            nid = get_elem_without_stale_element_exception(
                driver_instance, nid_xpath, nid_idx
            )
            nid_list.append(nid.get_attribute("nid"))
    return nid_list


def get_file_sizes(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of file sizes of all the resources present in a page
    """
    file_sizes = []
    file_size_xpath = "(//label[@title = 'File Size']/following::strong[1])"
    if xpath_exists(driver_instance, file_size_xpath):
        file_size_elements = driver_instance.find_elements(By.XPATH, file_size_xpath)
        for size_idx in range(1, len(file_size_elements) + 1):
            file_size = get_text_without_stale_element_exception(
                driver_instance, file_size_xpath, size_idx
            )
            file_sizes.append(file_size)
    return file_sizes


def get_download_counts(driver_instance: WebDriver):
    """
    :param driver_instance: WebDriver
    :return: list of download counts of all the resources in a page
    """
    downloads_count = []
    downloads_xpath = "(//label[@title = 'Download']/following::strong[1])"
    if xpath_exists(driver_instance, downloads_xpath):
        download_count_elements = driver_instance.find_elements(
            By.XPATH, downloads_xpath
        )
        for download_idx in range(1, len(download_count_elements) + 1):
            download = get_text_without_stale_element_exception(
                driver_instance, downloads_xpath, download_idx
            )
            downloads_count.append(download)
    return downloads_count


def get_granularity_of_all(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of granularity of all the resources in the given page.
    """
    resource_granularity_list = []
    granularity_xpath = "(//label[@title = 'Granularity']/following::strong[1])"
    if xpath_exists(driver_instance, granularity_xpath):
        wait_until_loading(driver_instance, granularity_xpath)
        granularity_elements = driver_instance.find_elements(
            By.XPATH, granularity_xpath
        )
        for gran_idx in range(1, len(granularity_elements) + 1):
            granularity_txt = get_text_without_stale_element_exception(
                driver_instance, granularity_xpath, gran_idx
            )
            resource_granularity_list.append(granularity_txt)
    return resource_granularity_list


def get_published_dates(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of published dates of all the resources in the given page.
    """
    published_dates_list = []
    published_date_xpath = "(//label[@title = 'Published on:']/following::strong[1])"
    if xpath_exists(driver_instance, published_date_xpath):
        published_dates_elements = driver_instance.find_elements(
            By.XPATH, published_date_xpath
        )
        for pub_idx in range(1, len(published_dates_elements) + 1):
            pub_date = get_text_without_stale_element_exception(
                driver_instance, published_date_xpath, pub_idx
            )
            published_dates_list.append(pub_date)
    return published_dates_list


def get_updated_dates(driver_instance: WebDriver):
    """
    :param driver_instance:WebDriver
    :return: list of updated dates of all the resources in the given page.
    """
    updated_dates_list = []
    updated_date_xpath = "(//label[@title = 'Updated on:']/following::strong[1])"
    if xpath_exists(driver_instance, updated_date_xpath):
        updated_dates_elements = driver_instance.find_elements(
            By.XPATH, updated_date_xpath
        )
        for up_idx in range(1, len(updated_dates_elements) + 1):
            up_date = get_text_without_stale_element_exception(
                driver_instance, updated_date_xpath, up_idx
            )
            updated_dates_list.append(up_date)
    return updated_dates_list


def get_resource_urls(list_of_nids: list):
    """
    The method requests the server with list of NIDs and fetches the resource URLs pertaining to the
    corresponding NID.
    NID is passed in the request payload.
    :param: list_of_nids: List
    :return: List of resource URLs
    """
    resource_url_list = []
    for nid in list_of_nids:
        json_payload = json.loads(const_variables.payload)
        json_payload["resource_id"][0]["target_id"] = nid
        request_payload = json.dumps(json_payload)
        response = requests.post(
            "https://data.gov.in/backend/dms/v1/ogdp/download_purpose?_format=json",
            data=request_payload,
            headers=const_variables.header_dict,
        ).content
        json_response = json.loads(response)
        resource_url_list.append(json_response["download_url"])
    print(resource_url_list)
    return resource_url_list
