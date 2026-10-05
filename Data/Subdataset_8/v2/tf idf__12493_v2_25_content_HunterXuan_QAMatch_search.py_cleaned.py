import json
import jieba
import argparse
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pysparnn.cluster_index as ci
qa_path = './data/qa.json'
tv_path = './data/tv.pkl'
cp_path = './data/cp.pkl'
parser = argparse.ArgumentParser()
parser.add_argument('question', type=str, help='Enter your question')
args = parser.parse_args()
question = args.question
def main():
    tokenized_question = jieba.cut(question)
    tokenized_question = ' '.join(tokenized_question)
    qa_data = json.load(open(qa_path))
    tfidf_vectorizer = pickle.load(open(tv_path, 'rb'))
    cluster_index = pickle.load(open(cp_path, 'rb'))
    question_tfidf = tfidf_vectorizer.transform([tokenized_question])
    result_array = cluster_index.search(question_tfidf, k=1, k_clusters=2, return_distance=False)
    top_match_indices = result_array[0]
    print("Top matched QA:")
    print('=====================')
    for idx in top_match_indices:
        print('Q:' + qa_data[int(idx)]['q'])
        print('A:' + qa_data[int(idx)]['a'])
        print('=====================')
if __name__ == "__main__":
    main()