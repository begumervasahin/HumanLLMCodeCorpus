import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def fonk1(cor):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b13))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    for i in range(len(b5)):
        b6 = "/vagrant/vocabulary/mllib.txt"
        for j in range(len(b4)):
            b7 = json.dumps([b4[j], b5[i][j]], ensure_ascii=False)
            b8 = open(b6, "a+")
            b8.write(b7.encode("utf-8"))
        b8.write("\n")
        b8.close()
b9 = SparkContext(appName='DocumentsRewrite')
b10 = b9.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def fonk2(x):
    b11 = jieba.fonk2(x, cut_all=True)
    b12 = []
    for value in b11:
        b12.append(value)
    return " ".join(b12)
b13 = b10.map(cut).collect()
fonk1(b13)