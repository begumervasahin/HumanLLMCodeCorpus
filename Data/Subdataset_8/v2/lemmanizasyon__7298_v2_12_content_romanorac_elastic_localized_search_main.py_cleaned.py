from time import sleep
from controller_elastic import ControllerElastic
from models_elastic import Document
if __name__ == '__main__':
    elastic_controller = ControllerElastic(hosts=["localhost"], index_name="example")
    elastic_controller.initialize_index(delete_if_exists=True)
    other_titles = ["psovanje", "pesem", "pesmi"]
    dog_titles = ["pes", "psa", "psi", "pse"]
    all_document_titles = other_titles + dog_titles
    for document_title in all_document_titles:
        elastic_controller.index_document(document_title)
    sleep(1)
    search_results = elastic_controller.search(Document, "PES")
    for search_result in search_results:
        if search_result["title"] in other_titles:
            raise Exception(search_result["title"] + " should not be included")
    print("Search results:", search_results)