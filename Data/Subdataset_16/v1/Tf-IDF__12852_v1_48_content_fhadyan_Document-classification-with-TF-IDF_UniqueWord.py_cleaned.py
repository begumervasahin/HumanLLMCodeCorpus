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
        b4 = ET.parse(b3)
        b5 = ET.tostring(b4.getroot(), b10='iso-8859-1', method='text').decode('utf-8')
        b6 = re.sub(r'[^a-zA-Z\s]', '', b5)
        b7 = nltk.word_tokenize(b6, language='english')
        b8 = FreqDist(b7)
        b9 = os.path.join(self.b2, filename.replace('.xml', '.txt'))
        with open(b9, 'w', b10 = 'utf-8') as output_file:
            for word, count in b8.items():
                output_file.write(f"{word} - {count}\n")
    def fonk3(self):
        os.makedirs(self.b2, b11 = True)
        for filename in os.listdir(self.b1):
            if filename.endswith('.xml'):
                self.fonk2(filename)
if b12 = = '__main__':
    b13 = class1()
    b13.fonk3()