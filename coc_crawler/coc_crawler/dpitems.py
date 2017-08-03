# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BeijingReviewItem(scrapy.Item):
    current_url = scrapy.Field()
    title = scrapy.Field()
    origin = scrapy.Field()
    manufactured = scrapy.Field()
    gauge = scrapy.Field()
    length = scrapy.Field()
    cigar_format = scrapy.Field()
    ring = scrapy.Field()
    weight = scrapy.Field()
    score = scrapy.Field()
    presentation = scrapy.Field()
    average_user_rating = scrapy.Field()
    pass

class BeijingUserReviewItem(scrapy.Item):
    title = scrapy.Field()
    review_no = scrapy.Field()
    user_rating = scrapy.Field()
    review_text = scrapy.Field()
    review_date = scrapy.Field()
    reviewer_name = scrapy.Field()
    pass

class CigarAffItem(scrapy.Item):
    session_id = scrapy.Field()
    pass
