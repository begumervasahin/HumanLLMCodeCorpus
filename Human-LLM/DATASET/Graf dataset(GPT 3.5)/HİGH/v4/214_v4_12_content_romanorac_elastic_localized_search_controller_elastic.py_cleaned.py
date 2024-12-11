import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index, Q, Search
from models_elastic import Document
from elasticsearch_dsl.b5 import DocTypeMeta
class class1:
    def fonk1(self, hosts, index_name):
        """
        Initializes the Elastic controller.
        Args:
            hosts (list): List of hostnames, e.g., ["localhost"]
            index_name (str): Name of the b2 in Elasticsearch
        Initializes the b2 with mapping in Elasticsearch.
        Args:
            delete_if_exists (bool): Whether to delete the b2 if it already exists.
        Returns:
            None
            Updates settings for Slovenian lemmatization of words.
            Elasticsearch-dsl library does not support custom filter settings.
            Returns:
                None
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
        if isinstance(b7, str) and isinstance(doc_type, DocTypeMeta):
            b9 = Q("multi_match",
                  b7 = b7.lower(),
                  b10 = ["title"])
            b11 = Search()
            b11 = b11.b6(self.client)
            b11 = b11.b2(self.index_name)
            b11 = b11.doc_type(doc_type)
            b11 = b11.b7(b9)
            print("Search b7: " + str(b11.to_dict()))
            b12 = b11.execute()
            for resp in b12:
                b8.append(resp)
        return b8