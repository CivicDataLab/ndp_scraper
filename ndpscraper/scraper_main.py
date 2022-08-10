""" Entry point to scrape https://data.gov.in/catalogs? site."""

# kcc
import logging
import time

import csvwriter
from catalog_metadata_extractor import get_metadata
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import *

options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-gpu")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
site_url = "https://data.gov.in/catalogs?"

next_page_btn_xpath = "//button[@aria-label='Go to next page']"
list_view_btn_xpath = "//a[@title='List View']"
grid_view_btn_xpath = "//a[@title='Grid View']"
start_time = time.time()
# TODO change the below for loop to while loop in prod. for helps while testing to specify page no.s explicitly
for page in range(146, 149):
    driver.get("https://data.gov.in/catalogs?page=" + str(page))
    card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
    resource_links_in_page = []
    for card_link in card_link_by_xpath:
        resource_links_in_page.append(card_link.get_attribute("href"))
    for link in resource_links_in_page:
        driver.get(link)
        # loop to traverse all the resources
        resource_page_no = 0
        while True:
            print("in while again..")
            time.sleep(1)
            # get metadata at the very first page. no need to scrape again in the upcoming pages as catalog metadata
            # remains same.
            if resource_page_no == 0:
                metadata = get_metadata(driver)
            list_view_btn = driver.find_element(By.XPATH, list_view_btn_xpath)
            driver.execute_script("arguments[0].click();", list_view_btn)
            # only names and notes are scraped in list view
            names = get_resource_names(driver)
            notes = get_notes(driver)
            print("names", names)
            print("notes", notes)
            # all other data are scraped in grid view
            grid_view_btn = driver.find_element(By.XPATH, grid_view_btn_xpath)
            driver.execute_script("arguments[0].click();", grid_view_btn)
            page_nid_list = get_nids(driver)
            print("nids ", page_nid_list)
            list_of_file_sizes = get_file_sizes(driver)
            print("sizesss", list_of_file_sizes)
            download_count_list = get_download_counts(driver)
            print("download counts", download_count_list)
            granularity_list = get_granularity_of_all(driver)
            print("granularity", granularity_list)
            published_dates = get_published_dates(driver)
            print("pub dates", published_dates)
            updated_dates = get_updated_dates(driver)
            print("up dates", updated_dates)
            reference_urls = get_reference_urls(driver)
            print("ref url", reference_urls)
            api_details = get_api_details(driver)
            print("api data", api_details)
            scraped_data = list(
                zip(
                    names,
                    page_nid_list,
                    list_of_file_sizes,
                    download_count_list,
                    granularity_list,
                    published_dates,
                    updated_dates,
                    reference_urls,
                    api_details,
                    notes,
                )
            )
            print(scraped_data)
            csvwriter.write_catalog_data_to_csv(metadata, scraped_data)
            if xpath_exists(driver, next_page_btn_xpath):
                resource_page_no += 1
                next_page_btn = driver.find_element(By.XPATH, next_page_btn_xpath)
                driver.execute_script("arguments[0].click();", next_page_btn)
            else:
                break

print("took ", time.time() - start_time, " seconds")
