from scrapy import signals
class class1:
    @classmethod
    def fonk1(cls, crawler):
        b1 = cls()
        b1.fonk9(crawler)
        return b1
    def fonk2(self, crawler):
        crawler.signals.connect(self.spider_opened, b2 = signals.spider_opened)
    def fonk3(self, response, spider):
        return None
    def fonk4(self, response, result, spider):
        for item in result:
            yield item
    def fonk5(self, response, exception, spider):
        pass
    def fonk6(self, start_requests, spider):
        for request in start_requests:
            yield request
    def fonk7(self, spider):
        spider.logger.info(f'Spider opened: {spider.name}')
class class2:
    @classmethod
    def fonk8(cls, crawler):
        b1 = cls()
        b1.fonk9(crawler)
        return b1
    def fonk9(self, crawler):
        crawler.signals.connect(self.spider_opened, b2 = signals.spider_opened)
    def fonk10(self, request, spider):
        return None
    def fonk11(self, request, response, spider):
        return response
    def fonk12(self, request, exception, spider):
        pass
    def fonk13(self, spider):
        spider.logger.info(f'Spider opened: {spider.name}')