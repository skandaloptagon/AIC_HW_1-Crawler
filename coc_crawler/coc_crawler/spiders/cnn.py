# -*- coding: utf-8 -*-
# Author: Ivan Duralde
# Base Code from John Skandalakis
# Reference: http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/
#            http://bgrva.github.io/blog/2014/03/04/scrapy-after-tutorials-part-1/

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from coc_crawler.items import NewsItem
from coc_crawler.static.sentiment import *
from scrapy.exceptions import *
from bs4 import BeautifulSoup
import time
import Queue

class CocSpider(CrawlSpider):
    name = "cnn"
    allowed_domains = ["cnn.com"]
    start_urls = ['http://www.cnn.com/']

    rules = (
        Rule(LinkExtractor(allow=('', )), callback='parse_item', follow = True),
    )

    def __init__(self, *args, **kwargs):
        super(CocSpider, self).__init__(*args, **kwargs)

    # Parses the brand list
    def parse_item(self, response):
        article_text = ' '.join(response.selector.xpath('//div[@class="zn-body__paragraph"]/text()').extract())
        if len(article_text) == 0:
            return
        sentiment = generate_sentiment(article_text)        

        article_title = str(response.selector.xpath('//title/text()').extract()[0])
        meta = dict()
        for m in response.selector.xpath('//meta'):
            try:
                meta[str(m.xpath('@name').extract()[0])]=str(m.xpath('@content').extract()[0])
            except:
                pass

        item = NewsItem()
        try:
            item['article_date'] = meta['pubdate']
        except KeyError:
            print "Key Error 'og:pubdate'"
            return
        item['article_title'] = article_title
        item['sentiment_score'] = sentiment

        print dict(item)
        pass
