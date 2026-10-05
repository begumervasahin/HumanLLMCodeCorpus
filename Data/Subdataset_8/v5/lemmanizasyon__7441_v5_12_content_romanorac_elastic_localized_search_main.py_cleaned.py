from time import sleep
from controller_elastic import ControllerElastic
from models_elastic import Document
def main():
    elastic_controller = ControllerElastic(hosts=["localhost"], index_name="example")
    elastic_controller.initialize_index(delete_if_exists=True)
    other_titles = ["psovanje", "pesem", "pesmi"]
    dog_titles = ["pes", "psa", "psi", "pse"]
    document_titles = other_titles + dog_titles
    for document_title in document_titles:
        elastic_controller.index_document(document_title)
    sleep(1)
    search_results = elastic_controller.search(Document, "PES")
    for result in search_results:
        if result["title"] in other_titles:
            raise Exception(result["title"] + " should not be here")
    print("Search hits: " + str(search_results))
if __name__ == '__main__':
    main()