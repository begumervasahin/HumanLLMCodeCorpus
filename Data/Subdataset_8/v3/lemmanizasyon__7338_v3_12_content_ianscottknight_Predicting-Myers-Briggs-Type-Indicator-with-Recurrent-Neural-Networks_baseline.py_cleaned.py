import os
import numpy as np
import pandas as pd
import csv
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
MODELS_DIR = "models"
DATA_DIR = "data"
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
TOP_WORDS = 2500
MAX_POST_LENGTH = 40
CROSS_VALIDATION = False
SAVE_MODEL = False
def lemmatize(posts, mbti_types, stop_words, lemmatizer):
    lemmatized_posts = [lemmatizer.lemmatize(word) for word in post.lower().split(" ") if word not in stop_words]
    return " ".join(lemmatized_posts)
def preprocess(posts, tokenizer, max_post_length):
    tokenized = tokenizer.texts_to_sequences(posts)
    return sequence.pad_sequences(tokenized, maxlen=max_post_length)
for dimension in DIMENSIONS:
    x_train, y_train, x_test, y_test = [], [], [], []
    with open(os.path.join(DATA_DIR, f"train_{dimension[0]}.csv"), "r") as file:
        reader = csv.reader(file)
        for row in reader:
            x_train.extend(row)
            y_train.extend([0] * len(row))
    with open(os.path.join(DATA_DIR, f"train_{dimension[1]}.csv"), "r") as file:
        reader = csv.reader(file)
        for row in reader:
            x_train.extend(row)
            y_train.extend([1] * len(row))
    with open(os.path.join(DATA_DIR, f"test_{dimension[0]}.csv"), "r") as file:
        reader = csv.reader(file)
        for row in reader:
            x_test.extend(row)
            y_test.extend([0] * len(row))
    with open(os.path.join(DATA_DIR, f"test_{dimension[1]}.csv"), "r") as file:
        reader = csv.reader(file)
        for row in reader:
            x_test.extend(row)
            y_test.extend([1] * len(row))
    MBTI_TYPES = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
    stop_words = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    tokenizer = Tokenizer(num_words=TOP_WORDS, filters="")
    tokenizer.fit_on_texts(x_train + x_test)
    x_train = [lemmatize(post, MBTI_TYPES, stop_words, lemmatizer) for post in x_train]
    x_test = [lemmatize(post, MBTI_TYPES, stop_words, lemmatizer) for post in x_test]
    df = pd.DataFrame(data={"text": x_train, "type": y_train})
    df = df.sample(frac=1).reset_index(drop=True)
    pipeline = Pipeline([
        ("vectorizer", CountVectorizer(stop_words="english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
    if CROSS_VALIDATION:
        k_fold = KFold(n_splits=6)
        scores, confusion_matrix_sum = [], np.array([[0, 0], [0, 0]])
        for train_indices, test_indices in k_fold:
            x_train_k, y_train_k = df.iloc[train_indices]["text"].values, df.iloc[train_indices]["type"].values
            x_test_k, y_test_k = df.iloc[test_indices]["text"].values, df.iloc[test_indices]["type"].values
            pipeline.fit(x_train_k, y_train_k)
            predictions_k = pipeline.predict(x_test_k)
            confusion_matrix_sum += confusion_matrix(y_test_k, predictions_k)
            score_k = accuracy_score(y_test_k, predictions_k)
            scores.append(score_k)
        with open(os.path.join(MODELS_DIR, f"baseline_cross_validation_{dimension}.txt"), "w") as file:
            file.write(f"*** {dimension[0]}/{dimension[1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            file.write(f"Total posts classified: {len(df)}\n")
            file.write(f"Accuracy: {sum(scores) / len(scores)}\n")
            file.write("Confusion matrix: \n")
            file.write(np.array2string(confusion_matrix_sum, separator=", "))
    pipeline.fit(df["text"].values, df["type"].values)
    predictions = pipeline.predict(x_test)
    confusion_matrix_test = confusion_matrix(y_test, predictions)
    accuracy_test = accuracy_score(y_test, predictions)
    with open(os.path.join(MODELS_DIR, f"baseline_accuracy_{dimension}.txt"), "w") as file:
        file.write(f"*** {dimension[0]}/{dimension[1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        file.write(f"Total posts classified: {len(x_test)}\n")
        file.write(f"Accuracy: {accuracy_test}\n")
        file.write("Confusion matrix: \n")
        file.write(np.array2string(confusion_matrix_test, separator=", "))
    print(f"Wrote training/test results for {dimension} here: {os.path.join(MODELS_DIR, f'baseline_accuracy_{dimension}.txt')}")
    if SAVE_MODEL:
        pipeline.named_steps["classifier"].model.save(os.path.join(MODELS_DIR, f"NB_classifier_{dimension}.h5"))
        pipeline.named_steps["classifier"].model = None
        joblib.dump(pipeline, os.path.join(MODELS_DIR, f"baseline_pipeline_{dimension}.pkl"))
    del pipeline