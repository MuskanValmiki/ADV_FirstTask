from urllib.request import Request
import scrapy
import json

class TrainSpider(scrapy.Spider):
    name = "calendar_spider"
    
    def start_requests(self):
        start_urls = [
        'https://www.imdb.com/calendar/?ref_=nv_mv_cal',
    ]
        
        for url in start_urls:
            yield scrapy.Request(url,callback=self.parse)
            
    def parse(self, response):

        Name=response.css('a::text').extract()
        yield{'litext':Name}
        
        with open('data.json', 'w') as f:
            json.dump(Name, f, indent=4)  

        # import pdb;pdb.set_trace()
            
  