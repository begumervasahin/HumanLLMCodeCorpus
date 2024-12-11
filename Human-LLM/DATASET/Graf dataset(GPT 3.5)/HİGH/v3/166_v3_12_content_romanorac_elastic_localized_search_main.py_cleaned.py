from time import sleep
from controller_elastic import ControllerElastic
from models_elastic import Document
def fonk1():
    b1 = ControllerElastic(hosts=["localhost"], index_name="example")
    b1.initialize_index(b2 = True)
    b3 = ["psovanje", "pesem", "pesmi"]
    b4 = ["pes", "psa", "psi", "pse"]
    b5 = b3 + b4
    for document_title in b5:
        b1.index_document(document_title)
    sleep(1)
    b6 = b1.search(Document, "PES")
    for search_result in b6:
        if search_result["title"] in b3:
            raise Exception(search_result["title"] + " should not be included")
    print("Search results:", b6)
if b7 = = '__main__':
    fonk1()