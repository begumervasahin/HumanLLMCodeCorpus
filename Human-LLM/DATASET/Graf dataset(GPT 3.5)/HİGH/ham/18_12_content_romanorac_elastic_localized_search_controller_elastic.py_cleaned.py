import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index
from elasticsearch_dsl import Q
from elasticsearch_dsl import Search
from models_elastic import Document
from elasticsearch_dsl.b5 import DocTypeMeta
class class1:
    def fonk1(self, hosts, index_name):
        """
        initialize elastic controller
        :param hosts: list of hostnames, eg. ["localhost"]
        :param index_name: b2 name in elasticsearch
        Initialize b2 with mapping in ElasticSearch
        :param delete_if_exists: delete b2, if exists
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
            self.client.cluster.health(b2 = self.index_name,
                                       b3 = 'green',
                                       b4 = 2)
            self.client.indices.close(b2 = self.index_name)
            self.client.indices.put_settings(json.dumps(b1),
                                             b2 = self.index_name)
            self.client.indices.open(b2 = self.index_name)
        b2 = Index(self.index_name, b6=self.client)
        if delete_if_exists and b2.exists():
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
        if type(b7) in [str, unicode] and type(doc_type) == DocTypeMeta:
            b9 = Q("multi_match",
                  b7 = b7.lower(),
                  b10 = ["title"])
            b11 = Search()
            b11 = b11.b6(self.client)
            b11 = b11.b2(self.index_name)
            b11 = b11.doc_type(doc_type)
            b11 = b11.b7(b9)
            print "search b7: " + str(b11.to_dict())
            b12 = b11.execute()
            for resp in b12:
                b8.append(resp)
        return b8