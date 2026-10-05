
from elasticsearch_dsl.document import DocType
from elasticsearch_dsl import analyzer, String
lemmagen_sl = analyzer(
    'lemmagen_sl',
    type='custom',
    tokenizer="uax_url_email",
    filter=["lowercase"]
)
class Document(DocType):
    title = String(analyzer=lemmagen_sl)