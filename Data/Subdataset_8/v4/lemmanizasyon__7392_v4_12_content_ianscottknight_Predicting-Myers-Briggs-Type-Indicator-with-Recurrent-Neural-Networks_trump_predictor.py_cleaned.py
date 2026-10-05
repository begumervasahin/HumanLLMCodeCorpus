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
final_personality = ""
x_test = []
with open(TRUMP_TWEETS_PATH, "r", encoding="ISO-8859-1") as file:
    reader = csv.reader(file)
    for row in reader:
        x_test.append(row)
types = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
types = [personality.lower() for personality in types]
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english")
def lemmatize_text(text):
    lemmatized = []
    for post in text:
        temp = post.lower()
        for personality_type in types:
            temp = temp.replace(" " + personality_type, "")
        temp = " ".join([lemmatizer.lemmatize(word) for word in temp.split(" ") if word not in stop_words])
        lemmatized.append(temp)
    return np.array(lemmatized)
for dimension in DIMENSIONS:
    model = load_model(os.path.join(MODELS_DIR, f"rnn_model_{dimension}.h5"))
    with open(os.path.join(MODELS_DIR, f"rnn_tokenizer_{dimension}.pkl"), "rb") as file:
        tokenizer = pickle.load(file)
    def preprocess_text(text):
        lemmatized_text = lemmatize_text(text)
        tokenized_text = tokenizer.texts_to_sequences(lemmatized_text)
        return sequence.pad_sequences(tokenized_text, maxlen=MAX_POST_LENGTH)
    predictions = model.predict(preprocess_text(x_test))
    prediction_avg = float(sum(predictions) / len(predictions))
    print(f"{dimension}:")
    print(prediction_avg)
    if prediction_avg >= 0.5:
        final_personality += dimension[1]
    else:
        final_personality += dimension[0]
print("")
print("Final prediction:", final_personality)