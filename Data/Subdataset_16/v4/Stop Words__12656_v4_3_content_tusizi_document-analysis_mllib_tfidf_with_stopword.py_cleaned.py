import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(b12):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b12))
    b4 = b1.get_feature_names_out()
    b5 = b3.toarray()
    b6 = "/vagrant/vocabulary/mllib.txt"
    with open(b6, "a+", b7 = "utf-8") as fo:
        for i in range(len(b5)):
            for j in range(len(b4)):
                b8 = json.dumps([b4[j], b5[i][j]], ensure_ascii=False)
                fo.write(b8 + "\n")
def fonk2(text):
    b4 = jieba.cut(text, cut_all=True)
    return " ".join(b4)
if b9 = = "__main__":
    b10 = SparkContext(appName='DocumentsRewrite')
    b11 = b10.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
    b12 = b11.map(cut_words).collect()
    fonk1(b12)