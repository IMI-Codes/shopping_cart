# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter # type: ignore
import re
#'https://api.currencyfreaks.com/v2.0/rates/latest?apikey=YOUR_APIKEY&symbols=PKR,GBP,EUR,USD'
API_KEY = f"065306e22aaf41b188d66e888365a91e"
BASE_URL = f"https://api.currencyfreaks.com/v2.0/rates/latest?"
symbol = "NGN"
company_pattern = re.compile(r"^\w+")
percentage_pattern = re.compile(r"\d{2}")
price_pattern = re.compile(r"\d+")
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
        if percentage_value  != None:
            percentage_holder = int(percentage_pattern.search(percentage_value).group()) # type: ignore
            adapter["discount_percentage"] = percentage_holder
        discount_price = adapter.get("discount_price_naira")
        original_price = adapter.get("original_price_naira")
        
        #remove naira sign and remove comma and fuse numbers
        if discount_price is not None:
            discount_holder = discount_price
            original_holder = original_price
            
            values_discount = price_pattern.findall(discount_holder)
            values_original = price_pattern.findall(original_holder) # type: ignore
            
            holder_discount = ""
            holder_original = ""
            
            for value in values_discount:
                holder_discount = holder_discount + value
            for value in values_original:
                holder_original = holder_original + value  # type: ignore
            
            adapter["discount_price_naira"] = int(holder_discount)
            adapter["original_price_naira"] = int(holder_original)
        else:
            original_holder = original_price
            values_original = price_pattern.findall(original_holder) # type: ignore
            holder_original = ""
            for value in values_original:
                holder_original = holder_original + value  # type: ignore
            adapter["original_price_naira"] = int(holder_original)
            
        
        #get naria to dollar rate
        
        
        #mulitply dollar rate v naira rate and get price in dollar
        
        
        
        #saving the values  dollar
        
        
        
        

        return item
# pipelines.py

import mysql.connector

class SaveToMySQLPipeline: # type: ignore


    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'manasseh',
            database = 'wish_list'
        )

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()
        
        ## Create books table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS placeholder(
            id int NOT NULL auto_increment, 
            url VARCHAR(255),
            title text,
            upc VARCHAR(255),
            product_type VARCHAR(255),
            price_excl_tax DECIMAL,
            price_incl_tax DECIMAL,
            tax DECIMAL,
            price DECIMAL,
            availability INTEGER,
            num_reviews INTEGER,
            stars INTEGER,
            category VARCHAR(255),
            description text,
            PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):
        return item




"""
import currencyapicom


result = client.historical('01-01-2022')
print(result)
 
"""
#convert the prices to dollar based on black market and normal exchange rate
#save to my db
#schedule daily runs
