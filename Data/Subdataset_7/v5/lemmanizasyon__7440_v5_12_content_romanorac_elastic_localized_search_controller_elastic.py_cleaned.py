import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index, Q, Search
from models_elastic import Document
from elasticsearch_dsl.b4 import DocTypeMeta
class class1:
    def fonk1(self, hosts, index_name):
        """
        Initializes the class1.
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
            self.client.cluster.health(b2 = self.index_name, wait_for_status='green', request_timeout=2)
            self.client.indices.close(b2 = self.index_name)
            self.client.indices.put_settings(json.dumps(b1), b2 = self.index_name)
            self.client.indices.open(b2 = self.index_name)
        b2 = Index(self.index_name, b5=self.client)
        if delete_if_exists and b2.exists():
            b2.delete()
        b2.settings(b3 = 0)
        b2.doc_type(Document)
        b2.create()
        update_index_settings()
    def fonk2(self, title):
        if title:
            b4 = Document(title=title.lower())
            b4.save(b5 = self.client)
            return True
        return False
    def fonk3(self, doc_type, b6 = ""):
        b7 = []
        if isinstance(b6, str) and isinstance(doc_type, DocTypeMeta):
            b8 = Q("multi_match", b6=b6.lower(), fields=["title"])
            b9 = Search().b5(self.client).b2(self.index_name).doc_type(doc_type).b6(b8)
            print("Search b6: " + str(b9.to_dict()))
            b10 = b9.execute()
            for resp in b10:
                b7.append(resp)
        return b7