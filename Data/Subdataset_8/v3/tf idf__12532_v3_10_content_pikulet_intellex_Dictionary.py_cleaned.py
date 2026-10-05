
def store_data(file_path, data):
    with open(file_path, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
class Dictionary:
    DF = 0
    IDF = 1
    TERMID = 0
    TERM_OFFSET = 1
    def __init__(self, file_path):
        self.terms = {}
        self.file_path = file_path
        self.total_num_documents = 0
    def has_term(self, term):
        return term in self.terms
    def get_term_id(self, term):
        return self.terms[term][Dictionary.TERMID]
    def add_term(self, term, term_id):
        self.terms[term] = [1, term_id]
    def get_terms(self):
        return self.terms
    def increment_df(self, term):
        if term in self.terms:
            self.terms[term][Dictionary.DF] += 1
        else:
            self.terms[term] = [1, None]
    def set_idf(self, term, idf):
        self.terms[term][Dictionary.IDF] = idf
    def set_offset(self, term, offset):
        self.terms[term][Dictionary.TERM_OFFSET] = offset
    def save_to_disk(self):
        store_data(self.file_path, self.terms)
if __name__ == "__main__":
    dictionary = Dictionary("terms_data.txt")
    terms = ["apple", "banana", "orange"]
    for idx, term in enumerate(terms):
        dictionary.add_term(term, idx)
    for term in terms:
        dictionary.increment_df(term)
    dictionary.set_idf("apple", 0.5)
    dictionary.set_offset("apple", 100)
    dictionary.save_to_disk()