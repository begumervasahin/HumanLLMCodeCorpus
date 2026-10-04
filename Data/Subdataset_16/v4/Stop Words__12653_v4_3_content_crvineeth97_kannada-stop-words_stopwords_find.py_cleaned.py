import nltk
nltk.download('punkt')
from textblob import TextBlob as tb
import json
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = {}
        self.b4 = []
        self.a1 = 0
    def fonk2(self):
        for corpus_path in self.b1:
            with open(corpus_path, 'r') as file:
                self.b2 = json.load(file)
                self.fonk3()
        self.fonk4()
    def fonk3(self):
        for document in self.b2:
            b5 = '. '.join(document['b5'])
            b5 = b5.replace('..', '.')
            self.b4.append(tb(b5))
        self.a1 = len(self.b4)
    def fonk4(self):
        for blob in self.b4:
            for word in set(blob.words):
                if word not in self.b3:
                    self.b3[word] = 0
                self.b3[word] += 1
    def fonk5(self):
        b6 = "stop-words.txt"
        with open(b6, 'w') as out_file:
            for word, count in sorted(self.b3.items(), b7 = lambda x: x[1], reverse=True)[:102]:
                out_file.write(f"{word}\n")
b1 = ["udayavani.json"]
b8 = class1(b1)
b8.fonk2()
b8.fonk5()