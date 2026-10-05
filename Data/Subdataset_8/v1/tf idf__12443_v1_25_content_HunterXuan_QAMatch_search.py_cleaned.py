import json
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pysparnn.cluster_index as ci
import pickle
import argparse
qa_path = './data/qa.json'
tv_path = './data/tv.pkl'
cp_path = './data/cp.pkl'
parser = argparse.ArgumentParser()
parser.add_argument('question', type=str, help='Type your Question')
args = parser.parse_args()
question = args.question
def main():
    cutted_question = jieba.cut(question)
    cutted_question = ' '.join(cutted_question)
    qa = json.load(open(qa_path))
    tv = pickle.load(open(tv_path, 'rb'))
    cp = pickle.load(open(cp_path, 'rb'))
    search_data = [cutted_question]
    search_tfidf = tv.transform(search_data)
    result_array = cp.search(search_tfidf, k=1, k_clusters=2, return_distance=False)
    result = result_array[0]
    print("Top matched QA:")
    print('=====================')
    for idx in result:
        print('Q:' + qa[int(idx)]['q'])
        print('A:' + qa[int(idx)]['a'])
        print('=====================')
if __name__ == "__main__":
    main()