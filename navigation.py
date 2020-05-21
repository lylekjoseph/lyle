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


if os.path.exists(file):
    os.remove(file)



class LekkeslaapSpiderSpider(scrapy.Spider):

    name = 'lekkeslaap_spider'
    allowed_domains = ['lekkeslaap.co.za']
    start_urls = ['http://www.lekkeslaap.co.za/akkommodasie-in/kaapstad-middestad/']

    def __init__(self, subject=None):
        self.subject = subject


    def parse(self, response):
        fjson = {}
        if self.subject:
            subject_url = response.xpath("//a[@class= 'name text']/@href").extract_first()
            absolute_subject_url = response.urljoin(subject_url)
            yield scrapy.Request(absolute_subject_url, callback=self.parse)

        else:
            self.log('Scraping all subjects.')
            subjects =  response.xpath("//a[@class='name text']/@href").extract()
            fjson["rating"] = response.css(".font-weight-bold.mr-1::text").extract()
            fjson["title.pg2"] = response.css("#estabTabScroll span::text").extract()
            fjson["address"] = response.css("u::text").extract()
            for subject in subjects:
                absolute_subject_url = response.urljoin(subject)
                yield scrapy.Request(absolute_subject_url, callback=self.parse)



            #print(fjson["rating"])

            #fjson["number_of_people"] = response.xpath(".big-photo:nth-child("+str(t)+") .meta::text").extract()
        #print(page1)
        #nr_reviews = response.xpath("//div[@class='reviews']/a[@class = 'text']/text()").extract()
        #avg_rating = response.xpath("//div[@class='reviews']/ul").extract()
        #fjson["rating"] = response.css(".big-photo:nth-child("+str(t)+") .full").extract()
        #print(title)

                with open('C:/Users/User/Desktop/lekkeslaap/lekkeslaap/spiders/20.05.2020test3.csv', "a") as fo:
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
    'ROBOTSTXT_OBEY' : 'False'
})
process.crawl(LekkeslaapSpiderSpider)
process.start()

loc = 'C:\\Users\\User\\Documents\\'+ file
#data_to_upload = pd.read_csv(loc)
