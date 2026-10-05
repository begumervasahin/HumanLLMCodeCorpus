import nltk
from textblob import TextBlob as tb
import json
nltk.download('punkt')
class TfIdf:
    def __init__(self, corpusPath):
        self.corpus_paths = corpusPath
        self.corpus = ""
        self.word_df_dict = {}
        self.blob_list = []
        self.blob_list_length = 0
    def setup(self):
        for corpus_path in self.corpus_paths:
            self.corpus = json.load(open(corpus_path, 'r'))
            self.build_corpus()
        self.calculate_word_frequency()
    def build_corpus(self):
        for document in self.corpus:
            content = '. '.join(document['content'])
            content.replace('..', '.')
            self.blob_list.append(tb(content))
        self.blob_list_length = len(self.blob_list)
    def calculate_word_frequency(self):
        for blob in self.blob_list:
            for word in set(blob.words):
                if word not in self.word_df_dict:
                    self.word_df_dict[word] = 0
                self.word_df_dict[word] += 1
    def write_to_file(self):
        output_file_name = "stop-words.txt"
        with open(output_file_name, 'w') as output_file:
            for key, val in sorted(self.word_df_dict.items(), key=lambda x: x[1], reverse=True)[:102]:
                output_file.write(key + '\n')
corpus_paths = ["udayavani.json"]
tfidf = TfIdf(corpus_paths)
tfidf.setup()
tfidf.write_to_file()