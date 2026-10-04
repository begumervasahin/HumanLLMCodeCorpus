import nltk
nltk.download('punkt')
from textblob import TextBlob as tb
import json
class TfIdf:
    def __init__(self, corpus_paths):
        self.corpus_paths = corpus_paths
        self.corpus = []
        self.word_df_dict = {}
        self.blob_list = []
    def setup(self):
        self.load_corpus_files()
        self.build_corpus()
        self.calculate_word_frequency()
    def load_corpus_files(self):
        for path in self.corpus_paths:
            with open(path, 'r', encoding='utf-8') as file:
                self.corpus.extend(json.load(file))
    def build_corpus(self):
        for document in self.corpus:
            content = '. '.join(document['content'])
            content = content.replace('..', '.')
            self.blob_list.append(tb(content))
    def calculate_word_frequency(self):
        for blob in self.blob_list:
            for word in set(blob.words):
                if word not in self.word_df_dict:
                    self.word_df_dict[word] = 0
                self.word_df_dict[word] += 1
    def write_to_file(self, filename="stop-words.txt", top_n=102):
        """
        Write the top N most frequent words to a file.
        Parameters:
        - filename: The name of the output file (default is "stop-words.txt").
        - top_n: The number of top frequent words to write (default is 102).
        """
        with open(filename, 'w', encoding='utf-8') as out_file:
            for word, freq in sorted(self.word_df_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]:
                out_file.write(f"{word}\n")
corpus_paths = ["udayavani.json"]
tfidf = TfIdf(corpus_paths)
tfidf.setup()
tfidf.write_to_file()