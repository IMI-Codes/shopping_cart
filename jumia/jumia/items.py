# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class earbud_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    manufacturer_name = scrapy.Field()
    original_price = scrapy.Field()
    discount_price = scrapy.Field()
    stars = scrapy.Field()
    reviews = scrapy.Field()
    pass
