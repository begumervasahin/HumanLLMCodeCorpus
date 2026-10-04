import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
sc = SparkContext(appName='DocumentsRewrite')
rdd = sc.textFile('/vagrant/data/data.txt').map(lambda x: json.loads(x)['content'])
def segment_text(text):
    seg_list = jieba.cut(text, cut_all=True)
    return " ".join(seg_list)
corpus = rdd.map(segment_text).collect()
def compute_and_save_tfidf(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names_out()
    weights = tfidf_matrix.toarray()
    output_file = "/vagrant/vocabulary/mllib.txt"
    with open(output_file, "a+", encoding="utf-8") as file:
        for doc_weights in weights:
            for word, weight in zip(words, doc_weights):
                record = json.dumps([word, weight], ensure_ascii=False)
                file.write(record + "\n")
            file.write("\n")
compute_and_save_tfidf(corpus)
sc.stop()