import scrapy
class CraigslistPipeline(object):
    def process_item(self, item, spider):
        return item
class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https:
    custom_settings = {
        'ITEM_PIPELINES': {
            'my_project.pipelines.CraigslistPipeline': 100,
        }
    }
    def parse(self, response):
        item = {
            'title': response.css('title::text').get(),
            'url': response.url,
        }
        yield item