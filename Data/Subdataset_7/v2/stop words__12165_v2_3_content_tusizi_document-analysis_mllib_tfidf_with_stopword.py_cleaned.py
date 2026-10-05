import json
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def fonk1(b11):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b11))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    with open("/vagrant/vocabulary/mllib.txt", "a+") as file_out:
        for doc_index, doc_weights in enumerate(b5):
            for word_index, weight in enumerate(doc_weights):
                b6 = b4[word_index]
                b7 = {"b6": b6, "tfidf_score": weight}
                b8 = json.dumps(b7, ensure_ascii=False)
                file_out.write(b8 + "\n")
def fonk2(text):
    b9 = jieba.cut(text, cut_all=True)
    return " ".join(b9)
if b10 = = "__main__":
    b11 = [
        "Your sample b11 here",
        "Another sample document"
    ]
    fonk1(b11)