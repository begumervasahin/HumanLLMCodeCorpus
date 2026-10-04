import os
from nltk.stem.porter import PorterStemmer
from UniqueWord import UniqueWord
class class1:
    def fonk1(self):
        self.b1 = "output/training/stopword/"
        self.b2 = "output/training/stem/"
        self.fonk2()
    def fonk2(self):
        if not os.listdir(self.b1):
            b3 = UniqueWord()
            b3.output()
    def fonk3(self):
        b4 = PorterStemmer()
        for filename in os.listdir(self.b1):
            if not filename.endswith('.txt'):
                continue
            self.fonk4(b4, filename)
    def fonk4(self, b4, filename):
        b5 = os.path.join(self.b1, filename)
        b6 = os.path.join(self.b2, filename)
        with open(b5, 'r') as source_file, open(b6, 'wb') as output_file:
            b7 = source_file.readlines()
            for line in b7:
                b8 = b4.stem(line[:-5])
                b9 = f"{b8} - {line[-2]}\n"
                output_file.write(b9.encode('utf-8'))
if b10 = = "__main__":
    b11 = class1()
    b11.fonk3()