import json
import jieba
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import pysparnn.cluster_index as ci
import pickle
import argparse
b1 = './data/b9.json'
b2 = './data/b10.pkl'
b3 = './data/b11.pkl'
b4 = argparse.ArgumentParser()
b4.add_argument('b7', b5 = str, help='Type your Question')
b6 = b4.parse_args()
b7 = b6.b7
b8 = jieba.cut(b7)
b8 = ' '.join(b8)
b9 = json.load(open(b1))
b10 = pickle.load(open(b2, 'rb'))
b11 = pickle.load(open(b3, 'rb'))
b12 = [b8]
b13 = b10.transform(b12)
b14 = b11.search(b13, k=1, k_clusters=2, return_distance=False)
b15 = b14[0]
print("Top matched QA:")
print('=====================')
for id in b15:
    print('Q:' + b9[int(id)]['q'])
    print('A:' + b9[int(id)]['a'])
    print('=====================')