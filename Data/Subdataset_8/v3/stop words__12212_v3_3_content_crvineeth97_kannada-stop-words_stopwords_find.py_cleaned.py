import nltk
import json
from textblob import TextBlob as tb
nltk.download('punkt')
class TfIdf:
    def __init__(self, corpus_paths):
        self.corpus_paths = corpus_paths
        self.corpus = []
        self.word_df_dict = {}
    def setup(self):
        for path in self.corpus_paths:
            with open(path, 'r') as file:
                data = json.load(file)
                self.corpus.extend(data)
        self.calculate_word_frequency()
    def build_corpus(self, content):
        return tb(' '.join(content))
    def calculate_word_frequency(self):
        for document in self.corpus:
            content = document['content']
            blob = self.build_corpus(content)
            for word in set(blob.words):
                self.word_df_dict[word] = self.word_df_dict.get(word, 0) + 1
    def write_to_file(self, filename="stop-words.txt", top_n=102):
        with open(filename, 'w') as out_file:
            for key, val in sorted(self.word_df_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]:
                out_file.write(key + '\n')
corpus_paths = ["udayavani.json"]
tfidf = TfIdf(corpus_paths)
tfidf.setup()
tfidf.write_to_file()