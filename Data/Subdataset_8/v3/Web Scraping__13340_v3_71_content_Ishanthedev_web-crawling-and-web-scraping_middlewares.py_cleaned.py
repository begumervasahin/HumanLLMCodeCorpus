import scrapy
from scrapy import signals
class QuoteTutorialSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        instance = cls()
        crawler.signals.connect(instance.on_spider_opened, signal=signals.spider_opened)
        return instance
    def process_spider_input(self, response, spider):
        return None
    def process_spider_output(self, response, result, spider):
        for item in result:
            yield item
    def process_spider_exception(self, response, exception, spider):
        pass
    def process_start_requests(self, start_requests, spider):
        for request in start_requests:
            yield request
    def on_spider_opened(self, spider):
        spider.logger.info(f'Spider opened: {spider.name}')
class QuoteTutorialDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        instance = cls()
        crawler.signals.connect(instance.on_spider_opened, signal=signals.spider_opened)
        return instance
    def process_request(self, request, spider):
        return None
    def process_response(self, request, response, spider):
        return response
    def process_exception(self, request, exception, spider):
        pass
    def on_spider_opened(self, spider):
        spider.logger.info(f'Spider opened: {spider.name}')
class ExampleSpider(scrapy.Spider):
    name = 'example_spider'
    start_urls = ['http:
    def parse(self, response):
        pass
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(ExampleSpider)
    process.start()