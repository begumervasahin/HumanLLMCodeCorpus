import json
import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(b9):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b9))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    b6 = "/vagrant/vocabulary/mllib.txt"
    with open(b6, "a+") as file_out:
        for i in range(len(b5)):
            for j in range(len(b4)):
                b7 = json.dumps([b4[j], b5[i][j]], ensure_ascii=False)
                file_out.write(b7)
                file_out.write("\n")
if b8 = = "__main__":
    b9 = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    def fonk2(document):
        return " ".join(jieba.cut(document, b10 = True))
    b11 = list(map(tokenize_document, b9))
    fonk1(b11)