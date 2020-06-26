import scrapy
from scrapy.crawler import CrawlerProcess
import validators

base_path = "C:/Users/User/Documents/Insigt/Resources/Python/LHDscrapers/thompson/"

class SatsaSpider(scrapy.Spider):
    name = 'satsa'
    allowed_domains = ['thompsons.co.za']
    start_urls = ['https://www.thompsons.co.za/deals/south-africa-deals']

    def parse(self, response):

        for t in range(1,120):
            fjson = {}
            fjson["title"] = response.css(".CampaignPackages-items:nth-child("+str(t)+")  .title a::text").extract()
            fjson["valid dates"] = response.css(".CampaignPackages-items:nth-child("+str(t)+")  .valid-dates p::text").extract()
            fjson["price"] = response.css(".CampaignPackages-items:nth-child("+str(t)+")  .price::text").extract()
            fjson["tags"] = response.css(".CampaignPackages-items:nth-child("+str(t)+")  .tag-names::text").extract()
            print(fjson)
            print("********************************************************************")
            print(t)


            with open(base_path + 'data.csv', "a") as fo:
                fo.write("\n"+str(fjson))
                fo.flush()


process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'})
process.crawl(SatsaSpider)
process.start()  # the script will block here until the crawling is finished
