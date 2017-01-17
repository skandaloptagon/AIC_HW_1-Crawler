# AIC_HW_1-Crawler
Feel free to use any open source crawler as the code base. Write your focused crawler, such as crawling only CoC website or crawling only healthcare web pages. You are expected to crawl at least 1000 pages.

## setup

just `virtualenv venv` then `source venv/bin/activate` then `pip install -r requirements.txt`

## How to run

Just `cd coc_crawler` then `Scrapy crawl coc`

## Results

### Viewing results

in `coc_crawler` a file called `items.jl` will be created which contains all the page links and the reference link.
Stats will appear in the terminal before, during, and after execution.

### My results

Speed Stats:

        2017-01-17 15:35:34 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
        2017-01-17 15:36:34 [scrapy.extensions.logstats] INFO: Crawled 256 pages (at 256 pages/min), scraped 250 items (at 250 items/min)
        2017-01-17 15:37:34 [scrapy.extensions.logstats] INFO: Crawled 482 pages (at 226 pages/min), scraped 469 items (at 219 items/min)
        2017-01-17 15:36:34 [scrapy.extensions.logstats] INFO: Crawled 256 pages (at 256 pages/min), scraped 250 items (at 250 items/min)
        INFO: Crawled 1127 pages (at 354 pages/min), scraped 1110 items (at 349 items/min)
        2017-01-17 15:40:34 [scrapy.extensions.logstats] INFO: Crawled 1518 pages (at 391 pages/min), scraped 1479 items (at 369 items/min)
        2017-01-17 15:41:34 [scrapy.extensions.logstats] INFO: Crawled 1736 pages (at 218 pages/min), scraped 1683 items (at 204 items/min)
        2017-01-17 15:42:34 [scrapy.extensions.logstats] INFO: Crawled 1957 pages (at 221 pages/min), scraped 1876 items (at 193 items/min)

Time Info:

        real    7m1.535s
        user    1m1.476s
        sys 0m6.383s

Scrapy Stats:

        2017-01-17 15:42:35 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
        {'downloader/exception_count': 2,
         'downloader/exception_type_count/scrapy.exceptions.IgnoreRequest': 2,
         'downloader/request_bytes': 793440,
         'downloader/request_count': 2056,
         'downloader/request_method_count/GET': 2056,
         'downloader/response_bytes': 538892083,
         'downloader/response_count': 2056,
         'downloader/response_status_count/200': 1899,
         'downloader/response_status_count/300': 5,
         'downloader/response_status_count/301': 77,
         'downloader/response_status_count/302': 6,
         'downloader/response_status_count/400': 1,
         'downloader/response_status_count/403': 6,
         'downloader/response_status_count/404': 62,
         'dupefilter/filtered': 38834,
         'finish_reason': 'finished',
         'finish_time': datetime.datetime(2017, 1, 17, 20, 42, 35, 690022),
         'item_scraped_count': 1883,
         'log_count/INFO': 80,
         'log_count/WARNING': 2,
         'offsite/domains': 715,
         'offsite/filtered': 23522,
         'request_depth_max': 4,
         'response_received_count': 1963,
         'scheduler/dequeued': 2040,
         'scheduler/dequeued/memory': 2040,
         'scheduler/enqueued': 2040,
         'scheduler/enqueued/memory': 2040,
         'start_time': datetime.datetime(2017, 1, 17, 20, 35, 34, 714515)}

Total Items Crawled from 4 layer deep:

        1883 items.jl

Example output:

        {
          "referring_url": "http://www.cc.gatech.edu/about/jobs",
          "session_id": -1,
          "current_url": "http://www.cc.gatech.edu/web-designer",
          "title": [
            "Web Designer  | College of Computing"
          ]
        }
        {
          "referring_url": "http://www.cc.gatech.edu/about/jobs",
          "session_id": -1,
          "current_url": "http://www.cc.gatech.edu/software-engineer-0",
          "title": [
            "Software Engineer | College of Computing"
          ]
        }
        {
          "referring_url": "http://www.cc.gatech.edu/academics/degree-programs/phd/computer-science/currentstudents",
          "session_id": -1,
          "current_url": "http://www.cc.gatech.edu/academics/degree-programs/phd/computer-science/currentstudents/intelligent-systems",
          "title": [
            "Ph.D. CS - Intelligent Systems Body of Knowledge | College of Computing"
          ]
        }
