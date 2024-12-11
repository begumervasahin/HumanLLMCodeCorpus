from scrapy import signals
class class1:
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
        spider.logger.info('Spider opened: %s' % spider.name)
class class2:
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
        spider.logger.info('Spider opened: %s' % spider.name)
if b3 = = "__main__":
    b4 = class1()
    b5 = class2()
    b4.fonk11(b6 = "test_spider")
    b5.fonk11(b6 = "test_spider")