from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
]    
  
    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        a=response.xpath('//title').extract()
        print a
