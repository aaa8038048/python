# -*- coding: utf-8 -*-
import scrapy
from tutorial2.items import Tutorial2Item
class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example"]
    start_urls = (
        'http://www.smzdm.com/',
    )

    def parse(self, response):
		for divs in response.xpath('//a[@class="picLeft"]'):
			img_url=divs.xpath('.//img/@src').extract()[0]
			urlItem=Tutorial2Item()
			urlItem['url']=img_url
			
			yield urlItem
        