# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import threading
import Queue
import time

class CocCrawlerPipeline(object):

    def open_spider(self, spider):
        spidername = str(spider).split("'")[1]
        self.file = open( '../output/'+spidername+'_'+str(time.time()) +'.csv', 'wb')
        self.run = True
        self.q = Queue.Queue()
        self.t = threading.Thread(target=self.f)
        self.t.daemon = True
        self.t.start()
     
    def f(self):
        w = None

        while True:
            try:
                i = self.q.get()
                w = csv.DictWriter(self.file,i.keys())
                w.writeheader()
                w.writerow(i)
                break
            except:
                pass

        while self.run:
            try:
                i = self.q.get()
                w.writerow(i)
            except:
                pass

    def close_spider(self, spider):
        print "closing pipeline",self.q.empty()
        while not self.q.empty():
            print "q still not empty"
            time.sleep(5)
            pass
        self.run=False
        self.file.close()

    def process_item(self, item, spider):
        self.q.put(dict(item))
