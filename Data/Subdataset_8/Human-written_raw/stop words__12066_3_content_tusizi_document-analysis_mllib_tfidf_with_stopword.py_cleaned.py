import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def tf_me(cor):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    for i in range(len(weight)):
        filename = "/vagrant/vocabulary/mllib.txt"
        for j in range(len(word)):
            r = json.dumps([word[j], weight[i][j]], ensure_ascii=False)
            fo = open(filename, "a+")
            fo.write(r.encode("utf-8"))
        fo.write("\n")
        fo.close()
sc = SparkContext(appName='DocumentsRewrite')
rdd = sc.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def cut(x):
    list = jieba.cut(x, cut_all=True)
    result = []
    for value in list:
        result.append(value)
    return " ".join(result)
corpus = rdd.map(cut).collect()
tf_me(corpus)