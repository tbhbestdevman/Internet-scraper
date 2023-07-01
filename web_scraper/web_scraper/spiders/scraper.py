```python
import scrapy
from scrapy.http import Request
from web_scraper.web_scraper.items import WebScraperItem

class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        items = WebScraperItem()

        # Extract specific data from the page
        # Replace 'data' with the actual data you want to scrape
        items['data'] = response.css('data::text').extract()

        yield items

        # Handle pagination
        next_page = response.css('next::attr(href)').extract_first()
        if next_page is not None:
            yield Request(response.urljoin(next_page), callback=self.parse)
```
