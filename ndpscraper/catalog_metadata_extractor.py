import logging

from utils import *


def get_metadata(driver_instance: WebDriver):
    """
    Metadata is fetched only in the first page of the catalog.
    :param driver_instance:WebDriver
    :return: A dictionary containing the metadata of the catalog.
    """
    wait_until_loading(driver_instance, "//span[@title='Click Here To View Info']")
    catalog_info_button = driver_instance.find_element(
        By.XPATH, "//span[@title='Click Here To View Info']"
    )
    catalog_name_xpath = "//li[@class = 'breadcrumb-item active']/span"
    catalog_info_xpath = "//span[@class = 'mb-2 mt-4 catalog_info_desc']"
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
    catalog_metadata = {}
    try:
        driver_instance.execute_script("arguments[0].click();", catalog_info_button)
        time.sleep(0.5)  # wait for sometime until everything is loaded properly
        if xpath_exists(driver_instance, catalog_name_xpath):
            catalog_metadata["Catalog Name"] = driver_instance.find_element(
                By.XPATH, catalog_name_xpath
            ).text
        else:
            catalog_metadata["Catalog Name"] = ""
        if xpath_exists(driver_instance, catalog_info_xpath):
            if xpath_exists(
                driver_instance, catalog_info_xpath + "/following::a"
            ) and driver_instance.find_element(
                By.XPATH, catalog_info_xpath + "/following::a"
            ).text.startswith(
                "More"
            ):
                wait_until_loading(
                    driver_instance, catalog_info_xpath + "/following::a"
                )
                more_button = driver_instance.find_element(
                    By.XPATH, catalog_info_xpath + "/following::a"
                )
                clk = (
                    ActionChains(driver_instance)
                    .move_to_element(more_button)
                    .click()
                    .perform()
                )
                descriptive_info_xpath = "//p[@class = 'mb-2 catalog_info_desc']/p"
                wait_until_loading(driver_instance, descriptive_info_xpath)
                catalog_metadata["Catalog Info"] = driver_instance.find_element(
                    By.XPATH, descriptive_info_xpath
                ).text
            elif xpath_exists(driver_instance, catalog_info_xpath + "/p"):
                catalog_metadata["Catalog Info"] = driver_instance.find_element(
                    By.XPATH, catalog_info_xpath + "/p"
                ).text
            else:
                catalog_metadata["Catalog Info"] = ""
        if xpath_exists(driver_instance, released_under_xpath):
            catalog_metadata["Released Under"] = driver_instance.find_element(
                By.XPATH, released_under_xpath
            ).text
        else:
            catalog_metadata["Released Under"] = ""
        wait_until_loading(driver_instance, contributor_xpath)  # xpath for contributor
        if xpath_exists(driver_instance, contributor_xpath):
            contributor_elements = driver_instance.find_elements(
                By.XPATH, contributor_xpath
            )
            contributors_list = []
            for element in contributor_elements:
                contributors_list.append(element.get_attribute("innerHTML"))
            catalog_metadata["Contributor"] = contributors_list
        else:
            catalog_metadata["Contributor"] = [""]
        if xpath_exists(driver_instance, keywords_xpath):
            keyword_elements = driver_instance.find_elements(By.XPATH, keywords_xpath)
            keywords_list = []
            for element in keyword_elements:
                keywords_list.append(element.get_attribute("innerHTML"))
            catalog_metadata["Keywords"] = keywords_list
        else:
            catalog_metadata["Keywords"] = [""]
        if xpath_exists(driver_instance, group_xpath):
            group_elements = driver_instance.find_elements(By.XPATH, group_xpath)
            groups_list = []
            for element in group_elements:
                groups_list.append(element.get_attribute("innerHTML"))
            catalog_metadata["Group"] = groups_list
        else:
            catalog_metadata["Group"] = [""]
        if xpath_exists(driver_instance, sector_xpath):
            sector_elements = driver_instance.find_elements(By.XPATH, sector_xpath)
            sectors_list = []
            for element in sector_elements:
                sectors_list.append(element.get_attribute("innerHTML"))
            catalog_metadata["Sectors"] = sectors_list
        else:
            catalog_metadata["Sectors"] = [""]
        if xpath_exists(driver_instance, published_on_xpath):
            catalog_metadata["Published On"] = driver_instance.find_element(
                By.XPATH, published_on_xpath
            ).get_attribute("innerHTML")
        else:
            catalog_metadata["Published On"] = ""
        if xpath_exists(driver_instance, updated_on_xpath):
            catalog_metadata["Updated On"] = driver_instance.find_element(
                By.XPATH, updated_on_xpath
            ).get_attribute("innerHTML")
        else:
            catalog_metadata["Updated On"] = ""
        if xpath_exists(driver_instance, domain_xpath):
            catalog_metadata["Domain"] = driver_instance.find_element(
                By.XPATH, domain_xpath
            ).get_attribute("innerHTML")
        else:
            catalog_metadata["Domain"] = ""
        if xpath_exists(driver_instance, cdo_name_xpath):
            catalog_metadata["CDO Name"] = driver_instance.find_element(
                By.XPATH, cdo_name_xpath
            ).text
        else:
            catalog_metadata["CDO Name"] = ""
        if xpath_exists(driver_instance, cdo_post_xpath):
            catalog_metadata["CDO Post"] = driver_instance.find_element(
                By.XPATH, cdo_post_xpath
            ).text
        else:
            catalog_metadata["CDO Post"] = ""
        # Ministry name can be long and can only be extracted when hovered over it
        if xpath_exists(driver_instance, ministry_name_xpath):
            try:
                tool_tip = WebDriverWait(driver_instance, 3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[@class='details col-6']/h3")
                    )
                )
                hov = ActionChains(driver_instance).move_to_element(tool_tip).perform()
                wait_until_loading(driver_instance, "//div[@class='popover-body']")
                ministry_name = driver_instance.find_element(
                    By.XPATH, "//div[@class='popover-body']"
                ).text
                catalog_metadata["Ministry/State/Department"] = ministry_name
            except:
                logging.warning("Ministry name isn't intractable")
        else:
            catalog_metadata["Ministry/State/Department"] = ""
        if xpath_exists(driver_instance, phone_number_xpath):
            catalog_metadata["Phone"] = driver_instance.find_element(
                By.XPATH, phone_number_xpath
            ).text
        else:
            catalog_metadata["Phone"] = ""
        if xpath_exists(driver_instance, email_xpath):
            catalog_metadata["Email"] = driver_instance.find_element(
                By.XPATH, email_xpath
            ).text
        else:
            catalog_metadata["Email"] = ""
        # even address is extracted by hovering
        if xpath_exists(driver_instance, address_xpath):
            try:
                tool_tip = WebDriverWait(driver_instance, 3).until(
                    EC.presence_of_element_located((By.XPATH, address_xpath))
                )
                hov = ActionChains(driver_instance).move_to_element(tool_tip).perform()
                wait_until_loading(driver_instance, "//div[@class='popover-body']")
                address = driver_instance.find_element(
                    By.XPATH, "//div[@class='popover-body']"
                ).text
                catalog_metadata["Address"] = address
            except:
                logging.warning("Address not intractable")
        else:
            catalog_metadata["Address"] = ""
        print("########", catalog_metadata)
        return catalog_metadata
    except:
        logging.warning("Catalog button isn't clickable..")
