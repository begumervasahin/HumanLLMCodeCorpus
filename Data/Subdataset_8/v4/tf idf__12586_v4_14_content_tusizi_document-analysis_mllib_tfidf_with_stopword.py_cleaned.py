
import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def calculate_tfidf(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names()
    weights = tfidf.toarray()
    filename = "/vagrant/vocabulary/mllib.txt"
    with open(filename, "a+") as fo:
        for i in range(len(weights)):
            for j in range(len(words)):
                json_data = json.dumps([words[j], weights[i][j]], ensure_ascii=False)
                fo.write(json_data.encode("utf-8"))
            fo.write("\n")
sc = SparkContext(appName='DocumentsRewrite')
rdd = sc.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def tokenize_text(text):
    tokens = jieba.cut(text, cut_all=True)
    return " ".join(list(tokens))
corpus = rdd.map(tokenize_text).collect()
calculate_tfidf(corpus)
sc.stop()