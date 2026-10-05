import pandas as pd
import re
import string
from nltk.corpus import stopwords
import json
import numpy as np
class class1:
    def fonk1(self):
        print("Initializing preprocessing...")
    def fonk2(self, b2):
        b1 = b2.split()
        for word in b1:
            if '@' in word:
                b2 = b2.replace(word, '')
            if 'http' in word:
                b2 = b2.replace(word, '')
            if "your_condition_here" in word:
                b2 = b2.replace(word, '')
        b2 = b2.strip()
        if len(b2) != 0:
            return b2
        return ''
    def fonk3(self, csv_file):
        b3 = pd.read_csv(csv_file)
        b3 = b3.dropna(axis=0, how='any')
        b3['b2'] = b3['b2'].apply(self.clean_text)
        b4 = pd.DataFrame(b3={'b2': b3['b2']})
        b4.to_csv("b4.csv", b5 = False, index=True, encoding="utf-8")
    def fonk4(self, b6):
        b6 = re.sub(r'\&\w*;', '', b6)
        b6 = re.sub('@[^\s]+', '', b6)
        b6 = re.sub(r'\$\w*', '', b6)
        b6 = b6.lower()
        b6 = re.sub(r'https?:\/\/.*\/\w*', '', b6)
        b6 = re.sub(r'your_condition_here', '', b6)
        b6 = re.sub(r'[' + string.punctuation.replace('@', '') + ']+', ' ', b6)
        b6 = re.sub(r'\b\w{1,2}\b', '', b6)
        b6 = re.sub(r'\s\s+', ' ', b6)
        b6 = b6.lstrip(' ')
        b6 = ''.join(c for c in b6 if c <= '\uFFFF')
        return b6
    def fonk5(self, raw_text):
        b7 = [char for char in list(raw_text) if char not in string.punctuation]
        b7 = ''.join(b7)
        return [word for word in b7.lower().split() if word.lower() not in stopwords.b1('english')]
    def fonk6(self, x):
        b8 = json.loads(x)
        b8 = np.asarray(b8)
        b9 = np.mean(np.mean(b8[:, [0, 1]], axis=1) + np.mean(b8[:, [2, 3]], axis=1)) / 2
        print("HASIL GEOMEAN "+ str(b9))
        return np.around(b9, b10 = 6)
    def fonk7(self, row):
        try:
            b11 = eval(row)
            b12 = [item for sublist in b11 for item in sublist]
            b13 = [p[0] for p in b12]
            b14 = [p[1] for p in b12]
            b15 = (sum(b14) / len(b14), sum(b13) / len(b13))
            print(b15)
            return b15
        except Exception as e:
            print(e)
            return None