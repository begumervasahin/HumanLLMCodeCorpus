
from data_helper import store_data
class Dictionary:
    DOCUMENT_FREQUENCY = 0
    IDF = 0
    TERM_ID = 1
    TERM_OFFSET = 1
    def __init__(self, file_path):
        self.terms = {}
        self.file_path = file_path
        self.total_num_documents = 0
    def has_term(self, term):
        return term in self.terms
    def get_term_id(self, term):
        return self.terms[term][Dictionary.TERM_ID]
    def add_term(self, term, term_id):
        self.terms[term] = [1, term_id]
    def get_terms(self):
        return self.terms
    def add_document_frequency(self, term):
        self.terms[term][Dictionary.DOCUMENT_FREQUENCY] += 1
    def set_idf(self, term, idf):
        self.terms[term][Dictionary.IDF] = idf
    def set_offset(self, term, offset):
        self.terms[term][Dictionary.TERM_OFFSET] = offset
    def save_to_disk(self):
        store_data(self.file_path, self.terms)