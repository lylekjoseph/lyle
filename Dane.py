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









class Danish(scrapy.Spider):

    name = 'Dane'
    allowed_domains = ['rejsegarantifonden.dk']
    start_urls =['https://www.rejsegarantifonden.dk/no_cache/find-din-rejseudbyder/?showall=1']





    def parse(self, response):



        fjson = {}
        fjson["Firmanavn"] =  response.xpath("//div/hr/dl[@class='rgf-regrejse-results']/text()").extract()




        with open('C:/Users/User/Desktop/Dane.csv', "a") as fo:
            fo.write("\n"+str(fjson))
            fo.flush()





process = CrawlerProcess({
    'FEED_FORMAT': "csv",
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

process.crawl(Danish)
process.start()


#data_to_upload = pd.read_csv(loc)
