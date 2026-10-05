
import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(b11):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b11))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    b6 = "/vagrant/vocabulary/mllib.txt"
    with open(b6, "a+") as fo:
        for i in range(len(b5)):
            for j in range(len(b4)):
                b7 = json.dumps([b4[j], b5[i][j]], ensure_ascii=False)
                fo.write(b7.encode("utf-8"))
            fo.write("\n")
b8 = SparkContext(appName='DocumentsRewrite')
b9 = b8.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def fonk2(text):
    b10 = jieba.cut(text, cut_all=True)
    return " ".join(list(b10))
b11 = b9.map(tokenize_text).collect()
fonk1(b11)
b8.stop()