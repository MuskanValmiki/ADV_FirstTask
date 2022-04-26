from urllib.request import Request
import scrapy
import requests

class TrainSpider(scrapy.Spider):
    name = "trains_spider"
    start_urls = (
        'https://www.mapsofindia.com/railway-timetable',
    )
    
    
    
    def parse(self, response):
        quotes = response.xpath('/html/body/section[2]/div/div table"]')
        for quote in quotes:
            yield {
                'train no':quote.xpath("//*[@id='head_table']/tr[2]/th[1]").extract(),
                'train name':quote.xpath(" //*[@id='head_table']/tr[2]/th[2]").extract(),
                'source stn':quote.xpath("//*[@id='head_table']/tr[2]/th[3]").extract(),
                'source dep time':quote.xpath(" //*[@id='head_table']/tr[2]/th[4]").extract(),
                'train distination stn':quote.xpath("//*[@id='head_table']/tr[2]/th[5]").extact(),
                'dest arr time':quote.xpath("//*[@id='head_table']/tr[2]/th[6]").extract(),
                'dep days/runs on':quote.xpath("//*[@id='head_table']/tr[2]/th[7]").extract()
            }
  
# /html/body/section[2]/div/div table
# //*[@id="head_table"]/tr[2]/th[1]   train no
# //*[@id="head_table"]/tr[2]/th[2] train name
# //*[@id="head_table"]/tr[2]/th[3] source stn
# //*[@id="head_table"]/tr[2]/th[4] source dep time
# //*[@id="head_table"]/tr[2]/th[5] train distination stn
# //*[@id="head_table"]/tr[2]/th[6] dest arr time
# //*[@id="head_table"]/tr[2]/th[7] dep days/runs on
