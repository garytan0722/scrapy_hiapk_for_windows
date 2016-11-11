# -*- coding: utf-8 -*-

import scrapy
from scrapy_hiapk.items import ScrapyHiapkItem
class apkspider(scrapy.Spider):
    def __init__(self, category='',start=None, end=None, *args, **kwargs):
        super(apkspider, self).__init__(*args, **kwargs)
        #self.start_urls = ['http://www.example.com/categories/%s' % category]
        start_int=int(start)
        end_int=int(end)
        for i in range(start_int,end_int):
            #50
            self.link="http://apk.hiapk.com/apps/%s?sort=5&pi=%i" %(category,i)
            self.start_urls.append(self.link)
        print ("START_URL:")
        print(self.start_urls)
    name = "hiapk"
    download_delay=2
    allowed_domains = ["apk.hiapk.com"]
    def parse(self, response):
        res=response.xpath('//div[@class="button_bg button_1 right_mt"]/a/@href').extract()
        print (res)
        for link in range(len(res)):
            url="http://apk.hiapk.com"+res[link]
            print(url)
            yield scrapy.Request(url, callback=self.download)
    def download(self, response):
        link=response.url
        print("APK FILE DST:"+link)
        myitem = ScrapyHiapkItem()
        myitem["file_urls"]=[link]
        yield myitem

     
