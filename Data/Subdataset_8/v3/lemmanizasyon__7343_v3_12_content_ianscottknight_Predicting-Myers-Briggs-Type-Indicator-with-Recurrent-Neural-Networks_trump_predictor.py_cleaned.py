import os
import csv
import pickle
import numpy as np
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.preprocessing import sequence, text
from keras.models import load_model
MODELS_DIR = "models"
DATA_DIR = "data"
TRUMP_TWEETS_PATH = os.path.join(DATA_DIR, "trumptweets.csv")
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
MODEL_BATCH_SIZE = 128
TOP_WORDS = 2500
MAX_POST_LENGTH = 40
EMBEDDING_VECTOR_LENGTH = 20
def preprocess_tweets(tweets, lemmatizer, types, stop_words, tokenizer):
    lemmatized_tweets = []
    for tweet in tweets:
        tweet = tweet.lower()
        for t in types:
            tweet = tweet.replace(" " + t, "")
        lemmatized_tweet = " ".join([
            lemmatizer.lemmatize(word)
            for word in tweet.split(" ")
            if word not in stop_words
        ])
        lemmatized_tweets.append(lemmatized_tweet)
    tokenized_tweets = tokenizer.texts_to_sequences(lemmatized_tweets)
    return sequence.pad_sequences(tokenized_tweets, maxlen=MAX_POST_LENGTH)
tweets = []
with open(TRUMP_TWEETS_PATH, "r", encoding="ISO-8859-1") as file:
    reader = csv.reader(file)
    for row in reader:
        tweets.append(row[0])
types = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
types = [t.lower() for t in types]
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english")
final_prediction = ""
for dim in DIMENSIONS:
    model = load_model(os.path.join(MODELS_DIR, f"rnn_model_{dim}.h5"))
    with open(os.path.join(MODELS_DIR, f"rnn_tokenizer_{dim}.pkl"), "rb") as file:
        tokenizer = pickle.load(file)
    processed_tweets = preprocess_tweets(tweets, lemmatizer, types, stop_words, tokenizer)
    predictions = model.predict(processed_tweets)
    avg_prediction = float(sum(predictions) / len(predictions))
    print(f"Dimension: {dim}")
    print(f"Average Prediction: {avg_prediction}")
    final_prediction += dim[1] if avg_prediction >= 0.5 else dim[0]
print("")
print("Final prediction:", final_prediction)