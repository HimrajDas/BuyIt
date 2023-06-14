import scrapy
from urllib.parse import urlencode
from ..items import CoursescraperItem
import logging

SCRAPEOPS_API_KEY = "0f1478a6-e418-4393-b9a9-dc3edf2c9689"

logging.basicConfig(
    filename="scrapy.log",
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)

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
        courses = response.css(".course-card--main-content--2XqiY.course-card--has-price-text--1c0ze")
        for course in courses:
            relative_url = course.css("h3 a ::attr(href)").get()
            course_url = "https://udemy.com" + relative_url
            yield scrapy.Request(get_scrapeops_url(course_url), callback=self.parse_course_page)


        next_page = response.css(".pagination-module--container--1Dmb0 a:last-child::attr(href)").get()
        if next_page is not None:
            next_page_url = "https://udemy.com" + next_page
            yield scrapy.Request(get_scrapeops_url(next_page_url), callback=self.parse)




    def parse_course_page(self, response):
        course_details = CoursescraperItem()

        course_details["course_name"] = response.css(".clp-lead__title--small::text").get()
        course_details["rating"] = response.css(".star-rating-module--rating-number--2xeHu::text").get()
        course_details["no_of_ratings"] = response.css(".star-rating-module--dark-background--3p2UF+ span::text").get()
        course_details["students_enrolled"] = response.css(".enrollment::text").get()
        course_details["reviews"] = response.css("div.ud-text-md.show-more-module--content--cjTh0 p::text").getall()
        course_details["percentage_of_one_star"] = response.css('//*[@id="udemy"]/div[12]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/button[5]/span[3]/span::text').get()
        course_details["percentage_of_two_star"] = response.css('//*[@id="udemy"]/div[12]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/button[4]/span[3]/span::text').get()
        course_details["percentage_of_three_star"] = response.css('//*[@id="udemy"]/div[12]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/button[3]/span[3]/span::text').get()
        course_details["percentage_of_four_star"] = response.css('//*[@id="udemy"]/div[12]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/button[2]/span[3]/span::text').get()
        course_details["percentage_of_five_star"] = response.css('//*[@id="udemy"]/div[12]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/button[1]/span[3]/span::text').get()

        yield course_details


        logging.info(f"Details: {course_details['course_name']}")
        


        



