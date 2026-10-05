from elasticsearch_dsl.document import DocType
from elasticsearch_dsl import analyzer, String
b1 = analyzer('b1', type='custom',
                       b2 = "uax_url_email",
                       b3 = ["lowercase"],
                       )
class class1(DocType):
    b4 = String(analyzer=b1)