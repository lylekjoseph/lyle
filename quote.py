# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['flightcentre.co.za']
    start_urls = ['http://www.flightcentre.co.za/holidays/search?destination_in=South+Africa']

    def start_requests(self):
        for url in self.start_urls :
            yield SplashRequest(url= url,
                                callback=self.parse,
                                args={'wait': 0.5},
                                endpoint = 'render.html')
    def parse(self, response):
        print('listing')
        title = response.xpath("//div[@data-testid='Product.Name']")
        print(title)

        title2 = response.css(".ProductSearch-HolidaySearch-MuiTypography-root ProductSearch-HolidaySearch-fctg-product-search489 ProductSearch-HolidaySearch-MuiTypography-h3 selectorgadget_selected").extract()
        print(title2)

        logo = response.css(".logo::text").extract()
        print(logo)

        test = response.css(".header-phone::text").extract()
        print(test)

        price_currency = response.xpath("//span[@class = 'dollar-sign']/text()").extract()
        price = response.xpath("//span[@class = 'value']/text()").extract()
        price = ([x for x in price if "\n" not in x ])
        print(price)
        location = response.xpath("//div[@class = 'product-sub-heading']/span/text()").extract()
        print(location)
        travel_dates = response.xpath("//div[@class = 'product-travel-dates']/text()").extract()
        print(travel_dates)
        expiry_dates = response.xpath("//span[@class = 'expiry-date']/text()").extract()
        print(expiry_dates)
        stay_nights = response.xpath("//span[@class = 'from-prefix']/text()").extract()
        print(stay_nights)
        departure_airport = response.xpath("//span[@class = 'field-content']/a/@data-departure").extract()
        print(departure_airport)
        site_link = response.xpath("//span[@class = 'field-content']/a/@href").extract()
        string = 'http://www.flightcentre.co.za'
        site_link = [string + x for x in site_link]
        print(site_link)
        img_link = response.xpath("//div[@class='field-items']/div/img/@src").extract()
        print(img_link)

        print(title)

        for item in zip(title,price_currency, price,location,travel_dates,expiry_dates,stay_nights,departure_airport,site_link,img_link):
            data = {
                'title' :item[0],
                'currency' : item[1],
                'price' : item[2],
                'location' : item[3],
                'travel_dates' : item[4],
                'expiry_dates' : item[5],
                'stay_nights' : item[6],
                'departure_airport' : item[7],
                'site_link' : item[8],
                'img_link' : item[9],
                'title2' : item[10],
                'logo' : item[11],
                'test' : item[11],
                'scrape_date' : time.strftime('%Y%m%d'),
                'scrape_source' : 'flightcentre'
            }
        #    print(data)
            yield data

'''
        print('pages')
        listing_page = 'https://www.flightcentre.co.za/'
        #next_page = response.xpath().extract
        index = len(response.xpath("//li[@class= 'pager-next']/a/@href").extract())-1
        refs = response.xpath("//li[@class= 'pager-next']/a/@href").extract()
        href  = refs[index]
        print(href)
        Next =  response.xpath("//li[@class= 'pager-next']/a/@href").extract()

        if len(Next) > 0:
        #if 'Next' in response.xpath("//div[@class= 'paging']/a//text()").extract():
            next_page = listing_page + href
            print(next_page)
            yield scrapy.Request(next_page, callback = self.parse)

'''

'''
process = CrawlerProcess({
    'FEED_FORMAT': "csv",
    'FEED_URI': file,
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'DOWNLOAD_DELAY' : "2",
    'COOKIES_ENABLED' : 'True',
    'COOKIES_DEBUG' : 'True',
    'CONCURRENT_REQUESTS' : '8',
    'ROBOTSTXT_OBEY' : 'False'
    #'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    #'AWS_ACCESS_KEY_ID' : 'AKIAJ53R23MMJ6LO3GYQ',
    #'AWS_SECRET_ACCESS_KEY' : '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',
    #'IMAGES_STORE' : 's3://dealers-online.images/'
})




process.crawl(flightcentreSpider)
process.start()


#data_to_upload= pd.read_csv(file)
'''
