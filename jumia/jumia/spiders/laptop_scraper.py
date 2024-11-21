import scrapy


class LaptopScraperSpider(scrapy.Spider):
    name = "laptop_scraper"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/laptops/"]

    def parse(self, response): # type: ignore
        pass
