""" The file contains the variables that have large values and are constant across all the pages"""

header_dict = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_ga=GA1.3.1806082847.1658141362; _gid=GA1.3.961707762.1658141362",
    "Origin": "https://data.gov.in",
    "Referer": "https://data.gov.in/catalog/xyz",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
    "sec-ch-ua": '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

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

# Change this accordingly while site gets updated
PAGES_TO_TRAVERSE_IN_SITE = 523

NID_XPATH = "//*[@id='app']/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]"

metadata_dict = {
    "Catalog Name": "",
    "Catalog Info": "",
    "Released Under": "",
    "Contributor": "",
    "Keywords": "",
    "Group": "",
    "Sectors": "",
    "Published On": "",
    "Updated On": "",
    "Domain": "",
    "CDO Name": "",
    "CDO Post": "",
    "Ministry/State/Department": "",
    "Phone": "",
    "Email": "",
    "Address": "",
}

card_header_xpath = "(//div[@class='card-header']/span)"
notes_xpath = "(//span[@class='note_text'])"
reference_url_xpath = "(//div[@class='CR_strip col-12'][1]/div/div[3])"
api_xpath = "(//div[@class='CR_strip col-12'][2]/div/div[3])"
nid_xpath = "(//*[@id='app']/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2])"
file_size_xpath = "(//label[@title = 'File Size']/following::strong[1])"
downloads_xpath = "(//label[@title = 'Download']/following::strong[1])"
granularity_xpath = "(//label[@title = 'Granularity']/following::strong[1])"
published_date_xpath = "(//label[@title = 'Published on:']/following::strong[1])"
updated_date_xpath = "(//label[@title = 'Updated on:']/following::strong[1])"

col_names = [
        "Catalog Name",
        "Catalog Info",
        "Released Under",
        "Contributor",
        "Keywords",
        "Group",
        "Sectors",
        "Catalog Published On",
        "Catalog Updated On",
        "Domain",
        "CDO Name",
        "CDO Post",
        "Ministry/State/Department",
        "Phone",
        "Email",
        "Address",
        "Resource",
        "NID",
        "File Size",
        "Downloads",
        "Granularity",
        "Resource Published On",
        "Resource Updated On",
        "Reference URL",
        "Sourced webservices/APIs",
        "Note"
    ]