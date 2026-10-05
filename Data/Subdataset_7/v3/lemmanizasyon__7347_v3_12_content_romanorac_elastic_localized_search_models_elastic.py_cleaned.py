from elasticsearch_dsl import Document, analyzer, String
b1 = analyzer(
    'lemmagen_sl',
    b2 = 'custom',
    b3 = "uax_url_email",
    b4 = ["lowercase"]
)
class class1(Document):
    b5 = String(analyzer=b1)
if b6 = = "__main__":
    b7 = class1()
    b7.b5 = "Example Document Title"
    print("Title:", b7.b5)
