""" Entry point to scrape https://data.gov.in/catalogs? site."""

# kcc
import logging
import time

import csv_writer
from catalog_metadata_scraper import get_metadata
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utility_methods import *
from const_variables import *

options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-gpu")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)

next_page_btn_xpath = "//button[@aria-label='Go to next page']"
list_view_btn_xpath = "//a[@title='List View']"
grid_view_btn_xpath = "//a[@title='Grid View']"
start_time = time.time()
main_page_no = 148

while True:
    driver.get("https://data.gov.in/catalogs?page=" + str(main_page_no))
    print("scraping page no. ", main_page_no)
    card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
    resource_links_in_page = []
    for card_link in card_link_by_xpath:
        resource_links_in_page.append(card_link.get_attribute("href"))
    for resource_link in resource_links_in_page:
        driver.get(resource_link)
        # loop to traverse all the resources
        resource_page_no = 0
        while True:
            # get metadata at the very first page. no need to scrape again in the upcoming pages as catalog metadata
            # remains same.
            if resource_page_no == 0:
                metadata = get_metadata(driver)
            list_view_btn = driver.find_element(By.XPATH, list_view_btn_xpath)
            driver.execute_script("arguments[0].click();", list_view_btn)
            # only names and notes are scraped in list view
            names = get_resource_names(driver, card_header_xpath)
            notes = get_notes(driver, notes_xpath)
            # print("names", names)
            # print("notes", notes)

            # # all other data are scraped in grid view
            grid_view_btn = driver.find_element(By.XPATH, grid_view_btn_xpath)
            driver.execute_script("arguments[0].click();", grid_view_btn)
            page_nid_list = get_nids(driver, nid_xpath)
            # print("nids ", page_nid_list)
            list_of_file_sizes = get_file_sizes(driver, file_size_xpath)
            # print("sizesss", list_of_file_sizes)
            download_count_list = get_download_counts(driver, downloads_xpath)
            # print("download counts", download_count_list)
            granularity_list = get_granularity_of_all(driver, granularity_xpath)
            # print("granularity", granularity_list)
            published_dates = get_published_dates(driver, published_date_xpath)
            # print("pub dates", published_dates)
            updated_dates = get_updated_dates(driver, updated_date_xpath)
            # print("up dates", updated_dates)
            reference_urls = get_reference_urls(driver, reference_url_xpath)
            # print("ref url", reference_urls)
            api_details = get_api_details(driver, api_xpath)
            # print("api data", api_details)
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
            # print(scraped_data)
            csv_writer.write_catalog_data_to_csv(metadata, scraped_data, col_names)
            if xpath_exists(driver, next_page_btn_xpath):
                resource_page_no += 1  # increment the page no. so that metadata isn't scraped again
                next_page_btn = driver.find_element(By.XPATH, next_page_btn_xpath)
                driver.execute_script("arguments[0].click();", next_page_btn)
            else:
                break
    #  print("Scraped page no.", main_page_no)
    main_page_no += 1
    if main_page_no == PAGES_TO_TRAVERSE_IN_SITE + 1:
        driver.close()
        break

print("took ", time.time() - start_time, " seconds")
