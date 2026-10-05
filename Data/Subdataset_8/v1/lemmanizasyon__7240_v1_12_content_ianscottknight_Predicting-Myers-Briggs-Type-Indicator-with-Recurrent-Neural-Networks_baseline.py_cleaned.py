import os
import numpy as np
import pandas as pd
import csv
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier, Perceptron
from sklearn.neighbors import KNeighborsClassifier
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
MODELS_DIR = "models"
DATA_DIR = "data"
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
TOP_WORDS = 2500
MAX_POST_LENGTH = 40
CROSS_VALIDATION = False
SAVE_MODEL = False
def lemmatize(x, MBTI_TYPES, stop_words, lemmatizer):
    lemmatized = []
    for post in x:
        temp = post.lower()
        for mbti_type in MBTI_TYPES:
            mbti_type = mbti_type.lower()
            temp = temp.replace(" " + mbti_type, "")
        temp = " ".join([lemmatizer.lemmatize(word) for word in temp.split(" ") if (word not in stop_words)])
        lemmatized.append(temp)
    return np.array(lemmatized)
def preprocess(x, tokenizer, MAX_POST_LENGTH):
    tokenized = tokenizer.texts_to_sequences(x)
    return sequence.pad_sequences(tokenized, maxlen=MAX_POST_LENGTH)
for k in range(len(DIMENSIONS)):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    with open(os.path.join(DATA_DIR, f"train_{DIMENSIONS[k][0]}.csv"), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for post in row:
                x_train.append(post)
                y_train.append(0)
    with open(os.path.join(DATA_DIR, f"train_{DIMENSIONS[k][1]}.csv"), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for post in row:
                x_train.append(post)
                y_train.append(1)
    with open(os.path.join(DATA_DIR, f"test_{DIMENSIONS[k][0]}.csv"), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for post in row:
                x_test.append(post)
                y_test.append(0)
    with open(os.path.join(DATA_DIR, f"test_{DIMENSIONS[k][1]}.csv"), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for post in row:
                x_test.append(post)
                y_test.append(1)
    MBTI_TYPES = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
    stop_words = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    tokenizer = Tokenizer(num_words=TOP_WORDS, filters="")
    tokenizer.fit_on_texts(x_train + x_test)
    x_train = lemmatize(x_train, MBTI_TYPES, stop_words, lemmatizer)
    x_test = lemmatize(x_test, MBTI_TYPES, stop_words, lemmatizer)
    df = pd.DataFrame(data={"text": x_train, "type": y_train})
    df = df.sample(frac=1).reset_index(drop=True)
    pipeline = Pipeline([
        ("vectorizer", CountVectorizer(stop_words="english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
    if CROSS_VALIDATION:
        k_fold = KFold(n_splits=6)
        scores_k = []
        confusion_k = np.array([[0, 0], [0, 0]])
        for train_indices, test_indices in k_fold:
            x_train_k = df.iloc[train_indices]["text"].values
            y_train_k = df.iloc[train_indices]["type"].values
            x_test_k = df.iloc[test_indices]["text"].values
            y_test_k = df.iloc[test_indices]["type"].values
            pipeline.fit(x_train_k, y_train_k)
            predictions_k = pipeline.predict(x_test_k)
            confusion_k += confusion_matrix(y_test_k, predictions_k)
            score_k = accuracy_score(y_test_k, predictions_k)
            scores_k.append(score_k)
        with open(os.path.join(MODELS_DIR, f"baseline_cross_validation_{DIMENSIONS[k]}.txt"), "w") as f:
            f.write(f"*** {DIMENSIONS[k][0]}/{DIMENSIONS[k][1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            f.write(f"Total posts classified: {len(df)}\n")
            f.write(f"Accuracy: {sum(scores_k) / len(scores_k)}\n")
            f.write("Confusion matrix: \n")
            f.write(np.array2string(confusion_k, separator=", "))
    pipeline.fit(df["text"].values, df["type"].values)
    predictions = pipeline.predict(x_test)
    confusion = confusion_matrix(y_test, predictions)
    score = accuracy_score(y_test, predictions)
    with open(os.path.join(MODELS_DIR, f"baseline_accuracy_{DIMENSIONS[k]}.txt"), "w") as f:
        f.write(f"*** {DIMENSIONS[k][0]}/{DIMENSIONS[k][1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        f.write(f"Total posts classified: {len(x_test)}\n")
        f.write(f"Accuracy: {score}\n")
        f.write("Confusion matrix: \n")
        f.write(np.array2string(confusion, separator=", "))
    print(f"Wrote training / test results for {DIMENSIONS[k]} here: {os.path.join(MODELS_DIR, f'baseline_accuracy_{DIMENSIONS[k]}.txt')}")
    if SAVE_MODEL:
        pipeline.named_steps["classifier"].model.save(os.path.join(MODELS_DIR, f"NB_classifier_{DIMENSIONS[k]}.h5"))
        pipeline.named_steps["classifier"].model = None
        joblib.dump(pipeline, os.path.join(MODELS_DIR, f"baseline_pipeline_{DIMENSIONS[k]}.pkl"))
    del pipeline