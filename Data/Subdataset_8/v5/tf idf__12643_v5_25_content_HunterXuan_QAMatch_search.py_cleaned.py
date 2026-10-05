import json
import jieba
import argparse
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pysparnn.cluster_index as ci
QA_PATH = './data/qa.json'
TV_PATH = './data/tv.pkl'
CP_PATH = './data/cp.pkl'
parser = argparse.ArgumentParser()
parser.add_argument('question', type=str, help='Enter your question')
args = parser.parse_args()
question = args.question
cutted_question = ' '.join(jieba.cut(question))
qa_data = json.load(open(QA_PATH))
tfidf_vectorizer = pickle.load(open(TV_PATH, 'rb'))
cluster_index = pickle.load(open(CP_PATH, 'rb'))
search_data = [cutted_question]
search_tfidf = tfidf_vectorizer.transform(search_data)
result_array = cluster_index.search(search_tfidf, k=1, k_clusters=2, return_distance=False)
result = result_array[0]
print("Top matched QA:")
print('=====================')
for idx in result:
    qa_pair = qa_data[int(idx)]
    print(f'Q: {qa_pair["q"]}')
    print(f'A: {qa_pair["a"]}')
    print('=====================')