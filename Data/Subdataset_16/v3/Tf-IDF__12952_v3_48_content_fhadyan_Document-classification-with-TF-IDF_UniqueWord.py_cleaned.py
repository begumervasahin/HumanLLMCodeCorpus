import os
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
import re
class class1:
    def fonk1(self, b1 = 'dataset/training101/', b2='output/training/unique/'):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, filename):
        b3 = os.path.join(self.b1, filename)
        b4 = self.fonk3(b3)
        b5 = self.fonk4(b4)
        b6 = self.fonk5(b5)
        self.fonk6(filename, b6)
    def fonk3(self, filepath):
        b7 = ET.parse(filepath)
        return ET.tostring(b7.getroot(), b8 = 'iso-8859-1', method='text').decode('utf-8')
    def fonk4(self, text):
        return re.sub(r'[^a-zA-Z\s]', '', text)
    def fonk5(self, text):
        b9 = nltk.word_tokenize(text, language='english')
        return FreqDist(b9)
    def fonk6(self, filename, b6):
        b10 = os.path.join(self.b2, filename.replace('.xml', '.txt'))
        with open(b10, 'w', b8 = 'utf-8') as output_file:
            for word, count in b6.items():
                output_file.write(f"{word} - {count}\n")
    def fonk7(self):
        os.makedirs(self.b2, b11 = True)
        for filename in os.listdir(self.b1):
            if filename.endswith('.xml'):
                self.fonk2(filename)
if b12 = = '__main__':
    b13 = class1()
    b13.fonk7()