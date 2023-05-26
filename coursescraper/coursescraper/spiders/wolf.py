import scrapy


class WolfSpider(scrapy.Spider):
    name = "wolf"
    # allowed_domains = ["udemy.com"]
    start_urls = ["https://udemy.com/", "http://udacity.com"]

    def parse(self, response):
        pass
