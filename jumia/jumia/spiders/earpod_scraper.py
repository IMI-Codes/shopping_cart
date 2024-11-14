import scrapy
from items import earbud_Item

class headsetSpider(scrapy.Spider):
    name = "headset_scraper"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/mobile-phone-bluetooth-headsets/"]

    def parse(self, response) -> None: # type: ignore
        products = response.css(".prd")
        
