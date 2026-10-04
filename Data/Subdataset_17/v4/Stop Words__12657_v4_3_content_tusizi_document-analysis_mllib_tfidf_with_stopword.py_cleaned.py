import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def compute_tfidf(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names_out()
    weights = tfidf_matrix.toarray()
    filename = "/vagrant/vocabulary/mllib.txt"
    with open(filename, "a+", encoding="utf-8") as fo:
        for i in range(len(weights)):
            for j in range(len(words)):
                record = json.dumps([words[j], weights[i][j]], ensure_ascii=False)
                fo.write(record + "\n")
def cut_words(text):
    words = jieba.cut(text, cut_all=True)
    return " ".join(words)
if __name__ == "__main__":
    sc = SparkContext(appName='DocumentsRewrite')
    rdd = sc.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
    corpus = rdd.map(cut_words).collect()
    compute_tfidf(corpus)