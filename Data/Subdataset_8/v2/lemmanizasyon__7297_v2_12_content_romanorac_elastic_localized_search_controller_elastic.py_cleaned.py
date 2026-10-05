import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index, Q, Search
from elasticsearch_dsl.document import DocTypeMeta
from models_elastic import Document
class ControllerElastic:
    def __init__(self, hosts, index_name):
        """
        Initializes the Elastic controller.
        Args:
            hosts (list): List of hostnames, e.g., ["localhost"].
            index_name (str): Index name in Elasticsearch.
        Initializes the index with mapping in Elasticsearch.
        Args:
            delete_if_exists (bool): If True, deletes index if it already exists.
            Updates settings for Slovenian lemmatization of words.
            """
            analysis_settings = {
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
            self.client.cluster.health(index=self.index_name, wait_for_status='green', request_timeout=2)
            self.client.indices.close(index=self.index_name)
            self.client.indices.put_settings(json.dumps(analysis_settings), index=self.index_name)
            self.client.indices.open(index=self.index_name)
        index = Index(self.index_name, using=self.client)
        if delete_if_exists and index.exists():
            index.delete()
        index.settings(number_of_replicas=0)
        index.doc_type(Document)
        index.create()
        update_index_settings()
    def index_document(self, title):
        if title:
            document = Document(title=title.lower())
            document.save(using=self.client)
            return True
        return False
    def search(self, doc_type, query=""):
        results = []
        if isinstance(query, str) and issubclass(doc_type, DocTypeMeta):
            q = Q("multi_match", query=query.lower(), fields=["title"])
            s = Search()
            s = s.using(self.client)
            s = s.index(self.index_name)
            s = s.doc_type(doc_type)
            s = s.query(q)
            print("search query: " + str(s.to_dict()))
            response = s.execute()
            for resp in response:
                results.append(resp)
        return results
if __name__ == "__main__":
    hosts = ["localhost"]
    index_name = "example_index"
    controller = ControllerElastic(hosts, index_name)
    controller.initialize_index(delete_if_exists=True)
    documents_to_index = ["Document 1", "Document 2", "Document 3"]
    for doc in documents_to_index:
        controller.index_document(doc)
    search_results = controller.search(Document, query="document")
    print("Search results:")
    for result in search_results:
        print(result.title)