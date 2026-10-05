import gensim
import glob
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from rake_nltk import Rake
rake = Rake()
file_list = glob.glob(os.path.join(os.getcwd(), "data/", "*.txt"))
raw_documents = []
for file_path in file_list:
    with open(file_path) as file_input:
        raw_documents.append(file_input.read())
tokenized_documents = [[word.lower() for word in word_tokenize(text)] for text in raw_documents]
dictionary = gensim.corpora.Dictionary(tokenized_documents)
corpus = [dictionary.doc2bow(tokenized_doc) for tokenized_doc in tokenized_documents]
tfidf_model = gensim.models.TfidfModel(corpus)
total_documents = sum(len(doc) for doc in corpus)
similarity_matrix = gensim.similarities.Similarity('/var/www/html/Auto-tagging-of-Theses-and-Dissertations-of-Bicol-University-Searching-and-Matching-/result/result',
                                                   tfidf_model[corpus], num_features=len(dictionary))
query_document = [word.lower() for word in word_tokenize("I'm taking the show on the road.")]
query_document_bow = dictionary.doc2bow(query_document)
query_document_tfidf = tfidf_model[query_document_bow]
similarities = similarity_matrix[query_document_tfidf]
print(similarities)