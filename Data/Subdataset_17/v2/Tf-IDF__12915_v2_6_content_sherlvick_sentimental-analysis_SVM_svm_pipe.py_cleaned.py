import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
def train_model():
    np.random.seed(100)
    dataset_path = "Test.csv"
    corpus = pd.read_csv(dataset_path, encoding='utf-8-sig')
    texts = corpus['text']
    labels = corpus['label']
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('classifier', svm.SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    model = pipeline.fit(texts, labels)
    model_filename = 'Amz_5000_.sav'
    with open(model_filename, 'wb') as model_file:
        pickle.dump(model, model_file)
    model_saved = os.path.exists(model_filename)
    messages = ["Successful: Training model saved", "Oh Snap! Something's wrong", f"Number of samples: {len(corpus)}"]
    if model_saved:
        del messages[1]
    else:
        del messages[0]
    return messages
if __name__ == "__main__":
    result = train_model()
    print(result)