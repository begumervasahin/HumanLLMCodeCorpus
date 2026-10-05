import scrapy
from scrapy import signals
class QuotetutorialSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        middleware_instance = cls()
        crawler.signals.connect(middleware_instance.spider_opened, signal=signals.spider_opened)
        return middleware_instance
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
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
class QuotetutorialDownloaderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        middleware_instance = cls()
        crawler.signals.connect(middleware_instance.spider_opened, signal=signals.spider_opened)
        return middleware_instance
    def process_request(self, request, spider):
        return None
    def process_response(self, request, response, spider):
        return response
    def process_exception(self, request, exception, spider):
        pass
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http:
    def parse(self, response):
        pass
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(MySpider)
    process.start()