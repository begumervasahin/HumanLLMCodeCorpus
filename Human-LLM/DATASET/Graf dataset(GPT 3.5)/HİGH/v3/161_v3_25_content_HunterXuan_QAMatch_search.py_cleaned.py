import json
import argparse
import pickle
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
import pysparnn.b14 as ci
b1 = './data/qa.json'
b2 = './data/tv.pkl'
b3 = './data/cp.pkl'
def fonk1(file_path):
    with open(file_path, 'r', b4 = 'utf-8') as file:
        return json.load(file)
def fonk2(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
def fonk3(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
def fonk4(b11):
    b5 = jieba.cut(b11)
    return ' '.join(b5)
def fonk5(b16, b14, b12):
    b6 = b14.search(b16, k=1, k_clusters=2, return_distance=False)
    b7 = b6[0]
    return [b12[int(idx)] for idx in b7]
def fonk6():
    b8 = argparse.ArgumentParser()
    b8.add_argument('b11', b9 = str, help='Enter your b11')
    b10 = b8.parse_args()
    b11 = b10.b11
    b12 = fonk1(b1)
    b13 = fonk2(b2)
    b14 = fonk3(b3)
    b15 = fonk4(b11)
    b16 = b13.transform([b15])
    b17 = fonk5(b16, b14, b12)
    print("Top matched QA:")
    print('=====================')
    for match in b17:
        print(f"Q: {match['q']}")
        print(f"A: {match['a']}")
        print('=====================')
if b18 = = "__main__":
    fonk6()