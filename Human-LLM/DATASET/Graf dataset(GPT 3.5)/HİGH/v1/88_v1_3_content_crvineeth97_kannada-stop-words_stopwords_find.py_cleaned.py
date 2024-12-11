import nltk
from textblob import TextBlob as tb
import json
nltk.download('punkt')
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = {}
    def fonk2(self):
        for path in self.b1:
            with open(path, 'r') as file:
                b4 = json.load(file)
                self.b2.extend(b4)
        self.fonk4()
    def fonk3(self, b5):
        return tb(' '.join(b5))
    def fonk4(self):
        for document in self.b2:
            b5 = document['b5']
            b6 = self.fonk3(b5)
            for word in set(b6.words):
                self.b3[word] = self.b3.get(word, 0) + 1
    def fonk5(self, b7 = "stop-words.txt", top_n=102):
        with open(b7, 'w') as outFile:
            for b8, val in sorted(self.b3.items(), b8 = lambda x: x[1], reverse=True)[:top_n]:
                outFile.write(b8 + '\n')
b1 = ["udayavani.json"]
b9 = class1(b1)
b9.fonk2()
b9.fonk5()