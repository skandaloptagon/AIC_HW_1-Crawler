# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsItem(scrapy.Item):
    article_date = scrapy.Field()
    article_title = scrapy.Field()
    company = scrapy.Field()
    stock_value = scrapy.Field()
    sentiment_score = scrapy.Field()
