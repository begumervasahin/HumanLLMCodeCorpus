import nltk
import json
from textblob import TextBlob as tb
nltk.download('punkt')
class TfIdf:
    def __init__(self, corpus_paths):
        self.corpus_paths = corpus_paths
        self.word_df_dict = {}
    def setup(self):
        for corpus_path in self.corpus_paths:
            self.load_corpus(corpus_path)
        self.calculate_word_frequency()
    def load_corpus(self, corpus_path):
        with open(corpus_path, 'r') as file:
            corpus = json.load(file)
            self.build_blob_list(corpus)
    def build_blob_list(self, corpus):
        for document in corpus:
            content = '. '.join(document['content'])
            content = content.replace('..', '.')
            self.blob_list.append(tb(content))
    def calculate_word_frequency(self):
        for blob in self.blob_list:
            for word in set(blob.words):
                self.word_df_dict[word] = self.word_df_dict.get(word, 0) + 1
    def write_to_file(self):
        output_file_name = "stop-words.txt"
        with open(output_file_name, 'w') as output_file:
            for word, frequency in sorted(self.word_df_dict.items(), key=lambda x: x[1], reverse=True)[:102]:
                output_file.write(f"{word}\n")
corpus_paths = ["udayavani.json"]
tfidf = TfIdf(corpus_paths)
tfidf.setup()
tfidf.write_to_file()