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
    def fonk5(self):
        for blob in self.b4:
            for word in set(blob.words):
                if word not in self.b3:
                    self.b3[word] = 0
                self.b3[word] += 1
    def fonk6(self, b7 = "stop-words.txt", top_n=102):
        """
        Write the top N most frequent words to a file.
        Parameters:
        - b7: The name of the output file (default is "stop-words.txt").
        - top_n: The number of top frequent words to write (default is 102).
        """
        with open(b7, 'w', b5 = 'utf-8') as out_file:
            for word, freq in sorted(self.b3.items(), b8 = lambda x: x[1], reverse=True)[:top_n]:
                out_file.write(f"{word}\n")
b1 = ["udayavani.json"]
b9 = class1(b1)
b9.fonk2()
b9.fonk6()