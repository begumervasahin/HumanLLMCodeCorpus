from time import sleep
from controller_elastic import ControllerElastic
from models_elastic import Document
if b1 = = '__main__':
    b2 = ControllerElastic(hosts=["localhost"], index_name="example")
    b2.initialize_index(b3 = True)
    b4 = ["psovanje", "pesem", "pesmi"]
    b5 = ["pes", "psa", "psi", "pse"]
    b6 = b4 + b5
    for document_title in b6:
        b2.index_document(document_title)
    sleep(1)
    b7 = b2.search(Document, "PES")
    for search_result in b7:
        if search_result["title"] in b4:
            raise Exception(search_result["title"] + " should not be included")
    print("Search results:", b7)