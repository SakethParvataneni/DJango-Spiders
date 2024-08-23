import scrapy

class EenaduSpider(scrapy.Spider):
    name = "eenadu"

    start_urls = [
        'https://www.eenadu.net/',
    ]

    def parse(self, response):
        # Add your parsing logic here
        for article in response.css('selector-for-articles'):
            yield {
                'title': article.css('selector-for-title::text').get(),
                'link': article.css('selector-for-link::attr(href)').get(),
                # Add more fields as needed
            }
