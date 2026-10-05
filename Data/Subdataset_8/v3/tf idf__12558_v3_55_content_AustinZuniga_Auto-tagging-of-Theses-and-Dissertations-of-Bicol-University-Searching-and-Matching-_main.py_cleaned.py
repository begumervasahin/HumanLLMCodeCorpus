import gensim
import glob
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from rake_nltk import Rake
rake = Rake()
def read_raw_documents(file_list):
    raw_documents = []
    for file_path in file_list:
        with open(file_path) as file_input:
            raw_documents.append(file_input.read())
    return raw_documents
def tokenize_documents(raw_documents):
    tokenized_documents = [[word.lower() for word in word_tokenize(text)] for text in raw_documents]
    return tokenized_documents
def create_dictionary(tokenized_documents):
    dictionary = gensim.corpora.Dictionary(tokenized_documents)
    return dictionary
def create_corpus(dictionary, tokenized_documents):
    corpus = [dictionary.doc2bow(tokenized_doc) for tokenized_doc in tokenized_documents]
    return corpus
def create_tfidf_model(corpus):
    tfidf_model = gensim.models.TfidfModel(corpus)
    return tfidf_model
def calculate_similarity_matrix(corpus, tfidf_model, dictionary):
    similarity_matrix = gensim.similarities.Similarity('/var/www/html/Auto-tagging-of-Theses-and-Dissertations-of-Bicol-University-Searching-and-Matching-/result/result',
                                                       tfidf_model[corpus], num_features=len(dictionary))
    return similarity_matrix
def preprocess_query_document(query):
    return [word.lower() for word in word_tokenize(query)]
def calculate_query_tfidf(dictionary, tfidf_model, query_document):
    query_document_bow = dictionary.doc2bow(query_document)
    return tfidf_model[query_document_bow]
def main():
    file_list = glob.glob(os.path.join(os.getcwd(), "data/", "*.txt"))
    raw_documents = read_raw_documents(file_list)
    tokenized_documents = tokenize_documents(raw_documents)
    dictionary = create_dictionary(tokenized_documents)
    corpus = create_corpus(dictionary, tokenized_documents)
    tfidf_model = create_tfidf_model(corpus)
    similarity_matrix = calculate_similarity_matrix(corpus, tfidf_model, dictionary)
    query_document = preprocess_query_document("I'm taking the show on the road.")
    query_document_tfidf = calculate_query_tfidf(dictionary, tfidf_model, query_document)
    similarities = similarity_matrix[query_document_tfidf]
    print(similarities)
if __name__ == "__main__":
    main()