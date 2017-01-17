# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from coc_crawler.items import CocCrawlerItem
from scrapy.exceptions import *
class CocSpider(CrawlSpider):
    name = "coc"
    allowed_domains = ["www.cc.gatech.edu"]
    start_urls = ['http://www.cc.gatech.edu/']

    rules = (
        Rule(LinkExtractor(allow=('', )), callback='parse_item', follow = True),
    )
    def __init__(self, session_id=-1, *args, **kwargs):
        super(CocSpider, self).__init__(*args, **kwargs)
        self.session_id = session_id

    def parse_item(self, response):
        item = CocCrawlerItem()
        item["session_id"] = self.session_id
        item["current_url"] = response.url
        referring_url = response.request.headers.get('Referer', None)
        item["referring_url"] = referring_url
        try:
            item["title"] = response.xpath('//title/text()').extract()
        except NotSupported:
            item["title"] = None
        return item
