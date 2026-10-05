import json
import argparse
import pickle
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
import pysparnn.cluster_index as ci
QA_DATA_PATH = './data/qa.json'
TFIDF_MODEL_PATH = './data/tv.pkl'
CLUSTER_INDEX_PATH = './data/cp.pkl'
def load_qa_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
def load_tfidf_model(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
def load_cluster_index(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
def tokenize_question(question):
    tokens = jieba.cut(question)
    return ' '.join(tokens)
def search_answer(question_tfidf, cluster_index, qa_data):
    result_array = cluster_index.search(question_tfidf, k=1, k_clusters=2, return_distance=False)
    top_match_indices = result_array[0]
    return [qa_data[int(idx)] for idx in top_match_indices]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('question', type=str, help='Enter your question')
    args = parser.parse_args()
    question = args.question
    qa_data = load_qa_data(QA_DATA_PATH)
    tfidf_vectorizer = load_tfidf_model(TFIDF_MODEL_PATH)
    cluster_index = load_cluster_index(CLUSTER_INDEX_PATH)
    tokenized_question = tokenize_question(question)
    question_tfidf = tfidf_vectorizer.transform([tokenized_question])
    top_matches = search_answer(question_tfidf, cluster_index, qa_data)
    print("Top matched QA:")
    print('=====================')
    for match in top_matches:
        print(f"Q: {match['q']}")
        print(f"A: {match['a']}")
        print('=====================')
if __name__ == "__main__":
    main()