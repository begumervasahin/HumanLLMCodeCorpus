import math
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
def tokenise_normalise(raw_string):
    tokenizer = RegexpTokenizer(r'\w+')
    tokenised_text = tokenizer.tokenize(str(raw_string))
    token_normalise = [w.lower() for w in tokenised_text]
    return token_normalise
def stem(token_normalised_text):
    stemmer = PorterStemmer()
    processed_text = [stemmer.stem(w) for w in token_normalised_text]
    return processed_text
def create_tf_dict_doc(processed_text, doc_id, stats_dict):
    for root in processed_text:
        if root not in stats_dict:
            stats_dict[root] = {}
        if doc_id not in stats_dict[root]:
            stats_dict[root][doc_id] = 0
        stats_dict[root][doc_id] += 1
    return stats_dict
def create_tf_dict_query(processed_query):
    query_dict = {}
    for root in processed_query:
        if root not in query_dict:
            query_dict[root] = 0
        query_dict[root] += 1
    return query_dict
def find_tfidf_doc(stats_dict, number_of_docs):
    idf_dict = {word: len(stats_dict[word]) for word in stats_dict}
    for word in stats_dict:
        for doc in stats_dict[word]:
            tf = 1 + math.log(stats_dict[word][doc])
            idf = math.log(number_of_docs / idf_dict[word])
            stats_dict[word][doc] = tf * idf
    return stats_dict, idf_dict
def find_tfidf_query(query_dict, idf_dict, number_of_docs):
    for word in query_dict:
        tf = 1 + math.log(query_dict[word])
        idf = math.log(number_of_docs / idf_dict.get(word, number_of_docs))
        query_dict[word] = tf * idf
    return query_dict
if __name__ == "__main__":
    docs = ["The quick brown fox jumps over the lazy dog.", "The dog barks at the fox."]
    number_of_docs = len(docs)
    stats_dict = {}
    for i, doc in enumerate(docs):
        tokenized = tokenise_normalise(doc)
        stemmed = stem(tokenized)
        stats_dict = create_tf_dict_doc(stemmed, f"doc_{i}", stats_dict)
    stats_dict, idf_dict = find_tfidf_doc(stats_dict, number_of_docs)
    query = "quick fox"
    tokenized_query = tokenise_normalise(query)
    stemmed_query = stem(tokenized_query)
    query_dict = create_tf_dict_query(stemmed_query)
    query_tfidf = find_tfidf_query(query_dict, idf_dict, number_of_docs)
    print("TF-IDF for Documents:", stats_dict)
    print("TF-IDF for Query:", query_tfidf)