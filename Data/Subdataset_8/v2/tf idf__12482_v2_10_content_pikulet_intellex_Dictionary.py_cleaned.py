
def store_data(file_path, data):
    with open(file_path, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
class Dictionary:
    DF = 0
    IDF = 0
    TERMID = 1
    TERM_OFFSET = 1
    def __init__(self, file):
        self.terms = {}
        self.file = file
        self.total_num_documents = 0
    def has_term(self, t):
        return t in self.terms
    def get_termID(self, t):
        return self.terms[t][Dictionary.TERMID]
    def add_term(self, t, termID):
        self.terms[t] = [1, termID]
    def get_terms(self):
        return self.terms
    def add_df(self, t):
        if t in self.terms:
            self.terms[t][Dictionary.DF] += 1
        else:
            self.terms[t] = [1, None]
    def set_idf(self, t, idf):
        self.terms[t][Dictionary.IDF] = idf
    def set_offset(self, t, offset):
        self.terms[t][Dictionary.TERM_OFFSET] = offset
    def save_to_disk(self):
        store_data(self.file, self.terms)
if __name__ == "__main__":
    dictionary = Dictionary("terms_data.txt")
    terms = ["apple", "banana", "orange"]
    for idx, term in enumerate(terms):
        dictionary.add_term(term, idx)
    for term in terms:
        dictionary.add_df(term)
    dictionary.set_idf("apple", 0.5)
    dictionary.set_offset("apple", 100)
    dictionary.save_to_disk()