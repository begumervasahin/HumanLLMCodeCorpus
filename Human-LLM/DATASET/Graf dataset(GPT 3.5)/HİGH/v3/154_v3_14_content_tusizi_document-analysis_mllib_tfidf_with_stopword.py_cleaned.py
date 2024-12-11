import json
import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(b10):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b10))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    b6 = "/vagrant/vocabulary/mllib.txt"
    with open(b6, "a+") as file_out:
        for doc_index, doc_weights in enumerate(b5):
            for word_index, weight in enumerate(doc_weights):
                b7 = b4[word_index]
                b8 = json.dumps([b7, weight], ensure_ascii=False)
                file_out.write(b8)
                file_out.write("\n")
if b9 = = "__main__":
    b10 = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    def fonk2(document):
        return " ".join(jieba.cut(document, b11 = True))
    b12 = list(map(tokenize_document, b10))
    fonk1(b12)