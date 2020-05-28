# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for url in self.start_urls :
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint = 'render.html')
    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            yield {'author': quote.xpath('.//*[@class="author"]/text()').extract_first(),
                    'quote': quote.xpath('.//*[@class="text"]/text()').extract_first()

            }
