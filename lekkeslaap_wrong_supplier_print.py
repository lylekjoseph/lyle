

# -*- coding: utf-8 -*-
import scrapy
#import numpy as np
#import pandas as pd
#import json
import os
import re

import time
import sys
import math

import logging
from scrapy.utils.log import configure_logging


#from scrapy.contrib.pipeline.images import ImagesPipeline
#from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
#from scrapy.http import FormRequest
#from scrapy.selector import HtmlXPathSelector


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


import warnings
warnings.filterwarnings('ignore')


file = 'lekkeslaap_all_default_'+time.strftime('%Y%m%d') +'.csv'
fjson = {}


if os.path.exists(file):
    os.remove(file)



class LekkeslaapSpiderSpider(scrapy.Spider):

    name = 'lekkeslaap_spider'
    allowed_domains = ['lekkeslaap.co.za']
    start_urls = ['http://www.lekkeslaap.co.za/akkommodasie-in/kaapstad-middestad']

    def parse(self, response):
        listings = response.css(".number_results_heading").extract()
        listings_num = re.search('[0-9]+', str(listings)).group()

        pages = math.ceil(int(listings_num)/10)
        print(pages)
        pages = pages + 10
        print(pages)
        print("check page test")
        for i in range(1,pages):
            #print(i)
            next_page = 'http://www.lekkeslaap.co.za/akkommodasie-in/kaapstad-middestad/'+str(i)
            yield scrapy.Request(next_page, callback=self.parse_listing)

    def parse_listing(self, response):

        for t in range(1,11):

            fjson["title"] = response.css(".big-photo:nth-child("+str(t)+") .name::text").extract()
            fjson["listing_type"] =  response.css(".big-photo:nth-child("+str(t)+") .type::text").extract()
            #fjson["province"] = response.css(".region a::text").extract()
            fjson["region"] = response.css(".big-photo:nth-child("+str(t)+") .region::text").extract()
            #fjson["region"] = response.css("..region a::text").extract()
            fjson["starting_price"] = response.css(".big-photo:nth-child("+str(t)+") .price::text").extract()
            fjson["pre_discount_price"] = response.css(".big-photo:nth-child("+str(t)+") .org-price::text").extract()
            fjson["is_instant_booking"] =  response.css(".big-photo:nth-child("+str(t)+") .instant-booking::text").extract()
            #page = response.xpath("//div[@class = 'page_number_selected']/text()").extract()
            fjson["page"] = response.xpath("//div[@class = 'number_results']/table/tr/td/text()").extract()
            fjson["top_features"] = response.css(".big-photo:nth-child("+str(t)+") .table-chars td::text").extract()

            supplierPage = str(response.xpath("//a[@class='name text']/@href")[t-1].extract())
            print(t)
            yield response.follow(supplierPage, callback=self.parse_book)
            with open('C:/Users/User/Desktop/lekkeslaap/lekkeslaap/spiders/24.05.20_test9.csv', "a") as fo:
                fo.write("\n"+str(fjson))
                fo.flush()
            #print(t)

    def parse_book(self,response):

        fjson["Title_test_ratings_page"] = response.css("#estabTabScroll span::text").extract()
        fjson["ratings"] = response.css(".font-weight-bold.mr-1::text").extract()
        #fjson["listing_type"] =  response.css("#js-title-box .mb-3 div::text").extract()
        #fjson["region"] = response.css("u::text").extract()
        #fjson["starting_price"] = response.css("#js-navpricebox-fixed .font-weight-bold::text").extract()
        #fjson["pre_discount_price"] = response.css("s::text").extract()

        #print(fjson)


process = CrawlerProcess({
    'FEED_FORMAT': "csv",
    'FEED_URI': file,
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'DOWNLOAD_DELAY' : "0.1",
    'COOKIES_ENABLED' : 'True',
    'COOKIES_DEBUG' : 'True',
    'CONCURRENT_REQUESTS' : '8',
    'ROBOTSTXT_OBEY' : 'False'
})
process.crawl(LekkeslaapSpiderSpider)
process.start()

loc = 'C:\\Users\\User\\Documents\\'+ file
#data_to_upload = pd.read_csv(loc)
