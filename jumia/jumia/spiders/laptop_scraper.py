import scrapy
from jumia.items  import laptop_Item


class LaptopScraperSpider(scrapy.Spider):
    name = "laptop_scraper"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/laptops/"]

    def parse(self, response): # type: ignore
        products = response.css(".prd")
        item = laptop_Item()
        for product in products:
            official_store = product.css("div._mall ::text").get()
            discount_price = product.css("div.old ::text").get()
            if official_store:
                #test and modify selectors
                
                item["product_name"] = product.css("h3.name ::text").get()#yes
                if discount_price:    
                    item["original_price"] = product.css("div.old ::text").get()#yes
                    item["discount_price"] = product.css("div.prc ::text").get()#yes
                    item['discount_percentage'] = product.css("div._dsct ::text").get()
                else:
                    item["original_price"] = product.css("div.prc ::text").get()
                item["stars"] = product.css("div.stars ::text").get() #yes
                #item["review_count"] = product.xpath('//div[@class="rev"]/text()').get()#modify 
                
                item["product_type"] = "laptop"
                yield item # type: ignore
        next_page_url = response.css('a.pg[aria-label="Next Page"]::attr(href)').get()
        if next_page_url is not None:
            #yield response.follow(next_page, callback=self.parse) # type: ignore
            yield response.follow(next_page_url, callback=self.parse)  # type: ignore
        
