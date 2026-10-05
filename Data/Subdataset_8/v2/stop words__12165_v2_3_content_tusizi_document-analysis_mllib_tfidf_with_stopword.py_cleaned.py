import json
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def compute_tfidf(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(vectorizer.fit_transform(corpus))
    feature_names = vectorizer.get_feature_names()
    weights = tfidf_matrix.toarray()
    with open("/vagrant/vocabulary/mllib.txt", "a+") as file_out:
        for doc_index, doc_weights in enumerate(weights):
            for word_index, weight in enumerate(doc_weights):
                word = feature_names[word_index]
                tfidf_info = {"word": word, "tfidf_score": weight}
                json_data = json.dumps(tfidf_info, ensure_ascii=False)
                file_out.write(json_data + "\n")
def tokenize(text):
    tokens = jieba.cut(text, cut_all=True)
    return " ".join(tokens)
if __name__ == "__main__":
    corpus = [
        "Your sample corpus here",
        "Another sample document"
    ]
    compute_tfidf(corpus)