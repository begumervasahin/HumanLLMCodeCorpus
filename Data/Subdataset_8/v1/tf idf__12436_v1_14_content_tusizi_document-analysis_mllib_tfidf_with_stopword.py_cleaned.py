import json
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def tf_me(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names()
    weights = tfidf.toarray()
    filename = "/vagrant/vocabulary/mllib.txt"
    with open(filename, "a+") as fo:
        for i in range(len(weights)):
            for j in range(len(words)):
                data = json.dumps([words[j], weights[i][j]], ensure_ascii=False)
                fo.write(data)
                fo.write("\n")
if __name__ == "__main__":
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    def cut(x):
        return " ".join(jieba.cut(x, cut_all=True))
    corpus = list(map(cut, corpus))
    tf_me(corpus)