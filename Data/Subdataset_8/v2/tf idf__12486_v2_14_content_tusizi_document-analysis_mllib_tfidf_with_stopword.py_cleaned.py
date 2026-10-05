import json
import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def compute_tfidf(corpus):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names()
    weights = tfidf_matrix.toarray()
    output_file = "/vagrant/vocabulary/mllib.txt"
    with open(output_file, "a+") as file_out:
        for i in range(len(weights)):
            for j in range(len(words)):
                data = json.dumps([words[j], weights[i][j]], ensure_ascii=False)
                file_out.write(data)
                file_out.write("\n")
if __name__ == "__main__":
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    def tokenize_document(document):
        return " ".join(jieba.cut(document, cut_all=True))
    corpus_tokenized = list(map(tokenize_document, corpus))
    compute_tfidf(corpus_tokenized)