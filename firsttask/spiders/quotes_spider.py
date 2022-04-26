from email.quoprimime import quote
import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.mapsofindia.com/railway-timetable/',
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quotes = response.xpath('/html/body/section[1]/div/div[2]/div[3]/div[2]/p').extract_first()
        json_object = json.dumps(quotes, indent = 4)
        with open("quotes.json", "w") as outfile:
                outfile.write(json_object)
           