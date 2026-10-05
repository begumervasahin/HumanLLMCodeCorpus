import re
import math
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
class BuildIndex:
    def __init__(self, files):
        self.tf = {}
        self.df = {}
        self.idf = {}
        self.filenames = files
        self.file_to_terms = self._process_files(self.filenames)
        self.regdex = self._build_regdex(self.filenames)
        self.total_index = self._build_full_index()
        self.vectors = self._vectorize()
        self.magnitudes = self._calculate_magnitudes(self.filenames)
        self._populate_scores()
    def _process_files(self, filenames):
        file_to_terms = {}
        for file in filenames:
            text = open(file, 'r').read().lower()
            text = re.sub(r'[\W_]+', ' ', text)
            file_to_terms[file] = text.split()
        return file_to_terms
    def _index_one_file(self, termlist):
        file_index = {}
        ps = PorterStemmer()
        for index, words in enumerate(termlist):
            for word in word_tokenize(words):
                word = word.lower().strip('.').strip(',')
                word = ps.stem(word)
                if word in file_index:
                    file_index[word].append(index)
                else:
                    file_index[word] = [index]
        return file_index
    def _build_regdex(self, filenames):
        file_to_terms = {}
        for file in filenames:
            file_to_terms[file] = self.file_to_terms[file]
        return self._make_indices(file_to_terms)
    def _make_indices(self, termlists):
        total = {}
        for filename in termlists.keys():
            total[filename] = self._index_one_file(termlists[filename])
        return total
    def _build_full_index(self):
        total_index = {}
        indie_indices = self.regdex
        for filename in indie_indices.keys():
            self.tf[filename] = {}
            for word in indie_indices[filename].keys():
                self.tf[filename][word] = len(indie_indices[filename][word])
                if word in self.df.keys():
                    self.df[word] += 1
                else:
                    self.df[word] = 1
                if word in total_index.keys():
                    if filename in total_index[word].keys():
                        total_index[word][filename].append(indie_indices[filename][word][:])
                    else:
                        total_index[word][filename] = indie_indices[filename][word]
                else:
                    total_index[word] = {filename: indie_indices[filename][word]}
        return total_index
    def _vectorize(self):
        vectors = {}
        for filename in self.filenames:
            vectors[filename] = [len(self.regdex[filename][word]) for word in self.regdex[filename].keys()]
        return vectors
    def _calculate_magnitudes(self, documents):
        magnitudes = {}
        for document in documents:
            magnitudes[document] = pow(sum(map(lambda x: x**2, self.vectors[document])), 0.5)
        return magnitudes
    def _term_frequency(self, term, document):
        return self.tf[document][term] / self.magnitudes[document] if term in self.tf[document].keys() else 0
    def _populate_scores(self):
        for filename in self.filenames:
            for term in self.get_uniques():
                self.tf[filename][term] = self._term_frequency(term, filename)
                if term in self.df.keys():
                    self.idf[term] = self._calculate_idf(len(self.filenames), self.df[term])
                else:
                    self.idf[term] = 0
    def _calculate_idf(self, N, N_t):
        return math.log(1 + N / N_t) if N_t != 0 else 1
    def generate_score(self, term, document):
        return self.tf[document][term] * self.idf[term]
    def get_uniques(self):
        return self.total_index.keys()
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt"]
    index = BuildIndex(files)
    print("TF:", index.tf)
    print("DF:", index.df)
    print("IDF:", index.idf)