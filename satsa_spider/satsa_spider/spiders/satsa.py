# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import validators

base_path = "enter path to url_csv.csv"


def get_urls():
    path = base_path + 'url_csv.csv'
    fl = []
    with open(path, 'r') as fo:
        for l in fo.readlines():
            llist = l.split(',')
            url = llist[1]
            valid = validators.url(url)
            if not valid:
                continue
            fl.append(url + "/#tabs-4")

    return fl


class SatsaSpider(scrapy.Spider):
    name = 'satsa'
    allowed_domains = ['www.satsa.com']
    start_urls = get_urls()

    def parse(self, response):
        fjson = {}
        fjson["address"] = response.css(".item-address > .address + dd::text").get()
        fjson["gps"] = response.css(".item-address > .gps + dd::text").get()
        fjson["tel"] = response.css(".item-address > .phone + dd::text").get()
        fjson["email"] = response.css(".item-address > .email + dd > a::text").get()
        fjson["web"] = response.css(".item-address > .web + dd > a::text").get()

        for i in range(len(response.css(".item-address > .fax"))):
            text = response.css(".item-address > .fax::text")[i].get()
            if text == "Skype":
                fjson["skype"] = response.css(".item-address > .fax + dd::text")[i].get()
                pass
            elif text == "Fax":
                fjson["fax"] = response.css(".item-address > .fax + dd::text")[i].get()
                pass
            elif text == "Contact:":
                fjson["contact_user"] = response.css(".item-address > .fax + dd::text")[i].get()

        with open(base_path + 'data.txt', "a") as fo:
            fo.write("\n"+str(fjson))
            fo.flush()


process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'})
process.crawl(SatsaSpider)
process.start()  # the script will block here until the crawling is finished
