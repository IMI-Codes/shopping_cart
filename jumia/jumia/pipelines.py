# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter # type: ignore
import re

company_pattern = re.compile(r"^\w+")
percentage_pattern = re.compile(r"\d{2}")

class JumiaPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        name = adapter.get("product_name").strip() # type: ignore
        value = company_pattern.search(name) # type: ignore
        company_name = value.group() # type: ignore
        adapter["manufacturer_name"] = company_name
        
        star_value = adapter.get("stars")
        if star_value is not None:
            star_holder = star_value.split("out") # type: ignore
            score_value = float(star_holder[0])
            adapter["stars"] = score_value
        
        percentage_value = adapter.get("discount_percentage")
        if percentage_value is not None:
            percentage_holder = int(percentage_pattern.search(percentage_value).group()) # type: ignore
            adapter["discount_percentage"] = percentage_holder
        
        return item



#save the price to a naira section
#convert the prices to dollar based on black market and normal exchange rate
#save to my db
#schedule daily runs