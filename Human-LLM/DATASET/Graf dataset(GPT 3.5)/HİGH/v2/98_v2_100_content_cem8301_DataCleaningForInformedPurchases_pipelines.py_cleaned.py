import scrapy
class class1(object):
    def fonk1(self, b4, spider):
        return b4
class class2(scrapy.Spider):
    b1 = 'my_spider'
    b2 = ['https:
    b3 = {
        'ITEM_PIPELINES': {
            'my_project.pipelines.class1': 100,
        }
    }
    def fonk2(self, response):
        b4 = {
            'title': response.css('title::text').get(),
            'url': response.url,
        }
        yield b4