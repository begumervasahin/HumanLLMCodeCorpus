import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(b11, b14):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b11))
    b4 = b1.get_feature_names_out()
    b5 = b3.toarray()
    with open(b14, "a+", b6 = "utf-8") as fo:
        for doc_weights in b5:
            for word, weight in zip(b4, doc_weights):
                b7 = json.dumps([word, weight], ensure_ascii=False)
                fo.write(b7 + "\n")
def fonk2(text):
    return " ".join(jieba.cut(text, b8 = True))
def fonk3(b13, b14):
    b9 = SparkContext(appName='DocumentsRewrite')
    b10 = b9.textFile(b13).map(lambda x: json.loads(x)['content'])
    b11 = b10.map(cut_words).collect()
    fonk1(b11, b14)
if b12 = = "__main__":
    b13 = '/vagrant/data/data.txt'
    b14 = '/vagrant/vocabulary/mllib.txt'
    fonk3(b13, b14)