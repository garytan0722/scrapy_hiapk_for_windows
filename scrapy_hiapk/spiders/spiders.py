# -*- coding: utf-8 -*-

import scrapy
from scrapy_hiapk.items import ScrapyHiapkItem
class apkspider(scrapy.Spider):
    name = "hiapk"
    download_delay=2
    allowed_domains = ["apk.hiapk.com"]
    start_urls = []
    for i in range(60,70):
        link="http://apk.hiapk.com/apps/Tools?sort=5&pi=%i" %i
        start_urls.append(link)
    print ("START_URL:")
    print(start_urls)
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

     
