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
        b4 = ET.parse(b3)
        b5 = ET.tostring(b4.getroot(), encoding='iso-8859-1', method='text').decode("utf-8")
        b6 = self.fonk4(b5)
        b7 = self.fonk5(b6)
        self.fonk6(filename, b7)
    def fonk4(self, text):
        b8 = re.compile('[^a-zA-Z\s]')
        return b8.sub('', text)
    def fonk5(self, text):
        b9 = nltk.word_tokenize(text, language='english')
        return FreqDist(b9)
    def fonk6(self, filename, b7):
        b10 = os.path.join(self.b2, filename[:-4] + ".txt")
        with open(b10, "wb+") as output_file:
            for word, frequency in b7.items():
                output_file.write(bytes(f"{word} - {frequency}\n", "utf-8"))
if b11 = = "__main__":
    b12 = class1()
    b12.fonk2()