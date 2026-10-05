from elasticsearch_dsl import Document, analyzer, String
custom_analyzer = analyzer(
    'lemmagen_sl',
    type='custom',
    tokenizer="uax_url_email",
    filter=["lowercase"]
)
class MyDocument(Document):
    title = String(analyzer=custom_analyzer)
if __name__ == "__main__":
    document = MyDocument()
    document.title = "Example Document Title"
    print("Title:", document.title)
