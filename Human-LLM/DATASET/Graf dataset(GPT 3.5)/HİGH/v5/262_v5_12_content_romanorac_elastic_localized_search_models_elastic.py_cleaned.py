
from elasticsearch_dsl.document import DocType
from elasticsearch_dsl import analyzer, String
b1 = analyzer(
    'lemmagen_sl',
    b2 = 'custom',
    b3 = "uax_url_email",
    b4 = ["lowercase"]
)
class class1(DocType):
    b5 = String(analyzer=b1)