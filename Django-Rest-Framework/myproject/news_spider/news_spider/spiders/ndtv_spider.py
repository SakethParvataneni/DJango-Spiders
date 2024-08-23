import scrapy
from scrapy.http import HtmlResponse

class NdTvSpider(scrapy.Spider):
    name = 'ndtv'
    start_urls = ['https://www.ndtv.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={'selenium': True}, callback=self.parse)

    def parse(self, response):
        # Extract page title
        titles = response.xpath('//title/text()').getall()
        self.logger.info(f'Titles: {titles}')

        # Extract headlines
        headlines = response.xpath('//h2[contains(@class, "newsHdng")]/a/text()').getall()
        self.logger.info(f'Headlines: {headlines}')

        # Extract article URLs
        urls = response.xpath('//h2[contains(@class, "newsHdng")]/a/@href').getall()
        self.logger.info(f'Article URLs: {urls}')

        # Extract article summaries or descriptions
        summaries = response.xpath('//p[contains(@class, "newsCont")]/text()').getall()
        self.logger.info(f'Summaries: {summaries}')

        # Example of structuring extracted data
        for headline, url, summary in zip(headlines, urls, summaries):
            yield {
                'headline': headline.strip(),
                'url': url,
                'summary': summary.strip()
            }
