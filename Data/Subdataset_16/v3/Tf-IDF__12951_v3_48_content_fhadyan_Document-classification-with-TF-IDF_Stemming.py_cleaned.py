import os
from nltk.stem import PorterStemmer
from UniqueWord import UniqueWord
class class1:
    def fonk1(self, b1 = "output/training/stopword/", b2="output/training/stem/"):
        self.b1 = b1
        self.b2 = b2
        self.fonk2()
    def fonk2(self):
        if not os.listdir(self.b1):
            b3 = UniqueWord()
            b3.output()
    def fonk3(self, b9, b10):
        b4 = PorterStemmer()
        with open(b9, 'r', b5 = 'utf-8') as infile:
            b6 = infile.readlines()
        with open(b10, 'w', b5 = 'utf-8') as outfile:
            for b7 in b6:
                b7 = b7.strip()
                if len(b7) > 5:
                    b8 = b4.fonk4(b7[:-5])
                    outfile.write(f"{b8} - {b7[-2]}\n")
    def fonk4(self):
        for filename in os.listdir(self.b1):
            if filename.endswith('.txt'):
                b9 = os.path.join(self.b1, filename)
                b10 = os.path.join(self.b2, filename)
                self.fonk3(b9, b10)
if b11 = = "__main__":
    b12 = class1()
    b12.fonk4()