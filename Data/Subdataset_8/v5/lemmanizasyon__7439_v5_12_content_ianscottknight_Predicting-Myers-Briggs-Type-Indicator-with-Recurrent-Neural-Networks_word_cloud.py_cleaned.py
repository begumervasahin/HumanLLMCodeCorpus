import os
import numpy as np
import pandas as pd
import csv
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.models import load_model
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
MODELS_DIR = "models"
DATA_DIR = "data"
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
NUM_EXTREME_EXAMPLES = 500
MAX_POST_LENGTH = 40
PERSONALITY_TYPES = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
PERSONALITY_TYPES = [type.lower() for type in PERSONALITY_TYPES]
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
def lemmatize_posts(posts):
    lemmatized = []
    for user_posts in posts:
        for post in user_posts:
            post = post.lower()
            for personality_type in PERSONALITY_TYPES:
                post = post.replace(" " + personality_type, "")
            lemmatized_post = " ".join([lemmatizer.lemmatize(word) for word in post.split() if word not in stop_words])
            lemmatized.append(lemmatized_post)
    return np.array(lemmatized)
def preprocess_posts(posts, tokenizer):
    lemmatized_posts = lemmatize_posts(posts)
    tokenized = tokenizer.texts_to_sequences(lemmatized_posts)
    return sequence.pad_sequences(tokenized, maxlen=MAX_POST_LENGTH)
tokenizer = Tokenizer()
tokenizer_path = os.path.join(MODELS_DIR, "tokenizer.pkl")
with open(tokenizer_path, "rb") as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)
for dimension in DIMENSIONS:
    test_posts_a = []
    test_posts_b = []
    with open(os.path.join(DATA_DIR, f"test_{dimension[0]}.csv"), "r") as file_a:
        reader = csv.reader(file_a)
        for row in reader:
            test_posts_a.append(row)
    with open(os.path.join(DATA_DIR, f"test_{dimension[1]}.csv"), "r") as file_b:
        reader = csv.reader(file_b)
        for row in reader:
            test_posts_b.append(row)
    test_posts = test_posts_a + test_posts_b
    model_path = os.path.join(MODELS_DIR, f"rnn_model_{dimension}.h5")
    model = load_model(model_path)
    x_test = preprocess_posts(test_posts, tokenizer)
    probs = model.predict_proba(x_test)
    sorted_probs = sorted(enumerate(probs), key=lambda x: x[1][0])
    min_prob_indices = sorted_probs[:NUM_EXTREME_EXAMPLES]
    max_prob_indices = sorted_probs[-NUM_EXTREME_EXAMPLES:]
    for i, extreme_indices in enumerate([min_prob_indices, max_prob_indices], start=1):
        for prob, index in extreme_indices:
            file_path = os.path.join(DATA_DIR, f"extreme_examples_{dimension[i-1]}.txt")
            with open(file_path, "a") as file:
                lemmatized_post = lemmatize_posts([test_posts[index]])[0]
                file.write(lemmatized_post + "\n\n")