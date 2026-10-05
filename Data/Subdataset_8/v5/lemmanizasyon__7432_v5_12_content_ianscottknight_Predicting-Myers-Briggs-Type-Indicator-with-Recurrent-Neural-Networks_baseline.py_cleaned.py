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
for dimension in DIMENSIONS:
    x_train, y_train = [], []
    x_test, y_test = [], []
    for data_type in ["train", "test"]:
        for personality_type in [dimension[0], dimension[1]]:
            file_path = os.path.join(DATA_DIR, f"{data_type}_{personality_type}.csv")
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    for post in row:
                        x_data, y_data = x_train, y_train if data_type == "train" else x_test, y_test
                        x_data.append(post)
                        y_data.append(0 if personality_type == dimension[0] else 1)
    MBTI_TYPES = [
        "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
        "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
    ]
    stop_words = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    tokenizer = Tokenizer(num_words=TOP_WORDS, filters="")
    tokenizer.fit_on_texts(x_train + x_test)
    def preprocess(data):
        lemmatized_data = []
        for post in data:
            temp = post.lower()
            for mbti_type in MBTI_TYPES:
                mbti_type = mbti_type.lower()
                temp = temp.replace(f" {mbti_type}", "")
            temp = " ".join([lemmatizer.lemmatize(word) for word in temp.split(" ") if word not in stop_words])
            lemmatized_data.append(temp)
        tokenized_data = tokenizer.texts_to_sequences(lemmatized_data)
        return sequence.pad_sequences(tokenized_data, maxlen=MAX_POST_LENGTH)
    x_train, x_test = preprocess(x_train), preprocess(x_test)
    df = pd.DataFrame(data={"text": x_train, "type": y_train}).sample(frac=1).reset_index(drop=True)
    pipeline = Pipeline([
        ("vectorizer", CountVectorizer(stop_words="english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
    if CROSS_VALIDATION:
        k_fold = KFold(n_splits=6)
        scores_k = []
        confusion_k = np.zeros((2, 2))
        for train_indices, test_indices in k_fold:
            x_train_k, y_train_k = df.iloc[train_indices]["text"].values, df.iloc[train_indices]["type"].values
            x_test_k, y_test_k = df.iloc[test_indices]["text"].values, df.iloc[test_indices]["type"].values
            pipeline.fit(x_train_k, y_train_k)
            predictions_k = pipeline.predict(x_test_k)
            confusion_k += confusion_matrix(y_test_k, predictions_k)
            score_k = accuracy_score(y_test_k, predictions_k)
            scores_k.append(score_k)
        with open(os.path.join(MODELS_DIR, f"baseline_cross_validation_{dimension}.txt"), "w") as f:
            f.write(f"*** {dimension[0]}/{dimension[1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            f.write(f"Total posts classified: {len(df)}\n")
            f.write(f"Accuracy: {sum(scores_k) / len(scores_k)}\n")
            f.write("Confusion matrix: \n")
            f.write(np.array2string(confusion_k, separator=", "))
    pipeline.fit(df["text"].values, df["type"].values)
    predictions = pipeline.predict(x_test)
    confusion = confusion_matrix(y_test, predictions)
    score = accuracy_score(y_test, predictions)
    with open(os.path.join(MODELS_DIR, f"baseline_accuracy_{dimension}.txt"), "w") as f:
        f.write(f"*** {dimension[0]}/{dimension[1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        f.write(f"Total posts classified: {len(x_test)}\n")
        f.write(f"Accuracy: {score}\n")
        f.write("Confusion matrix: \n")
        f.write(np.array2string(confusion, separator=", "))
    print(f"Wrote training/test results for {dimension} here: {os.path.join(MODELS_DIR, f'baseline_accuracy_{dimension}.txt')}")
    if SAVE_MODEL:
        model_path = os.path.join(MODELS_DIR, f"NB_classifier_{dimension}.h5")
        pipeline.named_steps["classifier"].model.save(model_path)
        pipeline.named_steps["classifier"].model = None
        joblib.dump(pipeline, os.path.join(MODELS_DIR, f"baseline_pipeline_{dimension}.pkl"))
    del pipeline