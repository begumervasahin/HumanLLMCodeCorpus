import gc
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, accuracy_score
warnings.filterwarnings("ignore")
def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    df = df.sample(frac=1).reset_index(drop=True)
    return df
def encode_target_variable(df):
    le = LabelEncoder()
    y = le.fit_transform(df['app_name'])
    X = df.iloc[:, 0:7].values
    return X, y, le.classes_
def plot_class_distribution(y_train, y_test):
    unique_train, counts_train = np.unique(y_train, return_counts=True)
    unique_test, counts_test = np.unique(y_test, return_counts=True)
    plt.bar(unique_train, counts_train, alpha=0.6, label='Training set')
    plt.bar(unique_test, counts_test, alpha=0.6, label='Testing set')
    plt.title('Class Frequency Distribution')
    plt.xlabel('Class (encoded)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
def evaluate_classifier(classifier, X_train, y_train, X_test, y_test, classifier_name):
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    not_predicted = set(y_test) - set(y_pred)
    print(f"*** {classifier_name} ***")
    print("Classes not predicted:", str(not_predicted), len(not_predicted))
    print("F-score:", f1_score(y_test, y_pred, average='weighted', labels=np.unique(y_pred)))
    print("Accuracy:", accuracy_score(y_test, y_pred))
    del classifier
    del y_pred
    gc.collect()
def plot_actual_vs_predicted(y_test, y_pred):
    _, ax = plt.subplots()
    ax.scatter(range(len(y_test)), y_test, c='blue', label='Actual', alpha=0.3)
    ax.scatter(range(len(y_pred)), y_pred, c='red', label='Predicted', alpha=0.3)
    plt.title('Actual and Predicted Values')
    plt.xlabel('Samples')
    plt.ylabel('Classes')
    plt.legend()
    plt.show()
def main():
    df = load_and_prepare_data('10k.anon.csv')
    print(df.head(10).to_string())
    print(f"Number of classes: {df['app_name'].nunique()}")
    print(f"Number of samples: {len(df)}")
    X, y, class_names = encode_target_variable(df)
    print("Encoded classes:", list(class_names))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
    plot_class_distribution(y_train, y_test)
    classifiers = {
        "KNN": KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='kd_tree', leaf_size=30),
        "Naive Bayes (Gaussian)": GaussianNB(),
        "Multilayer Perceptron": MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='lbfgs', max_iter=200)
    }
    for name, clf in classifiers.items():
        evaluate_classifier(clf, X_train, y_train, X_test, y_test, name)
    rf = RandomForestClassifier(n_estimators=100, criterion='gini', class_weight='balanced')
    rf.fit(X_train, y_train)
    export_graphviz(rf.estimators_[5], out_file='tree.dot', feature_names=df.columns[0:7],
                    class_names=class_names, rounded=True, proportion=False, precision=2, filled=True)
    y_pred = rf.predict(X_test)
    print("*** Random Forest ***")
    print("F-score:", f1_score(y_test, y_pred, average='weighted', labels=np.unique(y_pred)))
    print("Accuracy:", accuracy_score(y_test, y_pred))
    scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')
    print("Cross-validated accuracy:", scores)
    plot_actual_vs_predicted(y_test, y_pred)
    gc.collect()
if __name__ == "__main__":
    main()