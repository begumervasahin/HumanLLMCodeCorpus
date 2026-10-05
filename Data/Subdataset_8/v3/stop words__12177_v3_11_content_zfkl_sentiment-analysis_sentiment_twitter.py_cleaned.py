import re
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from nltk.corpus import stopwords
import scipy.stats as st
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'www\.\S+|https?:
    text = re.sub(r'[!?,\'"-]', ' ', text)
    text = re.sub(r'<br\s*/><br\s*/>', ' ', text)
    text = text.lower()
    return text
def read_file_and_clean(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned_content = clean_text(content)
    words = cleaned_content.split()
    filtered_words = [word for word in words if word not in set(stopwords.words('english'))]
    return ' '.join(filtered_words)
def prepare_data(neg_files, pos_files):
    texts = []
    labels = []
    for file_path in neg_files:
        texts.append(read_file_and_clean(file_path))
        labels.append(0)
    for file_path in pos_files:
        texts.append(read_file_and_clean(file_path))
        labels.append(1)
    return pd.DataFrame({'text': texts, 'label': labels})
def display_confusion_matrix(cm, class_names):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names, rotation=45)
    plt.yticks(tick_marks, class_names)
    plt.tight_layout()
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()
if __name__ == "__main__":
    neg_files_train = glob.glob("../aclImdb/train/neg/*.txt")
    pos_files_train = glob.glob("../aclImdb/train/pos/*.txt")
    df = prepare_data(neg_files_train, pos_files_train)
    vectorizer = CountVectorizer(min_df=0.01)
    X = vectorizer.fit_transform(df['text'])
    Y = df['label']
    model_params = {
        "penalty": ['l1', 'l2'],
        "C": st.expon(scale=100)
    }
    model = RandomizedSearchCV(LogisticRegression(solver='liblinear'), model_params, n_iter=10, cv=5, random_state=10)
    model.fit(X, Y)
    print(f"Best parameters: {model.best_params_}")
    print(f"Best cross-validation score: {model.best_score_:.2f}")