import gensim
import glob
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim import similarities
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
total_tokens = sum(len(doc) for doc in corpus)
similarity_index = similarities.Similarity(
    '/var/www/html/Auto-tagging-of-Theses-and-Dissertations-of-Bicol-University-Searching-and-Matching-/result/result',
    tfidf_model[corpus],
    num_features=len(dictionary)
)
query_doc = [word.lower() for word in word_tokenize("I'm taking the show on the road.")]
query_doc_bow = dictionary.doc2bow(query_doc)
query_doc_tfidf = tfidf_model[query_doc_bow]
similarity_scores = similarity_index[query_doc_tfidf]
print(similarity_scores)