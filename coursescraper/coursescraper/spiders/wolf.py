import scrapy
import logging
# from scrapy import signals
# from scrapy.http import HtmlResponse
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from scrapy_playwright.page import PageMethod


# PATH = "C:\Program Files (x86)\chromedriver.exe"


class WolfSpider(scrapy.Spider):
    name = "wolf"
    # allowed_domains = ["udemy.com"]
    # start_urls = ["https://www.udemy.com/courses/search/?src=ukw&q=machine+learning"]


    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(WolfSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
    #     return spider
    

    # def __init__(self, *args, **kwargs):
    #     self.driver = webdriver.Chrome(service=Service(PATH))
    #     super(WolfSpider, self).__init__(*args, **kwargs)

    
    # def spider_closed(self, spider):
    #     self.driver.quit()



    




    def parse(self, response):
        course_titles = response.css(".course-card--course-title--vVEjC a::text").getall()
        for title in course_titles:
            self.logger.info("Course Title: %s", title)




# set up logging
logging.basicConfig(
    filename="scrapy.log",
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    level=logging.INFO
)

