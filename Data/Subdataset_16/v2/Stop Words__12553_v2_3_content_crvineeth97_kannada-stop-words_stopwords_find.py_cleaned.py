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
        self.fonk3()
        self.fonk4()
        self.fonk5()
    def fonk3(self):
        for path in self.b1:
            with open(path, 'r', b5 = 'utf-8') as file:
                self.b2.extend(json.load(file))
    def fonk4(self):
        for document in self.b2:
            b6 = '. '.join(document['b6'])
            b6 = b6.replace('..', '.')
            self.b4.append(tb(b6))
        self.a1 = len(self.b4)
    def fonk5(self):
        for blob in self.b4:
            for word in set(blob.words):
                self.b3[word] = self.b3.get(word, 0) + 1
    def fonk6(self, b7 = 102):
        b8 = "stop-words.txt"
        with open(b8, 'w', b5 = 'utf-8') as out_file:
            for b9, val in sorted(self.b3.items(), b9 = lambda x: x[1], reverse=True)[:b7]:
                out_file.write(f"{b9}\n")
b1 = ["udayavani.json"]
b10 = class1(b1)
b10.fonk2()
b10.fonk6()