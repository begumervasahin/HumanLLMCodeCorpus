import os
from nltk.stem import PorterStemmer
from UniqueWord import UniqueWord
class class1:
    def fonk1(self, b1 = "output/training/stopword/", b2="output/training/stem/"):
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
            b6 = os.path.join(self.b2, filename)
            with open(b5, 'r', b7 = 'utf-8') as infile:
                b8 = infile.readlines()
            with open(b6, 'w', b7 = 'utf-8') as outfile:
                for b9 in b8:
                    b9 = b9.strip()
                    b10 = b4.fonk2(b9[:-5])
                    outfile.write(f"{b10} - {b9[-2]}\n")
if b11 = = "__main__":
    b12 = class1()
    b12.fonk2()