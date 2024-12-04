import scrapy


class TrainingEquipmentSpider(scrapy.Spider):
    name = "training_equipment_scraper"
    allowed_domains = ["www.prozis.com"]
    start_urls = ["https://www.prozis.com/ww/en/tech-home/home-gym/training-equipment"]

    def parse(self, response): # type: ignore
        pass
