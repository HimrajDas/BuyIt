import scrapy


class WolfSpider(scrapy.Spider):
    name = "wolf"
    allowed_domains = ["udemy.com"]
    start_urls = ["https://www.udemy.com/courses/search/?src=ukw&q="]

    def parse(self, response):
        
