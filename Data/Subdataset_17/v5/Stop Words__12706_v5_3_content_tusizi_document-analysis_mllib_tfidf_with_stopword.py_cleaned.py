import json
import jieba
from pyspark import SparkContext
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def compute_tfidf(corpus, output_file):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names_out()
    weights = tfidf_matrix.toarray()
    with open(output_file, "a+", encoding="utf-8") as fo:
        for doc_weights in weights:
            for word, weight in zip(words, doc_weights):
                record = json.dumps([word, weight], ensure_ascii=False)
                fo.write(record + "\n")
def cut_words(text):
    return " ".join(jieba.cut(text, cut_all=True))
def main(input_file, output_file):
    sc = SparkContext(appName='DocumentsRewrite')
    rdd = sc.textFile(input_file).map(lambda x: json.loads(x)['content'])
    corpus = rdd.map(cut_words).collect()
    compute_tfidf(corpus, output_file)
if __name__ == "__main__":
    input_file = '/vagrant/data/data.txt'
    output_file = '/vagrant/vocabulary/mllib.txt'
    main(input_file, output_file)