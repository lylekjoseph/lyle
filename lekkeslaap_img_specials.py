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
from scrapy_splash import SplashRequest
from time import sleep
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


if os.path.exists(file):
    os.remove(file)



class LekkeslaapSpiderSpider(scrapy.Spider):

    name = 'lekkeslaap_spider'
    allowed_domains = ['lekkeslaap.co.za']
    start_urls =['https://www.lekkeslaap.co.za/akkommodasie-in/suid-afrika?q=suid-afrika&start=&end=&pax=2#&0&&&1&&&2&&1&0&5000&0&0&&&0/']


    def parse(self, response):
        listings = response.css(".number_results_heading").extract()
        listings_num = re.search('[0-9]+', str(listings)).group()

        pages = math.ceil(int(listings_num)/10)
        print(pages)
        pages = pages + 10
        print(pages)
        print("check page test")
        for i in range(1,pages):
            print(i)
            next_page = 'https://www.lekkeslaap.co.za/akkommodasie-in/suid-afrika?q=suid-afrika&start=&end=&pax=2#&0&&&'+str(i)+'&&&2&&1&0&5000&0&0&&&0/'
            yield scrapy.Request(next_page, callback=self.parse_listing)

            def _init_(self, subject=None):
                self.subject = subject
                if self.subject:
                    subject_url = response.xpath('//a[@class="'+ self.subject + '"]/@href').extract_first()
                    absolute_subject_url = response.urljoin(subject_url)
                    yield Request(absolute_subject_url, callback=self.parse_subject)
                else:
                    self.log('Scraping all subjects.')
                    subjects =  response.xpath("//a[@class='name text']/@href").extract()
                    for subject in subjects:
                        absolute_subject_url = response.urljoin(subject)
                        yield Request(absolute_subject_url, callback=self.parse_subject)
                        fjson["rating"] = response.css(".font-weight-bold.mr-1::text").extract()
                        fjson["title.pg2"] = response.css("#estabTabScroll span::text").extract()
                        fjson["address"] = response.css("u::text").extract()


    def parse_listing(self, response):



        fjson = {}

        #fjson["title"] = response.css(".name::text").extract() worksfine scrapes all names per page
        for t in range(1,11):

            fjson["relative_img_link"]= response.xpath("//img/@data-src").extract()[t-1]

            fjson["special"] = response.css(".big-photo:nth-child("+str(t)+") .special::text").extract()
            fjson["title"] = response.css(".big-photo:nth-child("+str(t)+") .name::text").extract()
            fjson["listing_type"] =  response.css(".big-photo:nth-child("+str(t)+") .type::text").extract()
            #fjson["province"] = response.css(".region a::text").extract()
            fjson["flexible_cancellation"] = response.css(".big-photo:nth-child("+str(t)+") .cancellation::text").extract()
            fjson["region"] = response.css(".big-photo:nth-child("+str(t)+") .region::text").extract()
            fjson["starting_price"] = response.css(".big-photo:nth-child("+str(t)+") .price::text").extract()
            fjson["pre_discount_price"] = response.css(".big-photo:nth-child("+str(t)+") .org-price::text").extract()
            fjson["top_features"] = response.css(".big-photo:nth-child("+str(t)+") .table-chars td::text").extract()
            fjson["is_instant_booking"] =  response.css(".big-photo:nth-child("+str(t)+") .instant-booking::text").extract()
            #page = response.xpath("//div[@class = 'page_number_selected']/text()").extract()
            fjson["page1"] = response.xpath("//div[@class = 'number_results']/table/tr/td/text()").extract()



            #print(fjson["rating"])

            #fjson["number_of_people"] = response.xpath(".big-photo:nth-child("+str(t)+") .meta::text").extract()
        #print(page1)
        #nr_reviews = response.xpath("//div[@class='reviews']/a[@class = 'text']/text()").extract()
        #avg_rating = response.xpath("//div[@class='reviews']/ul").extract()
        #fjson["rating"] = response.css(".big-photo:nth-child("+str(t)+") .full").extract()
        #print(title)

            with open('C:/Users/User/Desktop/lekkeslaap/lekkeslaap/spiders/lhd_link_filter_test.csv', "a") as fo:
                fo.write("\n"+str(fjson))
                fo.flush()





process = CrawlerProcess({
    'FEED_FORMAT': "csv",
    'FEED_URI': file,
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'DOWNLOAD_DELAY' : "0.1",
    'COOKIES_ENABLED' : 'True',
    'COOKIES_DEBUG' : 'True',
    'CONCURRENT_REQUESTS' : '8',
    'ROBOTSTXT_OBEY' : 'False',
    'SPLASH_URL' : 'http://0.0.0.0:8050/',
    'DUPEFILTER_CLASS' : 'scrapy_splash.SplashAwareDupeFilter',
    'HTTPCACHE_STORAGE' : 'scrapy_splash.SplashAwareFSCacheStorage'





})
middleware = DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

process.crawl(LekkeslaapSpiderSpider)
process.start()

loc = 'C:\\Users\\User\\Documents\\'+ file
#data_to_upload = pd.read_csv(loc)
