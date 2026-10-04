import os
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
import re
class class1:
    def fonk1(self, b1 = 'dataset/training101/', b2='output/training/unique/'):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        for filename in os.listdir(self.b1):
            if filename.endswith('.xml'):
                self.fonk3(filename)
    def fonk3(self, filename):
        b3 = os.path.join(self.b1, filename)
        b4 = self.fonk4(b3)
        b5 = self.fonk5(b4)
        b6 = self.fonk6(b5)
        self.fonk7(filename, b6)
    def fonk4(self, filepath):
        b7 = ET.parse(filepath)
        return ET.tostring(b7.getroot(), b8 = 'iso-8859-1', method='text').decode("utf-8")
    def fonk5(self, text):
        b9 = re.compile('[^a-zA-Z\s]')
        return b9.sub('', text)
    def fonk6(self, text):
        b10 = nltk.word_tokenize(text, language='english')
        return FreqDist(b10)
    def fonk7(self, filename, b6):
        b11 = os.path.join(self.b2, filename[:-4] + ".txt")
        with open(b11, "wb+") as output_file:
            for word, frequency in b6.items():
                output_file.write(bytes(f"{word} - {frequency}\n", "utf-8"))
if b12 = = "__main__":
    b13 = class1()
    b13.fonk2()