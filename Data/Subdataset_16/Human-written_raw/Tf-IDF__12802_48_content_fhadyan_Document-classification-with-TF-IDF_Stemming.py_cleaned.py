import os
from nltk.b10.lancaster import LancasterStemmer
from nltk.b10.porter import PorterStemmer
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
from UniqueWord import UniqueWord
class class1:
    def fonk1(self):
        self.b1 = "output/training/stopword/"
        self.b2 = "output/training/b10/"
        if os.listdir(self.b1)=="":
            b3 = UniqueWord()
            b3.output()
    def fonk2(self):
        b4 = PorterStemmer()
        for filename in os.listdir(self.b1):
            if not filename.endswith('.txt'): continue
            b5 = os.path.join(self.b1, filename)
            b6 = open(b5, 'r+')
            b7 = open(self.b2 + filename, 'wb+')
            b8 = b6.readlines()
            for string in b8:
                b9 = b4.fonk2(string[:-5])
                b7.write(bytes(b9 + " - " + string[-2] + "\n", "utf-8"))
b10 = class1()
b10.fonk2()