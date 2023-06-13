import scrapy
from urllib.parse import urlencode


SCRAPEOPS_API_KEY = "0f1478a6-e418-4393-b9a9-dc3edf2c9689"

def get_scrapeops_url(url):
    payload = {
        "api_key": SCRAPEOPS_API_KEY,
        "url": url,
        "bypass": "cloudflare",
        "render_js": True,
    }

    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


# add 'render_js': True in the payload if above code deosn't work.


class WolfSpider(scrapy.Spider):
    name = "wolf"

    custom_setting = {
        "FEEDS": {
            "data.json": {"format": "json", "overwrite": True}
        } 
    }

    

    def start_requests(self):
        urls = ["https://www.udemy.com/courses/search/?src=ukw&q=machine+learning"]
        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)


    def parse(self, response):
        courses = response.css("div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze")
        for course in courses:
            relative_url = course.css("h3 a ::attr(href)").get()
            course_url = "https://udemy.com" + relative_url
            yield scrapy.Request(course_url, callback=self.parse_course_page)


        next_page = response.css("div.pagination-module--container--1Dmb0 a:last-child::attr(href)").get()
        if next_page is not None:
            next_page_url = "https://udemy.com" + next_page
            yield scrapy.Request(next_page_url, callback=self.parse)




    def parse_course_page(self, response):
        pass






