from scrapy import signals, Spider, Request
from scrapy.crawler import CrawlerProcess
class class1(Spider):
    b1 = 'custom_spider'
    b2 = ['http:
    def fonk1(self, response):
        self.logger.info('Parsing response from: %b3' % response.url)
class class2(object):
    @classmethod
    def fonk2(cls, crawler):
        b3 = cls()
        crawler.signals.connect(b3.spider_opened, b4 = signals.spider_opened)
        return b3
    def fonk3(self, response, spider):
        return None
    def fonk4(self, response, result, spider):
        for i in result:
            yield i
    def fonk5(self, response, exception, spider):
        pass
    def fonk6(self, start_requests, spider):
        for r in start_requests:
            yield r
    def fonk7(self, spider):
        spider.logger.info('Spider opened: %b3' % spider.b1)
class class3(object):
    @classmethod
    def fonk8(cls, crawler):
        b3 = cls()
        crawler.signals.connect(b3.spider_opened, b4 = signals.spider_opened)
        return b3
    def fonk9(self, request, spider):
        return None
    def fonk10(self, request, response, spider):
        return response
    def fonk11(self, request, exception, spider):
        pass
    def fonk12(self, spider):
        spider.logger.info('Spider opened: %b3' % spider.b1)
if b5 = = "__main__":
    b6 = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'LOG_LEVEL': 'INFO',
        'ITEM_PIPELINES': {},
        'DOWNLOADER_MIDDLEWARES': {
            b5 + '.class3': 543,
        },
        'SPIDER_MIDDLEWARES': {
            b5 + '.class2': 543,
        },
    })
    b6.crawl(class1)
    b6.start()
