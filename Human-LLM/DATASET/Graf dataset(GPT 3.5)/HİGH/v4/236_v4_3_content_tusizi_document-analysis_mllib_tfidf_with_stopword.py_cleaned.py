import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(b9):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b9))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    with open("/vagrant/vocabulary/mllib.txt", "a+") as file:
        for i in range(len(b5)):
            for j in range(len(b4)):
                b6 = json.dumps([b4[j], b5[i][j]], ensure_ascii=False)
                file.write(b6.encode("utf-8"))
            file.write("\n")
b7 = SparkContext(appName='DocumentsRewrite')
b8 = b7.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def fonk2(text):
    b4 = jieba.cut(text, cut_all=True)
    return " ".join(b4)
b9 = b8.map(tokenize_text).collect()
fonk1(b9)
b7.stop()