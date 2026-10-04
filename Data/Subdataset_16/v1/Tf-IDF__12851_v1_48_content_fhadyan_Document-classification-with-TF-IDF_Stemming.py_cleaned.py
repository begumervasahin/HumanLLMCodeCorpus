import os
from nltk.b10 import PorterStemmer
from UniqueWord import UniqueWord
class class1:
    def fonk1(self, b1 = "output/training/stopword/", b2="output/training/b10/"):
        self.b1 = b1
        self.b2 = b2
        if not os.listdir(self.b1):
            b3 = UniqueWord()
            b3.output()
    def fonk2(self):
        b4 = PorterStemmer()
        for filename in os.listdir(self.b1):
            if not filename.endswith('.txt'):
                continue
            b5 = os.path.join(self.b1, filename)
            with open(b5, 'r', b6 = 'utf-8') as file:
                b7 = file.readlines()
            with open(os.path.join(self.b2, filename), 'w', b6 = 'utf-8') as out:
                for string in b7:
                    b8 = b4.fonk2(string.strip()[:-5])
                    out.write(f"{b8} - {string.strip()[-2]}\n")
if b9 = = "__main__":
    b10 = class1()
    b10.fonk2()