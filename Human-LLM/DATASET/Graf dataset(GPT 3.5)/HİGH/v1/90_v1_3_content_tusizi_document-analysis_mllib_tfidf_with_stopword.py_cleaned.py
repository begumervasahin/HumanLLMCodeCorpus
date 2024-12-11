import json
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def fonk1(b8):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b8))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    with open("/vagrant/vocabulary/mllib.txt", "a+") as fo:
        for i in range(len(b5)):
            for j in range(len(b4)):
                b6 = json.dumps([b4[j], b5[i][j]], ensure_ascii=False)
                fo.write(b6)
                fo.write("\n")
def fonk2(x):
    b4 = jieba.fonk2(x, cut_all=True)
    return " ".join(b4)
if b7 = = "__main__":
    b8 = [
        "Your sample b8 here",
        "Another sample document"
    ]
    fonk1(b8)