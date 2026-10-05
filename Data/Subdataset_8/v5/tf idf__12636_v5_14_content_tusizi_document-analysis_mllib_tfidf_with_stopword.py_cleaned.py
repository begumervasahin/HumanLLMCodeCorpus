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
    output_file = "/vagrant/vocabulary/mllib.txt"
    with open(output_file, "a+") as file:
        for doc_index, doc_weights in enumerate(weights):
            for word_index, weight in enumerate(doc_weights):
                word_weight_json = json.dumps([words[word_index], weight], ensure_ascii=False)
                file.write(word_weight_json.encode("utf-8"))
            file.write("\n")
sc = SparkContext(appName='DocumentsRewrite')
data_file = '/vagrant/data/data.txt'
rdd = sc.textFile(data_file).map(lambda x: json.loads(x)['content'])
def tokenize_text(text):
    tokens = jieba.cut(text, cut_all=True)
    return " ".join(tokens)
corpus = rdd.map(tokenize_text).collect()
calculate_tfidf(corpus)
sc.stop()