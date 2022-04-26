from http import cookiejar
from urllib.request import Request
import scrapy
import requests

class TrainSpider(scrapy.Spider):
    name = "calendar_spider"
    

    def start_requests(self):
        start_urls = [
        'https://www.imdb.com/calendar/?ref_=nv_mv_cal',
    ]
        
        for url in start_urls:
            yield scrapy.Request(url,callback=self.parse)
            
    def parse(self, response):
        f=open('calendar.html','w').write(response.text)
        # print(f)
        # import pdb;pdb.set_trace()
            
