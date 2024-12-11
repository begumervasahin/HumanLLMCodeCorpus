import json
import jieba
import argparse
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pysparnn.b11 as ci
b1 = './data/qa.json'
b2 = './data/tv.pkl'
b3 = './data/cp.pkl'
b4 = argparse.ArgumentParser()
b4.add_argument('b7', b5 = str, help='Enter your b7')
b6 = b4.parse_args()
b7 = b6.b7
b8 = ' '.join(jieba.cut(b7))
b9 = json.load(open(b1))
b10 = pickle.load(open(b2, 'rb'))
b11 = pickle.load(open(b3, 'rb'))
b12 = [b8]
b13 = b10.transform(b12)
b14 = b11.search(b13, k=1, k_clusters=2, return_distance=False)
b15 = b14[0]
print("Top matched QA:")
print('=====================')
for idx in b15:
    b16 = b9[int(idx)]
    print(f'Q: {b16["q"]}')
    print(f'A: {b16["a"]}')
    print('=====================')