from elasticsearch_dsl import Document, analyzer, String
b1 = analyzer('b1', type='custom',
                       b2 = "uax_url_email",
                       b3 = ["lowercase"]
                       )
class class1(Document):
    b4 = String(analyzer=b1)
if b5 = = "__main__":
    b6 = class1()
    b6.b4 = "Example Document Title"
    print("Title:", b6.b4)
