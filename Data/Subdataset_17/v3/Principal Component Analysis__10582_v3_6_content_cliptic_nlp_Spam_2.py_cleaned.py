from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from wordcloud import WordCloud
def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], inplace=True)
    df.columns = ['labels', 'data']
    df['b_labels'] = df['labels'].map({'ham': 0, 'spam': 1})
    return df
def split_data(df):
    X = df["data"].values
    Y = df['b_labels'].values
    return train_test_split(X, Y, test_size=0.33, random_state=42)
def train_model(X_train, Y_train):
    count_vectorizer = CountVectorizer(decode_error='ignore')
    X_train_transformed = count_vectorizer.fit_transform(X_train)
    model = MultinomialNB()
    model.fit(X_train_transformed, Y_train)
    return model, count_vectorizer
def evaluate_model(model, count_vectorizer, X_train, X_test, Y_train, Y_test):
    X_train_transformed = count_vectorizer.transform(X_train)
    X_test_transformed = count_vectorizer.transform(X_test)
    train_score = model.score(X_train_transformed, Y_train)
    test_score = model.score(X_test_transformed, Y_test)
    print("Train score:", train_score)
    print("Test score:", test_score)
def visualize_wordcloud(df, label):
    words = ' '.join(df[df['labels'] == label]['data'].str.lower())
    wordcloud = WordCloud(width=600, height=400).generate(words)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {label}")
    plt.show()
def predict_and_display_misclassified(df, model, count_vectorizer):
    X_all = count_vectorizer.transform(df["data"].values)
    df['predictions'] = model.predict(X_all)
    sneaky_spam = df[(df['predictions'] == 0) & (df['b_labels'] == 1)]['data']
    not_actually_spam = df[(df['predictions'] == 1) & (df['b_labels'] == 0)]['data']
    print("THESE ARE THE SNEAKY SPAM MESSAGES:\n")
    for msg in sneaky_spam:
        print(msg)
    print("\nTHESE ARE THE NOT SPAM BUT CLASSIFIED AS THEY WERE:\n")
    for msg in not_actually_spam:
        print(msg)
def main():
    filepath = 'large_files/spam.csv'
    df = load_and_prepare_data(filepath)
    print(df.head())
    X_train, X_test, Y_train, Y_test = split_data(df)
    model, count_vectorizer = train_model(X_train, Y_train)
    evaluate_model(model, count_vectorizer, X_train, X_test, Y_train, Y_test)
    visualize_wordcloud(df, 'spam')
    visualize_wordcloud(df, 'ham')
    predict_and_display_misclassified(df, model, count_vectorizer)
if __name__ == "__main__":
    main()