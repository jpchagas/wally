import scrapy


class PrivateSpider(scrapy.Spider):
    name = "private"
    allowed_domains = ["privateimoveis.com"]
    start_urls = ["https://privateimoveis.com/home/cidade/porto-alegre"]

    def parse(self, response):
        pass
