# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CigarsReviewItem(scrapy.Item):
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

class CigarReviewItem2(scrapy.Item):
    average_user_rating = scrapy.Field()
    pass

class CigarAffItem(scrapy.Item):
    session_id = scrapy.Field()
    pass
