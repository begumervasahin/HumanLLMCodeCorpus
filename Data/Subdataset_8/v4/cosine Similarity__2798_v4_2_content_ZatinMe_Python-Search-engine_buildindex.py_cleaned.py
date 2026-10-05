import re
import math
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
class BuildIndex:
    def __init__(self, files):
        self.term_frequency = {}
        self.document_frequency = {}
        self.inverse_document_frequency = {}
        self.filenames = files
        self.file_to_terms = self._process_files(self.filenames)
        self.index = self._build_index(self.filenames)
        self.vector_space = self._vectorize()
        self.magnitudes = self._calculate_magnitudes(self.filenames)
        self._populate_scores()
    def _process_files(self, filenames):
        file_to_terms = {}
        for file in filenames:
            with open(file, 'r') as f:
                text = f.read().lower()
                text = re.sub(r'[\W_]+', ' ', text)
                terms = text.split()
                file_to_terms[file] = [PorterStemmer().stem(term) for term in terms]
        return file_to_terms
    def _build_index(self, filenames):
        index = {}
        for file, terms in self.file_to_terms.items():
            index[file] = self._index_one_file(terms)
        return index
    def _index_one_file(self, terms):
        index = {}
        for position, term in enumerate(terms):
            if term in index:
                index[term].append(position)
            else:
                index[term] = [position]
        return index
    def _vectorize(self):
        vectors = {}
        for filename in self.filenames:
            vectors[filename] = [len(self.index[filename][term]) for term in self.index[filename]]
        return vectors
    def _calculate_magnitudes(self, documents):
        magnitudes = {}
        for document in documents:
            magnitudes[document] = pow(sum(len(positions)**2 for positions in self.index[document].values()), 0.5)
        return magnitudes
    def _populate_scores(self):
        for filename in self.filenames:
            for term in self.get_uniques():
                self.term_frequency[(filename, term)] = self._calculate_term_frequency(term, filename)
                if term not in self.document_frequency:
                    self.document_frequency[term] = len(self.index[filename][term])
                if term in self.document_frequency:
                    self.inverse_document_frequency[term] = self._calculate_inverse_document_frequency(term)
        return self.term_frequency, self.document_frequency, self.inverse_document_frequency
    def _calculate_term_frequency(self, term, document):
        return len(self.index[document][term]) / self.magnitudes[document] if term in self.index[document] else 0
    def _calculate_inverse_document_frequency(self, term):
        N = len(self.filenames)
        N_t = self.document_frequency[term]
        return math.log(1 + N / N_t) if N_t != 0 else 1
    def generate_score(self, term, document):
        return self.term_frequency[(document, term)] * self.inverse_document_frequency[term]
    def get_uniques(self):
        return set(term for index in self.index.values() for term in index.keys())
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt"]
    index = BuildIndex(files)
    print("TF:", index.term_frequency)
    print("DF:", index.document_frequency)
    print("IDF:", index.inverse_document_frequency)