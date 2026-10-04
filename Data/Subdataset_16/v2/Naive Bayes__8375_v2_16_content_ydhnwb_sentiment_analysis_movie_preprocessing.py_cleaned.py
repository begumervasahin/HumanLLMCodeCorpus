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
                print(f"Removing {word}")
                b2 = b2.replace(word, '')
            if 'http' in word:
                b2 = b2.replace(word, '')
            if '\"' in word:
                b2 = b2.replace(word, '')
        b2 = b2.strip()
        return b2 if b2 else ''
    def fonk3(self, csv_file):
        b3 = pd.read_csv(csv_file)
        b3.dropna(b4 = True)
        b3['b2'] = b3['b2'].apply(self.clean_text)
        b5 = pd.DataFrame({'b2': b3['b2']})
        b5.to_csv("b5.csv", b6 = False, index=True, encoding="utf-8")
    def fonk4(self, b7):
        b7 = re.sub(r'&\w*;', '', b7)
        b7 = re.sub(r'@[^\s]+', '', b7)
        b7 = re.sub(r'\$\w*', '', b7)
        b7 = b7.lower()
        b7 = re.sub(r'https?:\/\/.*\/\w*', '', b7)
        b7 = re.sub(r'\"', '', b7)
        b7 = re.sub(r'[' + string.punctuation.replace('@', '') + ']+', ' ', b7)
        b7 = re.sub(r'\b\w{1,2}\b', '', b7)
        b7 = re.sub(r'\s\s+', ' ', b7)
        b7 = b7.lstrip()
        b7 = ''.join(c for c in b7 if c <= '\uFFFF')
        return b7
    def fonk5(self, raw_text):
        b8 = ''.join([char for char in raw_text if char not in string.punctuation])
        return [word for word in b8.lower().split() if word not in stopwords.b1('english')]
    def fonk6(self, x):
        try:
            b9 = np.asarray(json.loads(x))
            b10 = np.mean([np.mean(b9[:, 0]), np.mean(b9[:, 2])])
            print(f"Geometric mean: {b10}")
            return np.around(b10, b11 = 6)
        except Exception as e:
            print(f"Error in geo_mean: {e}")
            return None
    def fonk7(self, row):
        try:
            b9 = eval(row)
            b12 = [item for sublist in b9 for item in sublist]
            b13 = [p[0] for p in b12]
            b14 = [p[1] for p in b12]
            b15 = (sum(b14) / len(b14), sum(b13) / len(b13))
            print(f"Centroid: {b15}")
            return b15
        except Exception as e:
            print(f"Error in find_centroid: {e}")
            return None
