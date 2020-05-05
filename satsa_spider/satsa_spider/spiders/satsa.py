# -*- coding: utf-8 -*-
import scrapy
import csv
import pandas as pd
#from selenium import webdriver

class SatsaSpider(scrapy.Spider):
    name = 'satsa'
    allowed_domains = ['www.satsa.com']
    start_urls = ['http://www.satsa.com/item/all-africa-tours/'] #scrape test

    #f = open('C:/Users/User/Desktop/satsa_spider/satsa_spider/spiders/url_csv.csv','r')
    #reader = csv.reader(f)
    #url_dict = {}
    #for row in reader:                          #get data from excel into dict
    #    url_dict[row[0]] = {'url_link':row[1]}

#    for value in url_dict.values():            # iterate through links to be scraped from
        #print(value)


    df = pd.read_csv('C:/Users/User/Desktop/satsa_spider/satsa_spider/spiders/url_csv.csv')            # read csv panda
    for url in df['url_name'].unique():
        next_page = url
    #    print(url)
    #    start_urls = "'"+url+"''"
    #def start_requests(self):                # Selenium test
    #    self.driver = webdriver.Chrome('/webdrivers/chromedriver')
    #    self.driver('')

        def parse(self, response): #scrapetest
    #   infoCategory =  response.xpath('//dt/text()').extract()
    #    infoCategory =  response.xpath('//*[@class=address]').extract()
    #   response.xpath('//a[@href ="https://www.satsa.com/cat/tour-operatordmc/"]/text()')
            data =  response.xpath('//dd/text()').extract()#scrapetest
    #   tourType = listings =  response.xpath('//a/text()').extract()
    #    for infoCategory in listings:
    #    print infoCategory
            for info in data :          #scrapetest
                yield{'Info': info}     #scrapetest
