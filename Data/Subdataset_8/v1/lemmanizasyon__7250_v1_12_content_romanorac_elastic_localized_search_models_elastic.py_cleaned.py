from elasticsearch_dsl import Document, analyzer, String
lemmagen_sl = analyzer('lemmagen_sl', type='custom',
                       tokenizer="uax_url_email",
                       filter=["lowercase"]
                       )
class MyDocument(Document):
    title = String(analyzer=lemmagen_sl)
if __name__ == "__main__":
    doc = MyDocument()
    doc.title = "Example Document Title"
    print("Title:", doc.title)
