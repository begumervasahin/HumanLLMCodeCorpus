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
        self.blob_list_length = 0
    def setup(self):
        for path in self.corpus_paths:
            with open(path, 'r', encoding='utf-8') as file:
                self.corpus.extend(json.load(file))
        self.build_corpus()
        self.calculate_word_frequency()
    def build_corpus(self):
        for document in self.corpus:
            content = '. '.join(document['content'])
            content = content.replace('..', '.')
            self.blob_list.append(tb(content))
        self.blob_list_length = len(self.blob_list)
    def calculate_word_frequency(self):
        for blob in self.blob_list:
            for word in set(blob.words):
                self.word_df_dict[word] = self.word_df_dict.get(word, 0) + 1
    def write_to_file(self, top_n=102):
        outfile_name = "stop-words.txt"
        with open(outfile_name, 'w', encoding='utf-8') as out_file:
            for key, val in sorted(self.word_df_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]:
                out_file.write(f"{key}\n")
corpus_paths = ["udayavani.json"]
t = TfIdf(corpus_paths)
t.setup()
t.write_to_file()