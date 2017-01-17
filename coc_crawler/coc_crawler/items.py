# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CocCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    session_id = scrapy.Field()
    depth = scrapy.Field()
    current_url = scrapy.Field()
    referring_url = scrapy.Field()
    title = scrapy.Field()
    pass
