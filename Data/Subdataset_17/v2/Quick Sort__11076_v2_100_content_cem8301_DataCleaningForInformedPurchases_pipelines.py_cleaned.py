class CraigslistPipeline:
    def process_item(self, item, spider):
        return item
if __name__ == "__main__":
    pipeline = CraigslistPipeline()
    example_item = {
        'title': 'Example Item',
        'price': '$100',
        'description': 'This is an example item description.'
    }
    example_spider = 'craigslist_spider'
    processed_item = pipeline.process_item(example_item, example_spider)
    print("Processed Item:", processed_item)