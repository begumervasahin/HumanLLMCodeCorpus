import nltk
from textblob import TextBlob as tb
import json
nltk.download('punkt')
class class1:
    def fonk1(self, corpusPath):
        self.b1 = corpusPath
        self.b2 = ""
        self.b3 = {}
        self.b4 = []
        self.a1 = 0
    def fonk2(self):
        for corpus_path in self.b1:
            self.b2 = json.load(open(corpus_path, 'r'))
            self.fonk3()
        self.fonk4()
    def fonk3(self):
        for document in self.b2:
            b5 = '. '.join(document['b5'])
            b5.replace('..', '.')
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
        with open(b6, 'w') as output_file:
            for b7, val in sorted(self.b3.items(), b7 = lambda x: x[1], reverse=True)[:102]:
                output_file.write(b7 + '\n')
b1 = ["udayavani.json"]
b8 = class1(b1)
b8.fonk2()
b8.fonk5()