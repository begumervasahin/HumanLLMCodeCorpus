import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index, Q, Search
from elasticsearch_dsl.b5 import DocTypeMeta
from models_elastic import Document
class class1:
    def fonk1(self, b14, b15):
        """
        initialize elastic b16
        :param b14: list of hostnames, eg. ["localhost"]
        :param b15: b2 name in elasticsearch
        Initialize b2 with mapping in ElasticSearch
        :param b17: delete b2, if exists
        :return: None
            Function updates settings for slovenian lemmatization of words.
            As far as we know, elasticsearch-dsl library does not support
            custom filter settings.
            :return: None
            """
            b1 = {
                "analysis": {
                    "filter": {
                        "lemmagen_filter_sl": {
                            "type": "lemmagen",
                            "lexicon": "sl"
                        }
                    },
                    "analyzer": {
                        "lemmagen_sl": {
                            "type": "custom",
                            "tokenizer": "uax_url_email",
                            "filter": [
                                "lemmagen_filter_sl",
                                "lowercase"
                            ]
                        }
                    }
                }
            }
            self.client.cluster.health(b2 = self.b15,
                                       b3 = 'green',
                                       b4 = 2)
            self.client.indices.close(b2 = self.b15)
            self.client.indices.put_settings(json.dumps(b1),
                                             b2 = self.b15)
            self.client.indices.open(b2 = self.b15)
        b2 = Index(self.b15, b6=self.client)
        if b17 and b2.exists():
            b2.delete()
        b2.settings(
            a1 = 0
        )
        b2.doc_type(Document)
        b2.create()
        update_index_settings()
    def fonk2(self, title):
        if title:
            b5 = Document(title=title.lower())
            b5.save(b6 = self.client)
            return True
        return False
    def fonk3(self, doc_type, b7 = ""):
        b8 = []
        if isinstance(b7, str) and issubclass(doc_type, DocTypeMeta):
            b9 = Q("multi_match",
                  b7 = b7.lower(),
                  b10 = ["title"])
            b11 = Search()
            b11 = b11.b6(self.client)
            b11 = b11.b2(self.b15)
            b11 = b11.doc_type(doc_type)
            b11 = b11.b7(b9)
            print("search b7: " + str(b11.to_dict()))
            b12 = b11.execute()
            for resp in b12:
                b8.append(resp)
        return b8
if b13 = = "__main__":
    b14 = ["localhost"]
    b15 = "example_index"
    b16 = class1(b14, b15)
    b16.initialize_index(b17 = True)
    b18 = ["Document 1", "Document 2", "Document 3"]
    for doc in b18:
        b16.fonk2(doc)
    b19 = b16.fonk3(Document, b7="b5")
    print("Search b8:")
    for result in b19:
        print(result.title)