import scrapy


class FirstscrapySpider(scrapy.Spider):
    name = 'FirstScrapy'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        print(response.body)
