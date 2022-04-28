from urllib.request import Request
import scrapy
import json
import csv

class TrainSpider(scrapy.Spider):
    name = "calendar_spider"
    
    def start_requests(self):
        start_urls = [
        'https://www.imdb.com/calendar/?ref_=nv_mv_cal',
    ]
          
        for url in start_urls:
            yield scrapy.Request(url,callback=self.parse)
            
    def parse(self, response):
        movies_names=response.xpath('//*[@id="main"]/ul/li/a/text()').extract()
        
        with open('movies_names.csv','w') as f:
            for movie in movies_names:
                f.write(movie)
                f.write("\n")
                
        with open('movies_names.json','w') as file:
            json.dump(movies_names,file,indent=4)    
                    
        # import pdb;pdb.set_trace()
            
