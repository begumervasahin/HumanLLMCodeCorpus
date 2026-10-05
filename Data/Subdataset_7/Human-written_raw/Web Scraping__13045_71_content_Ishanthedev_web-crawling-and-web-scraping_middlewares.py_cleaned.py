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
        for i in result:
            yield i
    def fonk4(self, response, exception, spider):
        pass
    def fonk5(self, start_requests, spider):
        for r in start_requests:
            yield r
    def fonk6(self, spider):
        spider.logger.info('Spider opened: %b1' % spider.name)
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
        spider.logger.info('Spider opened: %b1' % spider.name)