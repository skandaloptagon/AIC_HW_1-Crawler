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

class CigarUserReviewItem(scrapy.Item):
    title = scrapy.Field()
    review_no = scrapy.Field()
    user_rating = scrapy.Field()
    review_text = scrapy.Field()
    review_date = scrapy.Field()
    reviewer_name = scrapy.Field()
    pass

class CUserReviewSpider(scrapy.Spider):
    name = "cur"
    allowed_domains = ["www.cigars-review.org"]
    start_urls = ['http://www.cigars-review.org/']

    def __init__(self, *args, **kwargs):
        super(CUserReviewSpider, self).__init__(*args, **kwargs)
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
            #print cigar_link
            yield scrapy.Request(cigar_link,callback=self.parse_cigar_item)
            i+=1

    def parse_cigar_item(self, response):                

        pages = response.selector.xpath('//a[contains(@class, "paginas")]')
        for page in pages:
            pagina_link = self.start_url + str(page.xpath('@href').extract()[0])
            pagina_link = pagina_link.replace('.org','.org/')
            yield scrapy.Request(pagina_link, callback=self.parse_cigar_item)

        junk = response.selector.xpath('//form[contains(@method, "post")]')
        for i in junk.extract()[0].split('Review #')[1:]:
        
            item = CigarUserReviewItem()

            item["title"] = response.selector.xpath('//h1[contains(@align,"right")]/text()').extract()[0].strip()

            try:
                item["user_rating"] = i.count("images/full.gif")+.5*i.count("images/medium.gif")
            except Exception as e:
                print e

            item["review_no"] = i.split()[0]

            item["review_text"] = i.split('Submitted by <')[0].split('">')[-1].strip("- <i></i>")
            try:
                item["review_text"] = item["review_text"].split('>')[-1]
            except:
                pass

            item["review_date"] = i.split('> on ')[-1].split('<')[0]
            
            item["reviewer_name"] = i.split('<a href="/users/')[-1].split('.')[0]
            #print dict(item),'\n'

            yield item

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(CUserReviewSpider)
    process.start() # the script will block here until the crawling is finished
