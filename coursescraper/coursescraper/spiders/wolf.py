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

    def start_requests(self):
        urls = ["https://www.udemy.com/courses/search/?src=ukw&q=machine+learning"]
        for url in urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)


    def parse(self, response):
        course_title = response.css(".course-card--course-title--vVEjC a::text").getall()
        for title in course_title:
            yield {
                "course_title": title
            }


