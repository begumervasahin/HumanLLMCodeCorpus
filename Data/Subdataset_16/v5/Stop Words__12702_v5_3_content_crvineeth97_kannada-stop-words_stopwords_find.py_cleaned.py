import nltk
nltk.download('punkt')
from textblob import TextBlob as tb
import json
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = {}
    def fonk2(self):
        self.fonk3()
        self.fonk5()
    def fonk3(self):
        for corpus_path in self.b1:
            with open(corpus_path, 'r') as file:
                b4 = json.load(file)
                self.fonk4(b4)
    def fonk4(self, b4):
        for document in b4:
            b5 = '. '.join(document['b5']).replace('..', '.')
            self.b2.append(tb(b5))
    def fonk5(self):
        for blob in self.b2:
            b6 = set(blob.words)
            for word in b6:
                if word not in self.b3:
                    self.b3[word] = 0
                self.b3[word] += 1
    def fonk6(self, b7 = "stop-words.txt"):
        b8 = sorted(self.b3.items(), key=lambda x: x[1], reverse=True)[:102]
        with open(b7, 'w') as out_file:
            for word, _ in b8:
                out_file.write(f"{word}\n")
if b9 = = "__main__":
    b1 = ["udayavani.json"]
    b10 = class1(b1)
    b10.fonk2()
    b10.fonk6()