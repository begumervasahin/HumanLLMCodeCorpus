import scrapy
from scrapy import signals
class class1(object):
    @classmethod
    def fonk1(cls, crawler):
        b1 = cls()
        crawler.signals.connect(b1.spider_opened, b2 = signals.spider_opened)
        return b1
    def fonk2(self, response, spider):
        return None
    def fonk3(self, response, result, spider):
        for item in result:
            yield item
    def fonk4(self, response, exception, spider):
        pass
    def fonk5(self, start_requests, spider):
        for request in start_requests:
            yield request
    def fonk6(self, spider):
        spider.logger.info('Spider opened: %s' % spider.b3)
class class2(object):
    @classmethod
    def fonk7(cls, crawler):
        b1 = cls()
        crawler.signals.connect(b1.spider_opened, b2 = signals.spider_opened)
        return b1
    def fonk8(self, request, spider):
        return None
    def fonk9(self, request, response, spider):
        return response
    def fonk10(self, request, exception, spider):
        pass
    def fonk11(self, spider):
        spider.logger.info('Spider opened: %s' % spider.b3)
class class3(scrapy.Spider):
    b3 = 'myspider'
    b4 = ['http:
    def fonk12(self, response):
        pass
if b5 = = "__main__":
    from scrapy.crawler import CrawlerProcess
    b6 = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    b6.crawl(class3)
    b6.start()