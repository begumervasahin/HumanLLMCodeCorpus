import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
sc = SparkContext(appName='DocumentsRewrite')
rdd = sc.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def cut(x):
    seg_list = jieba.cut(x, cut_all=True)
    return " ".join(seg_list)
corpus = rdd.map(cut).collect()
def tf_me(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names_out()
    weights = tfidf.toarray()
    filename = "/vagrant/vocabulary/mllib.txt"
    with open(filename, "a+", encoding="utf-8") as fo:
        for i in range(len(weights)):
            for j in range(len(words)):
                r = json.dumps([words[j], weights[i][j]], ensure_ascii=False)
                fo.write(r + "\n")
            fo.write("\n")
tf_me(corpus)
sc.stop()