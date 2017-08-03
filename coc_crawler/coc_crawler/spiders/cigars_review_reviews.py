# -*- coding: utf-8 -*-
# Author: Ivan Duralde
# Base Code from John Skandalakis
# Reference: http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/
#            http://bgrva.github.io/blog/2014/03/04/scrapy-after-tutorials-part-1/

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import *
from bs4 import BeautifulSoup
import time
import Queue
from scrapy.crawler import CrawlerProcess


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

class CRRSpider(scrapy.Spider):
    name = "crr"
    allowed_domains = ["www.cigars-review.org"]
    start_urls = ['http://www.cigars-review.org/']

    def __init__(self, *args, **kwargs):
        super(CRRSpider, self).__init__(*args, **kwargs)
        self.start_url= 'http://www.cigars-review.org'

    # Parses the brand list
    def parse(self, response):
        table = response.selector.xpath('//a[contains(@class, "brands")]')[:-1]
        for atag in table:
            brand_link = self.start_url + str(atag.xpath('@href').extract()[0])
            yield scrapy.Request(brand_link,callback=self.parse_brand_item)

    def parse_brand_item(self, response):
        table = response.selector.xpath('//a[@class="info"]')
        i = 0
        for atag in table:
            cigar_link = self.start_url + str(atag.xpath('@href').extract()[0])
            yield scrapy.Request(cigar_link,callback=self.parse_cigar_item)
            i+=1

    def parse_cigar_item(self, response):        
        table = response.selector.xpath('//table[contains(@width, "95%")]')
        obj = table.xpath('//font')
        bolds = obj.xpath('//b/text()').extract()[1:13]
        text = obj.xpath('text()').extract()[2:]
        tags = dict()

        #print response.url
        try:
            while bolds[0] != u'Origin:':
                bolds = bolds[1:]
        except IndexError:
            pass

        #print bolds, text
        if u'Average user rating ' in bolds:
            while bolds[-1] != u'Average user rating ':
                bolds = bolds[:-1]
            bolds = bolds[:-2]
        else:
            #print "WOOOOOOOOOOOOOOHOOOOOOOOOOOOOOO"
            pass

        try:
            text.remove(u'\xa0\xa0\xa0\xa0\n\n')
        except ValueError:
            pass
        #print len(text),response.url,text

        try:
            review = text[-1]
        except IndexError:
            pass
        text = text[:-1]

        #print bolds

        for bold in bolds:
            try:
                tags[bold] = text[0]
                text = text[1:]
            except:
                tags[bold] = ''

        #print tags

        item = CigarsReviewItem()
        item["current_url"] = response.url
        item["title"] = response.selector.xpath('//h1[contains(@align,"right")]/text()').extract()[0]
        try:
            item["origin"] = tags[u'Origin:']
        except:
            item["origin"] = ''
            pass
        try:
            item["manufactured"] = tags[u'Manufactured: ']
        except:
            item["manufactured"] = ''
            pass
        try:
            item["gauge"] = tags[u'Gauge:']
        except:
            item["gauge"] = ''
            pass
        try:
            item["length"] = tags[u'Length:']
        except:
            item["length"] = ''
            pass
        try:
            item["cigar_format"] = tags[u'Format:']
        except:
            item["cigar_format"] = ''
            pass
        try:
            item["ring"] = tags[u'Ring:']
        except:
            item["ring"] = ''
            pass
        try:
            item["weight"] = tags[u'Weight:']
        except:
            item["weight"] = ''
            pass
        try:
            item["score"] = tags[u'Score:']
        except:
            item["score"] = ''
            pass
        try:
            item["presentation"] = tags[u'Presentation: ']
        except:
            item["presentation"] = ''
            pass

        try:
            item["average_user_rating"] = len(table.xpath('//font/img[contains(@src,"images/full.gif")]'))+.5*len(table.xpath('//font/img[contains(@src,"images/medium.gif")]'))
        except:
            pass
        #print dict(item),'\n'
        return item

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(CRRSpider)
    process.start() # the script will block here until the crawling is finished
