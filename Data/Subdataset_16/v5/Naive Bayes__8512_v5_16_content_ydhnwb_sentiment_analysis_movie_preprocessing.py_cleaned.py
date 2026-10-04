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
            if '@' in word or 'http' in word or '\"' in word:
                print(f"Removing {word}")
                b2 = b2.replace(word, '')
        return b2.strip()
    def fonk3(self, csv_file):
        b3 = pd.read_csv(csv_file).dropna()
        b3['b2'] = b3['b2'].apply(self.clean_text)
        b4 = pd.DataFrame({'b2': b3['b2']})
        b4.to_csv("b4.csv", b5 = False, index=True, encoding="utf-8")
    def fonk4(self, b6):
        b6 = re.sub(r'\&\w*;', '', b6)
        b6 = re.sub(r'@[^\s]+', '', b6)
        b6 = re.sub(r'\$\w*', '', b6)
        b6 = b6.lower()
        b6 = re.sub(r'https?:\/\/.*\/\w*', '', b6)
        b6 = re.sub(r'[' + string.punctuation.replace('@', '') + ']+', ' ', b6)
        b6 = re.sub(r'\b\w{1,2}\b', '', b6)
        b6 = re.sub(r'\s\s+', ' ', b6)
        b6 = b6.lstrip(' ')
        b6 = ''.join(c for c in b6 if c <= '\uFFFF')
        return b6
    def fonk5(self, raw_text):
        b7 = ''.join([char for char in raw_text if char not in string.punctuation])
        b1 = [word for word in b7.lower().split() if word.lower() not in stopwords.b1('english')]
        return b1
    def fonk6(self, x):
        b8 = np.asarray(json.loads(x))
        b9 = np.mean(b8[:, 0:2], axis=1).mean()
        b9 = np.around(b9, decimals=6)
        print("Geometric mean:", b9)
        return b9
    def fonk7(self, row):
        try:
            b8 = eval(row)
            b10 = [coord[0] for coord in b8]
            b11 = [coord[1] for coord in b8]
            b12 = (np.mean(b11), np.mean(b10))
            print("Centroid:", b12)
            return b12
        except Exception as e:
            print("Error:", e)
            return None
