# AIC_HW_1-Crawler
Feel free to use any open source crawler as the code base. Write your focused crawler, such as crawling only CoC website or crawling only healthcare web pages. You are expected to crawl at least 1000 pages.

## setup

just `virtualenv venv` then `source venv/bin/activate` then `pip install -r requirements.txt`

## How to run

Just `cd coc_crawler` then `Scrapy crawl coc`

## Viewing results

in `coc_crawler` a file called `items.jl` will be created which contains all the page links and the reference link.
Stats will appear in the terminal before, during, and after execution.
