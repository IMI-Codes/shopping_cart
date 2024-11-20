import scrapy
from jumia.items  import earbud_Item

class headsetSpider(scrapy.Spider):
    name = "headset_scraper"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/mobile-phone-bluetooth-headsets/"]

    def parse(self, response) -> None: # type: ignore
        products = response.css(".prd")
        item = earbud_Item()
        for product in products:
            official_store = product.css("div._mall ::text").get()
            if official_store:
                #test and modify selectors
                item["product_name"] = product.css("h3.name ::text").get()#yes
                item["original_price"] = product.css("div.old ::text").get()#yes
                item["discount_price"] = product.css("div.prc ::text").get()#yes
                item["stars"] = product.css("div.stars ::text").get() #yes
                #item["review_count"] = product.xpath('//div[@class="rev"]/text()').get()#modify 
                item['discount_percentage'] = product.css("div._dsct ::text").get()
                yield item # type: ignore
        next_page_url = response.css('a.pg[aria-label="Next Page"]::attr(href)').get()
        if next_page_url is not None:
            #yield response.follow(next_page, callback=self.parse) # type: ignore
            yield response.follow(next_page_url, callback=self.parse)  # type: ignore
        