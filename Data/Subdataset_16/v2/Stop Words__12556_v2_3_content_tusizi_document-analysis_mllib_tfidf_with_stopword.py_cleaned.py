import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
b1 = SparkContext(appName='DocumentsRewrite')
b2 = b1.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def fonk1(text):
    b3 = jieba.fonk1(text, cut_all=True)
    return " ".join(b3)
b4 = b2.map(cut).collect()
def fonk2(b4):
    b5 = CountVectorizer()
    b6 = TfidfTransformer()
    b7 = b6.fit_transform(b5.fit_transform(b4))
    b8 = b5.get_feature_names_out()
    b9 = b7.toarray()
    b10 = "/vagrant/vocabulary/mllib.txt"
    with open(b10, "a+", b11 = "utf-8") as fo:
        for doc_weights in b9:
            for word, weight in zip(b8, doc_weights):
                b12 = json.dumps([word, weight], ensure_ascii=False)
                fo.write(b12 + "\n")
            fo.write("\n")
fonk2(b4)
b1.stop()