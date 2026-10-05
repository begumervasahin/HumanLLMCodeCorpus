import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def calculate_tfidf(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names()
    weights = tfidf_matrix.toarray()
    with open("/vagrant/vocabulary/mllib.txt", "a+") as file:
        for i in range(len(weights)):
            for j in range(len(words)):
                word_weight_pair = json.dumps([words[j], weights[i][j]], ensure_ascii=False)
                file.write(word_weight_pair.encode("utf-8"))
            file.write("\n")
sc = SparkContext(appName='DocumentsRewrite')
rdd = sc.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def tokenize_text(text):
    words = jieba.cut(text, cut_all=True)
    return " ".join(words)
corpus = rdd.map(tokenize_text).collect()
calculate_tfidf(corpus)
sc.stop()