
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from google.colab import drive
drive.mount('/content/gdrive')
def load_dataset(file_path):
    return pd.read_csv(file_path)
def preprocess_dataset(data):
    bins = (2, 6.5, 8)
    group_names = ["bad", "good"]
    data["quality"] = pd.cut(data["quality"], bins=bins, labels=group_names)
    label_quality = LabelEncoder()
    data["quality"] = label_quality.fit_transform(data["quality"])
    return data
def visualize_quality_distribution(data):
    plt.figure(figsize=(6, 4))
    sns.countplot(data["quality"])
    plt.title("Count of Wine Quality Categories")
    plt.xlabel("Quality")
    plt.ylabel("Count")
    plt.show()
def split_dataset(data):
    X = data.drop("quality", axis=1)
    y = data["quality"]
    return X, y
def standardize_features(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled
def train_random_forest_classifier(X_train, y_train):
    rf_classifier = RandomForestClassifier(n_estimators=200)
    rf_classifier.fit(X_train, y_train)
    return rf_classifier
def evaluate_classifier(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
file_path = '/content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv'
wine_data = load_dataset(file_path)
wine_data = preprocess_dataset(wine_data)
print("First few rows of the dataset:")
print(wine_data.head())
visualize_quality_distribution(wine_data)
X, y = split_dataset(wine_data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_scaled, X_test_scaled = standardize_features(X_train, X_test)
rf_classifier = train_random_forest_classifier(X_train_scaled, y_train)
evaluate_classifier(rf_classifier, X_test_scaled, y_test)