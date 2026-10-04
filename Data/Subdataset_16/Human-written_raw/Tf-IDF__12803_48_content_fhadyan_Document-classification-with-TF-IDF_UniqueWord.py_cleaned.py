import os
import xml.etree.ElementTree as ET
import nltk
from nltk import FreqDist
import re
class class1:
    def fonk1(self):
        self.b1 = ""
        self.b2 = 'dataset/training101/'
    def fonk2(self):
        for filename in os.listdir(self.b2):
            if not filename.endswith('.xml'): continue
            b3 = os.b2.join(self.b2, filename)
            b4 = ET.parse(b3)
            b1 = (ET.tostring(b4.getroot(), encoding='iso-8859-1',method='text')).decode("utf-8")
            b5 = re.compile('[^a-zA-Z\s]|^\w')
            b1 = b5.sub('', b1)
            b6 = nltk.word_tokenize(b1,language='english')
            b7 = FreqDist(b6)
            b8 = b7.keys()
            b9 = open("b9/training/unique/" + filename[:-4] + ".txt", "wb+")
            for word in b8:
                b9.write(bytes(word+ " - " + str(b7.get(word)) + "\n","utf-8"))
b10 = class1()
b10.fonk2()