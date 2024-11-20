# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class shopping_Item(scrapy.Item):
    product_name = scrapy.Field()
    original_price = scrapy.Field()
    discount_price = scrapy.Field()
    stars = scrapy.Field()
    review_count = scrapy.Field()
    discount_percentage = scrapy.Field()
    
class earbud_Item(shopping_Item): # type: ignore
    manufacturer_name = scrapy.Field()
