# importing the scrapy module
import scrapy
from scrapy import FormRequest


class ExtractUrls(scrapy.Spider):
    name = "extract"

    # request function
    def start_requests(self):
        urls = [ 'https://data.gov.in/catalogs', ]

        yield scrapy.Request(url = urls[0], callback = self.parse)

    # Parse function
    def parse(self, response):
        print(response.body)
        # Extra feature to get title
        count_of_dataset = response.xpath("//span/text()").get()
        print("HEREEEEEE",count_of_dataset)

        # Get anchor tags
        links = response.css('a::attr(href)').extract()
        print(links)

        print("**********")
        yield self.executeCurl()
        # for link in links:
        #     yield
        #     {
        #         'title': title,
        #         'links': link
        #     }
        #
        #     if 'geeksforgeeks' in link:
        #         yield scrapy.Request(url = link, callback = self.parse)
    def executeCurl(self):
        return FormRequest(url = "https://data.gov.in/catalogs",
                           formdata={
                               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6,lb;q=0.5,sv;q=0.4,sq;q=0.3,id;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.3.1399924205.1657692630; _gid=GA1.3.659871719.1657692630",
        "DNT": "1",
        "Host": "data.gov.in",
              "If-Modified-Since": "Thu, 07 Jul 2022 04:58:33 GMT",
        "Referer": 'https://data.gov.in/',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
        },
                        callback=self.click_advocate_name_icon)

    def click_advocate_name_icon(self, response):
        print(response.body)