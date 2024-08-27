from scrapy import Spider
from scrapy.selector import Selector
from selenium import webdriver

class NdtvSpider(Spider):
    name = "ndtv"
    
    def start_requests(self):
        url = "https://www.ndtv.com/"
        driver = webdriver.Chrome()  # or any other driver you are using
        driver.get(url)
        self.logger.info("Page loaded")
        
        response = Selector(text=driver.page_source)
        driver.quit()
        
        yield self.parse(response)

    def parse(self, response):
        # Update the XPath based on the correct class names
        headlines = response.xpath('//h2[contains(@class, "headline-class")]/text()').getall()
        # Add logic for scraping article URLs, summaries, etc.
        for headline in headlines:
            yield {
                'headline': headline.strip(),
            }
