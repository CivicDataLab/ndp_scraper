from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.remote.webelement import WebElement

options = Options()
options.add_argument("--window-size=1920,1200")
path_to_chrome_driver = "E:/chromedriver"
driver = webdriver.Chrome(options = options, executable_path = path_to_chrome_driver)
sub_driver = webdriver.Chrome(options = options, executable_path = path_to_chrome_driver)
driver.get("https://data.gov.in/catalogs?page=1")

card_link_by_class = driver.find_element(By.CLASS_NAME, "card-header")
card_link_by_xpath = driver.find_elements(By.XPATH, "//div[@class='card-header']/a")


"""Making a request ... Headers are to be updated using selectors """
payload = '{"name":[{"value":"zcc"}],"uid":[{"value":0}],"ip":[{"value":""}],"usage":[{"value":"2"}],"purpose":[{"value":"5"}],"file_type":[{"value":"csv"}],"export_status":[{"value":"url"}],"email":[{"value":"awd@g.co"}],"catalog_id":[{"target_id":""}],"resource_id":[{"target_id":7105433}]}'

header_dict = {
"Accept":"application/json, text/plain, */*",
"Accept-Language":"en-US,en;q=0.9",
"Connection": "keep-alive",
"Content-Type": "application/json;charset=UTF-8",
"Cookie" : "_ga=GA1.3.1806082847.1658141362; _gid=GA1.3.961707762.1658141362",
"Origin" : "https://data.gov.in",
"Referer" : "https://data.gov.in/catalog/real-time-air-quality-index",
"Sec-Fetch-Dest" : "empty",
"Sec-Fetch-Mode" : "cors",
"Sec-Fetch-Site" : "same-origin",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
"sec-ch-ua" : '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
"sec-ch-ua-mobile" : "?0",
"sec-ch-ua-platform" : '"Windows"'
}

res = requests.post('https://data.gov.in/backend/dms/v1/ogdp/download_purpose?_format=json', data = payload,
                    headers = header_dict)
print(res.content)
print("$$$$$$$$")



# link_text = card_link_by_xpath[0].text
# link = driver.find_element(By.LINK_TEXT, link_text)
# link.click()
# print(len(driver.window_handles))
# window_after = driver.window_handles[0]
# driver.switch_to.window(window_after)
# print(driver.page_source)

master_resource_url = card_link_by_xpath[0].get_attribute("href")
sub_driver.get(master_resource_url)


""" This loop should be kept !!!!!"""
# for card_link in card_link_by_xpath:
#     master_resource_url = card_link.get_attribute("href")
#     sub_driver.get(master_resource_url)

#sub_driver.close()
driver.close()
