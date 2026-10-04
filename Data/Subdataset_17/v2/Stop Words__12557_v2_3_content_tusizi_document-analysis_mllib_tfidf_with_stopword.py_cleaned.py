import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
sc = SparkContext(appName='DocumentsRewrite')
rdd = sc.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def cut(text):
    seg_list = jieba.cut(text, cut_all=True)
    return " ".join(seg_list)
corpus = rdd.map(cut).collect()
def compute_and_save_tfidf(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names_out()
    weights = tfidf.toarray()
    filename = "/vagrant/vocabulary/mllib.txt"
    with open(filename, "a+", encoding="utf-8") as fo:
        for doc_weights in weights:
            for word, weight in zip(words, doc_weights):
                record = json.dumps([word, weight], ensure_ascii=False)
                fo.write(record + "\n")
            fo.write("\n")
compute_and_save_tfidf(corpus)
sc.stop()