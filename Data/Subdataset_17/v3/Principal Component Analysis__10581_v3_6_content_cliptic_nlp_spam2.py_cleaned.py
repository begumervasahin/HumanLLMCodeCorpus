from __future__ import print_function, division
from builtins import range
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from wordcloud import WordCloud
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
    df.columns = ['labels', 'data']
    df['b_labels'] = df['labels'].map({'ham': 0, 'spam': 1})
    return df
def split_data(df, test_size=0.33, random_state=42):
    Y = df['b_labels'].values
    df_train, df_test, Ytrain, Ytest = train_test_split(df['data'], Y, test_size=test_size, random_state=random_state)
    return df_train, df_test, Ytrain, Ytest
def create_and_train_model(Xtrain, Ytrain):
    model = MultinomialNB()
    model.fit(Xtrain, Ytrain)
    return model
def print_model_scores(model, Xtrain, Ytrain, Xtest, Ytest):
    print("Train score:", model.score(Xtrain, Ytrain))
    print("Test score:", model.score(Xtest, Ytest))
def visualize_word_cloud(label, df):
    words = ' '.join(df[df['labels'] == label]['data'].str.lower())
    wordcloud = WordCloud(width=600, height=400).generate(words)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {label}')
    plt.show()
def print_misclassified_messages(df):
    sneaky_spam = df[(df['predictions'] == 0) & (df['b_labels'] == 1)]['data']
    print("\nSneaky Spam Messages (False Negatives):")
    for msg in sneaky_spam:
        print(msg)
    not_actually_spam = df[(df['predictions'] == 1) & (df['b_labels'] == 0)]['data']
    print("\nNot Actually Spam Messages (False Positives):")
    for msg in not_actually_spam:
        print(msg)
def main():
    filepath = 'large_files/spam.csv'
    df = load_and_preprocess_data(filepath)
    df_train, df_test, Ytrain, Ytest = split_data(df)
    tfidf = TfidfVectorizer(decode_error='ignore')
    Xtrain = tfidf.fit_transform(df_train)
    Xtest = tfidf.transform(df_test)
    model = create_and_train_model(Xtrain, Ytrain)
    print_model_scores(model, Xtrain, Ytrain, Xtest, Ytest)
    visualize_word_cloud('spam', df)
    visualize_word_cloud('ham', df)
    X = tfidf.transform(df['data'])
    df['predictions'] = model.predict(X)
    print_misclassified_messages(df)
if __name__ == "__main__":
    main()