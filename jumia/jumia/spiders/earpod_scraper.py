import scrapy
from items import earbud_Item

class headsetSpider(scrapy.Spider):
    name = "headset_scraper"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/mobile-phone-bluetooth-headsets/"]

    def parse(self, response) -> None: # type: ignore
        products = response.css(".prd")
        item = earbud_Item()
        for product in products:
            official_store = product.xpath('.//div[@class="bdg" and contains(text(), "Official Store")]')
            #product.css(".bdg::text").get() too vague
            if official_store:
                #test and modify selectors
                item["product_name"] = product.css("h3.name ::text").get()#yes
                item["original_price"] = product.css("div.old ::text").get()#yes
                item["discount_price"] = product.css("div.prc ::text").get()#yes
                item["stars"] = product.css("div.stars ::text").get() #yes
                item["review_count"] = product.css("div.rev ::text").get() #modify
            yield item # type: ignore
