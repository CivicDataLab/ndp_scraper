header_dict = {
"Accept":"application/json, text/plain, */*",
"Accept-Language":"en-US,en;q=0.9",
"Connection": "keep-alive",
"Content-Type": "application/json;charset=UTF-8",
"Cookie" : "_ga=GA1.3.1806082847.1658141362; _gid=GA1.3.961707762.1658141362",
"Origin" : "https://data.gov.in",
"Referer" : "https://data.gov.in/catalog/xyz",
"Sec-Fetch-Dest" : "empty",
"Sec-Fetch-Mode" : "cors",
"Sec-Fetch-Site" : "same-origin",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
"sec-ch-ua" : '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
"sec-ch-ua-mobile" : "?0",
"sec-ch-ua-platform" : '"Windows"'
}

# Change this accordingly while site gets updated
PAGES_TO_TRAVERSE_IN_SITE = 523

NID_XPATH = "//*[@id='app']/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]"
RESOURCE_DETAIL_XPATH = "//div[@class='card-header']/span"