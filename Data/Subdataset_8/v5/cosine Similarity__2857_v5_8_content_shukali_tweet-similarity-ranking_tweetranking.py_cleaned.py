import numpy as np
import pandas as pd
from numpy.linalg import norm
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
NUM_TWEETS_TO_READ = 5000
def cosine_similarity(vector1, vector2):
    return np.inner(vector1, vector2) / (norm(vector1) * norm(vector2)) if norm(vector1) != 0.0 and norm(vector2) != 0.0 else 0.0
def create_term_document_matrix(docs, doc_ids=None):
    vectorizer = CountVectorizer(lowercase=True, stop_words=None)
    term_doc_matrix = vectorizer.fit_transform(docs)
    term_doc_features = vectorizer.get_feature_names()
    df = pd.DataFrame(term_doc_matrix.toarray(), columns=term_doc_features, dtype="float64")
    if doc_ids is not None:
        df.index = doc_ids
    return df
porter_stemmer = PorterStemmer()
tweets = []
tweet_ids = []
with open("data/tweets.csv", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i >= NUM_TWEETS_TO_READ:
            break
        parts = line.split("\t")
        tweet_id = parts[1]
        tweet_text = " ".join(parts[3:])
        tokenized_text = word_tokenize(tweet_text)
        stemmed_text = [porter_stemmer.stem(word) for word in tokenized_text]
        processed_tweet = " ".join(stemmed_text)
        tweets.append(processed_tweet)
        tweet_ids.append(tweet_id)
term_doc_matrix = create_term_document_matrix(tweets, tweet_ids)
document_frequencies = term_doc_matrix.apply(lambda column: column[column > 0].count(), axis=0)
tf_idf = term_doc_matrix.applymap(lambda x: 1.0 + np.log10(x) if x > 0.0 else 0.0)
idf = np.log10(len(tweets) / document_frequencies)
tf_idf = tf_idf.multiply(idf)
def calculate_cosine_similarity(tweet1, tweet2):
    id1 = tweet_ids[tweets.index(tweet1)]
    id2 = tweet_ids[tweets.index(tweet2)]
    return cosine_similarity(tf_idf.loc[[id1]], tf_idf.loc[[id2]])
def print_top_similar_tweets(tweet_id='965706998946893824', n=10):
    similarity_scores = tf_idf.apply(lambda row: cosine_similarity(tf_idf.loc[[tweet_id]], row), axis='columns').sort_values(ascending=False)
    print("Query: " + tweets[tweet_ids.index(tweet_id)] + "\n")
    for i in range(n):
        print("{}: ".format(i+1) + tweets[tweet_ids.index(similarity_scores.index[i])] + "\n")
print_top_similar_tweets(tweet_id='965734505205063680')
while True:
    tweet_id = input("Please enter the tweet ID to perform similarity search for:")
    if tweet_id in tf_idf.index:
        print_top_similar_tweets(tweet_id=tweet_id)
    else:
        print("Tweet ID not found. Please enter a valid ID.")
    print("\n\n")