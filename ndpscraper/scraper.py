# kcc

import logging
import math
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
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


def wait_until_loading(driver_instance: WebDriver, xpath: str, delay=3):
    if delay == 3:
        print("new delay is : ", delay)
    WebDriverWait(driver_instance, delay).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def scroll_to_top(driver_instance: WebDriver):
    driver_instance.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.HOME)

def xpath_exists(driver: WebDriver, xpath: str):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def calculate_num_of_pages(driver_instance: WebDriver):
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
        print(records_in_page)
        num_of_pages = math.ceil(total_count / records_in_page)
        return num_of_pages
    else:
        return 0


def get_nids(driver: WebDriver):
    pass


def get_metadata(driver: WebDriver):
    wait_until_loading(driver, "//span[@title='Click Here To View Info']")
    catalog_info_button = driver.find_element(
        By.XPATH, "//span[@title='Click Here To View Info']"
    )
    catalog_name_xpath = "//li[@class = 'breadcrumb-item active']/span"
    catalog_info_xpath = "//span[@class = 'mb-2 mt-4 catalog_info_desc']/p"
    released_under_xpath = "//*[@id='accordion-1']/div/div/div/ul/li/a"
    contributor_xpath = "//*[@id='accordion-2']/div/p/div/*/*/a"
    keywords_xpath = "//*[@id='accordion-3']/div/p/div/a"
    group_xpath = "//*[@id='accordion-4']/div/p/div/a"
    sector_xpath = "//*[@id='accordion-5']/div/p/div/a"
    published_on_xpath = "//*[@id='accordion-6']/div/div/div/ul/li"
    updated_on_xpath = "//*[@id='accordion-7']/div/div/div/ul/li"
    domain_xpath = "//*[@id='accordion-8']/div/div/div/div/p"
    # //*[@id="accordion-8"]/div/div/div/div/p
    cdo_name_xpath = "//h3[@class = 'cdo_name m-0']"
    cdo_post_xpath = "//p[@class='cdo_post m-0']"
    ministry_name_xpath = "//div[@class='details col-6']/h3"
    phone_number_xpath = (
        "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/h3"
    )
    email_xpath = (
        "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[3]/h3"
    )
    address_xpath = (
        "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[4]/div[3]"
    )
    metadata = metadata_dict
    try:
        driver.execute_script("arguments[0].click();", catalog_info_button)
        if xpath_exists(driver, catalog_name_xpath):
            metadata["Catalog Name"] = driver.find_element(
                By.XPATH, catalog_name_xpath
            ).text
        if xpath_exists(driver, catalog_info_xpath):
            metadata["Catalog Info"] = driver.find_element(
                By.XPATH, catalog_info_xpath
            ).text
        if xpath_exists(driver, released_under_xpath):
            metadata["Released Under"] = driver.find_element(
                By.XPATH, released_under_xpath
            ).text

        wait_until_loading(driver, contributor_xpath)  # xpath for contributor
        if xpath_exists(driver, contributor_xpath):
            contributor_elements = driver.find_elements(By.XPATH, contributor_xpath)
            contributors_list = []
            for element in contributor_elements:
                contributors_list.append(element.get_attribute("innerHTML"))
            metadata["Contributor"] = contributors_list

        if xpath_exists(driver, keywords_xpath):
            keyword_elements = driver.find_elements(By.XPATH, keywords_xpath)
            keywords_list = []
            for element in keyword_elements:
                keywords_list.append(element.get_attribute("innerHTML"))
            metadata["Keywords"] = keywords_list

        if xpath_exists(driver, group_xpath):
            group_elements = driver.find_elements(By.XPATH, group_xpath)
            groups_list = []
            for element in group_elements:
                groups_list.append(element.get_attribute("innerHTML"))
            metadata["Group"] = groups_list

        if xpath_exists(driver, sector_xpath):
            sector_elements = driver.find_elements(By.XPATH, sector_xpath)
            sectors_list = []
            for element in sector_elements:
                sectors_list.append(element.get_attribute("innerHTML"))
            metadata["Sectors"] = sectors_list

        if xpath_exists(driver, published_on_xpath):
            metadata["Published On"] = driver.find_element(
                By.XPATH, published_on_xpath
            ).get_attribute("innerHTML")

        if xpath_exists(driver, updated_on_xpath):
            metadata["Updated On"] = driver.find_element(
                By.XPATH, updated_on_xpath
            ).get_attribute("innerHTML")

        if xpath_exists(driver, domain_xpath):
            metadata["Domain"] = driver.find_element(
                By.XPATH, domain_xpath
            ).get_attribute("innerHTML")

        if xpath_exists(driver, cdo_name_xpath):
            metadata["CDO Name"] = driver.find_element(By.XPATH, cdo_name_xpath).text
        if xpath_exists(driver, cdo_post_xpath):
            metadata["CDO Post"] = (driver.find_element(By.XPATH, cdo_post_xpath).text,)

        # Ministry name can be long and can only be extracted when hovered over it
        if xpath_exists(driver, ministry_name_xpath):
            try:
                toolTip = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[@class='details col-6']/h3")
                    )
                )
                hov = ActionChains(driver).move_to_element(toolTip).perform()
                wait_until_loading(driver, "//div[@class='popover-body']")
                ministry_name = driver.find_element(
                    By.XPATH, "//div[@class='popover-body']"
                ).text
                metadata["Ministry/State/Department"] = ministry_name
            except:
                logging.warning("Ministry name isn't intractable")
        if xpath_exists(driver, phone_number_xpath):
            metadata["Phone"] = (
                driver.find_element(By.XPATH, phone_number_xpath).text,
            )
        if xpath_exists(driver, email_xpath):
            metadata["Email"] = (driver.find_element(By.XPATH, email_xpath).text,)
        # even address is extracted by hovering
        if xpath_exists(driver, address_xpath):
            try:
                toolTip = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, address_xpath))
                )
                hov = ActionChains(driver).move_to_element(toolTip).perform()
                wait_until_loading(driver, "//div[@class='popover-body']")
                address = driver.find_element(
                    By.XPATH, "//div[@class='popover-body']"
                ).text
                metadata["Address"] = address
            except:
                logging.warning("Address not intractable")
        print("########", metadata)
        return metadata
    except:
        logging.warning("Catalog button isn't clickable..")


def get_file_sizes(driver_instance: WebDriver):
    file_sizes = []
    file_size_xpath = "//label[@title = 'File Size']/following::strong[1]"
    if xpath_exists(driver_instance, file_size_xpath):
        file_size_elements = driver_instance.find_elements(By.XPATH, file_size_xpath)
        for element in file_size_elements:
            file_sizes.append(element.text)
    return file_sizes


def get_download_counts(driver_instance: WebDriver):
    downloads_count = []
    downloads_xpath = "//label[@title = 'Download']/following::strong[1]"
    if xpath_exists(driver_instance, downloads_xpath):
        download_count_elements = driver_instance.find_elements(By.XPATH, downloads_xpath)
        for element in download_count_elements:
            downloads_count.append(element.text)
    return downloads_count


def get_granularity_of_all(driver_instance:WebDriver):
    granularity_list = []
    granularity_xpath = "//label[@title = 'Granularity']/following::strong[1]"
    if xpath_exists(driver_instance, granularity_xpath):
        granularity = driver_instance.find_elements(By.XPATH, granularity_xpath)
        for element in granularity:
            granularity_list.append(element.text)
    return granularity_list


def get_published_dates(driver_instance:WebDriver):
    published_dates_list = []
    published_date_xpath = "//label[@title = 'Published on:']/following::strong[1]"
    if xpath_exists(driver_instance, published_date_xpath):
        published_dates_elements = driver_instance.find_elements(By.XPATH, published_date_xpath)
        for element in published_dates_elements:
            published_dates_list.append(element.text)
    return published_dates_list


def get_updated_dates(driver_instance:WebDriver):
    updated_dates_list = []
    updated_date_xpath = "//label[@title = 'Updated on:']/following::strong[1]"
    if xpath_exists(driver_instance, updated_date_xpath):
        updated_dates_elements = driver_instance.find_elements(By.XPATH, updated_date_xpath)
        for element in updated_dates_elements:
            updated_dates_list.append(element.text)
    return updated_dates_list


def get_reference_urls(driver_instance: WebDriver):
    reference_urls = []
    reference_url_xpath = "//div[@class='CR_strip col-12'][1]/div/div[3]"
    if xpath_exists(driver_instance, reference_url_xpath):
        reference_url_elements = driver_instance.find_elements(By.XPATH, reference_url_xpath)
        for element in reference_url_elements:
            reference_urls.append(element.text)
    return reference_urls

def get_api_details(driver_instance:WebDriver):
    api_list = []
    api_xpath = "//div[@class='CR_strip col-12'][2]/div/div[3]"
    if xpath_exists(driver_instance, api_xpath):
        api_elements = driver_instance.find_elements(By.XPATH, api_xpath)
        for element in api_elements:
            api_name = element.text
            # usually the name will be NA or something else. If na - no link else some link will be there
            if len(api_name) > 2:
                api_link = element.find_element(By.XPATH, "./*/*/a").get_attribute("href")
                api_list.append((api_name, api_link))
            else:
                api_list.append((api_name, "No link available"))
    return api_list


def get_notes(driver_instance: WebDriver):
    notes_list = []
    notes_xpath = "//div[@class='pr-0 col-12']/div/div/div"
    if xpath_exists(driver_instance, notes_xpath):
        scroll_to_top(driver_instance)
        time.sleep(1)
        notes_elements = driver_instance.find_elements(By.XPATH, notes_xpath)
        for element in notes_elements:
            element_not_found = True
            y = 10
            while element_not_found:
                try:
                    ActionChains(driver_instance).scroll_by_amount(0, y).perform()
                    time.sleep(1)
                    hov = ActionChains(driver_instance).move_to_element(element).perform()
                    wait_until_loading(driver_instance, "//div[@class='popover-body']")
                    note = driver_instance.find_element(
                        By.XPATH, "//div[@class='popover-body']"
                    ).text
                    notes_list.append(note)
                    element_not_found = False
                except:
                    y += 35
    return notes_list


def get_resource_names(driver: WebDriver):
    resource_name_list = []
    card_header_xpath = "//div[@class='card-header']/span"
    if xpath_exists(driver, card_header_xpath):
        tool_tips_real = driver.find_elements(By.XPATH, card_header_xpath)
        tool_tips_real.pop(0)
        for element in tool_tips_real:
            element_not_found = True
            y = 10
            while element_not_found:
                try:
                    ActionChains(driver).scroll_by_amount(0, y).perform()
                    time.sleep(1)
                    hov = ActionChains(driver).move_to_element(element).perform()
                    wait_until_loading(driver, "//div[@class='popover-body']")
                    name = driver.find_element(
                        By.XPATH, "//div[@class='popover-body']"
                    ).text
                    resource_name_list.append(name)
                    element_not_found = False
                except:
                    y += 35
    return resource_name_list


options = Options()
options.add_argument("--window-size=1920,1200")
options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-gpu")
options.add_argument("headless")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=path_to_chrome_driver)
# phantom
site_url = "https://data.gov.in/catalogs?"

start_time = time.time()

driver.get("https://data.gov.in/catalogs?page=1")

detail_nid_tuple = ()
for page in range(
    2, 3
):  # TODO change the upper limit to total num of pages while prod run
    print("inside main page ", page)
    wait_until_loading(driver, "//div[@class='card-header']/a")
    card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")
    logging.info("recieved resource links ->", card_link_by_xpath)
    # [link1, link2, link3....]
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
        get_metadata(sub_driver)
        # time.sleep(8)
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
            resource_detail_list = get_resource_names(sub_driver)
            # resource_detail_list = get_resource_details(sub_driver)
        except:
            logging.warning(
                "Error getting details from the page.. ",
                master_resource_url,
                " moving on to the next page..",
            )
            sub_driver.close()
            continue
        list_of_nids = []
        for nid in page_nid_list:
            list_of_nids.append(
                nid.get_attribute("nid")
            )  # once calculated, get nids by
            # visiting all the other pages...
        print("CHECKING LENGTH%%%%%", len(resource_detail_list), len(list_of_nids))

        list_of_file_sizes = get_file_sizes(sub_driver)
        download_count_list = get_download_counts(sub_driver)
        granularity_list = get_granularity_of_all(sub_driver)
        published_dates = get_published_dates(sub_driver)
        updated_dates = get_updated_dates(sub_driver)
        reference_urls = get_reference_urls(sub_driver)
        api_details = get_api_details(sub_driver)
        notes = get_notes(sub_driver)
        detail_nid_tuple = detail_nid_tuple + tuple(
            zip(resource_detail_list, list_of_nids, list_of_file_sizes, download_count_list, granularity_list,
                published_dates, updated_dates, reference_urls, api_details, notes)
        )
        resource_detail_list.clear()
        list_of_nids.clear()
        list_of_file_sizes.clear()
        download_count_list.clear()
        granularity_list.clear()
        published_dates.clear()
        updated_dates.clear()
        reference_urls.clear()
        api_details.clear()
        notes.clear()
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
            page_nid_list = sub_sub_driver.find_elements(By.XPATH, NID_XPATH)
            for nid_index in range(len(page_nid_list)):
                list_of_nids.append(page_nid_list[nid_index].get_attribute("nid"))

            resource_detail_list = get_resource_names(sub_sub_driver)
            list_of_file_sizes = get_file_sizes(sub_sub_driver)
            download_count_list = get_download_counts(sub_sub_driver)
            granularity_list = get_granularity_of_all(sub_sub_driver)
            published_dates = get_published_dates(sub_sub_driver)
            updated_dates = get_updated_dates(sub_sub_driver)
            reference_urls = get_reference_urls(sub_sub_driver)
            api_details = get_api_details(sub_sub_driver)
            notes = get_notes(sub_sub_driver)

            detail_nid_tuple = detail_nid_tuple + tuple(
                zip(resource_detail_list, list_of_nids, list_of_file_sizes, download_count_list, granularity_list,
                    published_dates, updated_dates, reference_urls, api_details, notes)
            )
            # clearing all the lists
            resource_detail_list.clear()
            list_of_nids.clear()
            list_of_file_sizes.clear()
            download_count_list.clear()
            granularity_list.clear()
            published_dates.clear()
            updated_dates.clear()
            reference_urls.clear()
            api_details.clear()
            notes.clear()

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

"""Making a request ... Headers are to be updated using selectors """
payload = (
    '{"name":[{"value":"zcc"}],'
    '"uid":[{"value":0}],'
    '"ip":[{"value":""}],'
    '"usage":[{"value":"2"}],'
    '"purpose":[{"value":"5"}],'
    '"file_type":[{"value":"csv"}],'
    '"export_status":[{"value":"url"}],'
    '"email":[{"value":"awd@g.co"}],'
    '"catalog_id":[{"target_id":""}],'
    '"resource_id":[{"target_id":6720073}]}'
)

header = header_dict

res = requests.post(
    "https://data.gov.in/backend/dms/v1/ogdp/download_purpose?_format=json",
    data=payload,
    headers=header_dict,
)
print(res.content)
print("$$$$$$$$")
