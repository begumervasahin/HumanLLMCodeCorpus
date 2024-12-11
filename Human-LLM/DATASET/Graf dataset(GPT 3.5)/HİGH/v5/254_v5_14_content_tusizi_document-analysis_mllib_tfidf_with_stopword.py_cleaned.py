import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(b12):
    b1 = CountVectorizer()
    b2 = TfidfTransformer()
    b3 = b2.fit_transform(b1.fit_transform(b12))
    b4 = b1.get_feature_names()
    b5 = b3.toarray()
    b6 = "/vagrant/vocabulary/mllib.txt"
    with open(b6, "a+") as file:
        for doc_index, doc_weights in enumerate(b5):
            for word_index, weight in enumerate(doc_weights):
                b7 = json.dumps([b4[word_index], weight], ensure_ascii=False)
                file.write(b7.encode("utf-8"))
            file.write("\n")
b8 = SparkContext(appName='DocumentsRewrite')
b9 = '/vagrant/data/data.txt'
b10 = b8.textFile(b9).map(lambda x: json.loads(x)['content'])
def fonk2(text):
    b11 = jieba.cut(text, cut_all=True)
    return " ".join(b11)
b12 = b10.map(tokenize_text).collect()
fonk1(b12)
b8.stop()