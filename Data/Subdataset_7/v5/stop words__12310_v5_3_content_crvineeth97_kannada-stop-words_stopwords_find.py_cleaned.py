import nltk
import json
from textblob import TextBlob as tb
nltk.download('punkt')
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self):
        for corpus_path in self.b1:
            self.fonk3(corpus_path)
        self.fonk5()
    def fonk3(self, corpus_path):
        with open(corpus_path, 'r') as file:
            b3 = json.load(file)
            self.fonk4(b3)
    def fonk4(self, b3):
        for document in b3:
            b4 = '. '.join(document['b4'])
            b4 = b4.replace('..', '.')
            self.blob_list.append(tb(b4))
    def fonk5(self):
        for blob in self.blob_list:
            for word in set(blob.words):
                self.b2[word] = self.b2.get(word, 0) + 1
    def fonk6(self):
        b5 = "stop-words.txt"
        with open(b5, 'w') as output_file:
            for word, frequency in sorted(self.b2.items(), b6 = lambda x: x[1], reverse=True)[:102]:
                output_file.write(f"{word}\n")
b1 = ["udayavani.json"]
b7 = class1(b1)
b7.fonk2()
b7.fonk6()