# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursescraperItem(scrapy.Item):
    # define the fields for your item here like:
    course_name = scrapy.Field()
    rating = scrapy.Field()
    no_of_ratings = scrapy.Field()
    students_enrolled = scrapy.Field()
    prerequisites = scrapy.Field()
    reviews = scrapy.Field()
    percentage_of_one_star = scrapy.Field()
    percentage_of_two_star = scrapy.Field()
    percentage_of_three_star = scrapy.Field()
    percentage_of_four_star = scrapy.Field()
    percentage_of_five_star = scrapy.Field()

    pass
