import numpy as np
import pandas as pd
from numpy.linalg import norm
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
n_tweets_to_read = 5000
def cosine_similarity(a, b):
    return np.inner(a, b) / (norm(a) * norm(b)) if norm(a) != 0.0 and norm(b) != 0.0 else 0.0
def TermDocumentMatrix(docs, docIDs=None):
    vectorizer = CountVectorizer(lowercase=True, stop_words=None)
    tdm = vectorizer.fit_transform(docs)
    tdm_feature_names = vectorizer.get_feature_names()
    df = pd.DataFrame(tdm.toarray(), columns=tdm_feature_names, dtype="float64")
    if docIDs is not None:
        df.index = docIDs
    return df
ps = PorterStemmer()
tweets = []
tweetIDs = []
tweetsProcessed = []
with open("data/tweets.csv", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i < n_tweets_to_read:
            parts = line.split("\t")
            tweetID = parts[1]
            tweet = parts[3:]
            tweetIDs.append(tweetID)
            tweet_text = " ".join(tweet)
            tokenized_text = word_tokenize(tweet_text)
            stemmed_text = [ps.stem(word) for word in tokenized_text]
            processed_tweet = " ".join(stemmed_text)
            tweets.append(processed_tweet)
        else:
            break
tdf = TermDocumentMatrix(tweets, tweetIDs)
documentFrequencies = tdf.apply(lambda column: len(column[column > 0]), axis=0)
tf_idf = tdf.applymap(lambda x: 1.0 + np.log10(x) if x > 0.0 else 0.0)
idf = np.log10(len(tweets) / documentFrequencies)
tf_idf = tf_idf.multiply(idf)
def CosineSimilarityOfTweets(tweet1, tweet2):
    ID1 = tweetIDs[tweets.index(tweet1)]
    ID2 = tweetIDs[tweets.index(tweet2)]
    return cosine_similarity(tf_idf.loc[[ID1]], tf_idf.loc[[ID2]])
def printTopSimilarTweets(tweetID='965706998946893824', n=10):
    result = tf_idf.apply(lambda row: cosine_similarity(tf_idf.loc[[tweetID]], row), axis='columns').sort_values(ascending=False)
    print("Query: " + tweets[tweetIDs.index(tweetID)] + "\n")
    for i in range(n):
        print("{}: ".format(i+1) + tweets[tweetIDs.index(result.index[i])] + "\n")
printTopSimilarTweets(tweetID='965734505205063680')
while True:
    id = input("Please enter the tweet ID to perform similarity search for:")
    if id in tf_idf.index:
        printTopSimilarTweets(tweetID=id)
    else:
        print("Tweet ID not found. Please enter a valid ID.")
    print("\n\n")