""" Entry point to scrape https://data.gov.in/catalogs? site."""

# kcc
import logging
import urllib.parse

import csvwriter
from catalog_metadata_extractor import get_metadata
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import *
from variables import *

options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-gpu")
# options.add_argument("headless")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
site_url = "https://data.gov.in/catalogs?"

start_time = time.time()

driver.get("https://data.gov.in/catalogs?page=1")

for page in range(
    2, 3
):  # TODO change the upper limit to PAGES_TO_TRAVERSE_IN_SITE from variables.py while prod run
    print("inside main page ", page)
    wait_until_loading(driver, "//div[@class='card-header']/a")
    card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
    logging.info("received resource links ->", card_link_by_xpath)
    for card_link in card_link_by_xpath:
        print("traversing the resource..", card_link.text)
        sub_driver = webdriver.Chrome(
            options=options, executable_path=path_to_chrome_driver
        )
        master_resource_url = card_link.get_attribute("href")
        # [link1, link2, link3....] in above list
        try:
            sub_driver.get(master_resource_url)
        except:
            logging.warning("Error Loading ", master_resource_url)
            sub_driver.close()
            continue
        metadata = {}
        metadata = get_metadata(sub_driver)
        # time.sleep(8)
        # open link1, link2 and so on...
        try:
            num_of_pages = calculate_num_of_pages(sub_driver)
        except:
            logging.info("No resources under ", master_resource_url)
            continue  # if it can't calculate any page -> no data inside that link
        # calculate num of pages in each opened link...as first link is opened get all nids..
        # resource_detail = sub_driver.find_elements(By.XPATH, RESOURCE_DETAIL_XPATH)
        try:
            resource_detail_list = get_resource_names(sub_driver)
        except:
            logging.warning(
                "Error getting details from the page.. ",
                master_resource_url,
                " moving on to the next page..",
            )
            sub_driver.close()
            continue
        list_of_nids = get_nids(sub_driver)
        print("CHECKING LENGTH%%%%%", len(resource_detail_list), len(list_of_nids))
        # get details of the resources in the first page
        list_of_file_sizes = get_file_sizes(sub_driver)
        download_count_list = get_download_counts(sub_driver)
        granularity_list = get_granularity_of_all(sub_driver)
        published_dates = get_published_dates(sub_driver)
        updated_dates = get_updated_dates(sub_driver)
        reference_urls = get_reference_urls(sub_driver)
        api_details = get_api_details(sub_driver)
        notes = get_notes(sub_driver)
        resource_urls = get_resource_urls(list_of_nids)
        detail_nid_tuple = list(
            zip(
                resource_detail_list,
                list_of_nids,
                list_of_file_sizes,
                download_count_list,
                granularity_list,
                published_dates,
                updated_dates,
                reference_urls,
                api_details,
                notes,
                resource_urls,
            )
        )
        csvwriter.write_catalog_data_to_csv(metadata, detail_nid_tuple)
        # get details from the second page onwards..
        for j in range(2, num_of_pages + 1):
            if j > 2:
                break  # TODO remove the following 'if' after test
            print("going to page ", j, " under ", card_link.text)
            sub_sub_driver = webdriver.Chrome(
                options=options, executable_path=path_to_chrome_driver
            )
            master_resource_params = {"page": j}
            master_resource_page_to_get = (
                master_resource_url
                + "?"
                + urllib.parse.urlencode(master_resource_params)
            )
            try:
                sub_sub_driver.get(master_resource_page_to_get)  # open next page
            except:
                logging.warning(
                    "Error loading ",
                    master_resource_page_to_get,
                    " continuing with the next..",
                )
                sub_sub_driver.close()
                continue
            try:
                wait_until_loading(sub_sub_driver, NID_XPATH, 5)
            except:  # TODO this is the possible failure point.. try to make a request by sleeping once
                logging.warning(
                    "error while waiting for... ",
                    master_resource_page_to_get,
                    " trying once more ",
                )
                try:
                    wait_until_loading(sub_sub_driver, NID_XPATH, 15)
                except:
                    logging.warning(
                        "The url ",
                        master_resource_url,
                        " didn't load.. continuing with next",
                    )
                    sub_sub_driver.close()
                    continue
            print("PRINTING ALL LISTS UNDER PAGE 2 ONWARDS....")
            page_nid_list = get_nids(sub_sub_driver)
            resource_detail_list = get_resource_names(sub_sub_driver)
            list_of_file_sizes = get_file_sizes(sub_sub_driver)
            download_count_list = get_download_counts(sub_sub_driver)
            granularity_list = get_granularity_of_all(sub_sub_driver)
            published_dates = get_published_dates(sub_sub_driver)
            updated_dates = get_updated_dates(sub_sub_driver)
            reference_urls = get_reference_urls(sub_sub_driver)
            api_details = get_api_details(sub_sub_driver)
            notes = get_notes(sub_sub_driver)
            resource_urls = get_resource_urls(list_of_nids)
            print(page_nid_list)
            print(resource_detail_list)
            print(list_of_file_sizes)
            detail_nid_tuple = list(
                zip(
                    resource_detail_list,
                    list_of_nids,
                    list_of_file_sizes,
                    download_count_list,
                    granularity_list,
                    published_dates,
                    updated_dates,
                    reference_urls,
                    api_details,
                    notes,
                    resource_urls,
                )
            )
            print("PRINTING DATA FROM SECOND PAGE ONWARDS...")
            print(detail_nid_tuple)
            csvwriter.write_catalog_data_to_csv(metadata, detail_nid_tuple)
            sub_sub_driver.close()
        sub_driver.close()
    params = {"page": page}
    url_to_get = site_url + urllib.parse.urlencode(params)
    driver.close()
    driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
    driver.get(url_to_get)
    time.sleep(2)

print(len(detail_nid_tuple))
print(set(detail_nid_tuple))
print("time taken is ", time.time() - start_time)
