import scrapy


class PricespiderSpider(scrapy.Spider):
    name = "pricespider"
    allowed_domains = ["cargillsonline.com"]
    start_urls = ["https://cargillsonline.com"]

    def parse(self, response):
        pass
