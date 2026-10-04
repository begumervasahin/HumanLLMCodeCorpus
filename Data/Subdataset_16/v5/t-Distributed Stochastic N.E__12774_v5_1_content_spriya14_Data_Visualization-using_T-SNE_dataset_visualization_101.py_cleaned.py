import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
def fonk1(url):
    b1 = pd.read_csv(url)
    print("Initial Data Preview:")
    print(b1.head())
    return b1
def fonk2(b1):
    b2 = b1.columns[b1.isnull().sum() == 0]
    b3 = b1[b2]
    b3 = b3.iloc[:, 7:]
    print("\nRemaining Columns After Cleaning:")
    print(b3.columns)
    return b3
def fonk3(b1):
    b4 = b1.iloc[:, :-1].values
    b5 = b1.iloc[:, -1].values
    b6 = StandardScaler()
    b7 = b6.fit_transform(b4)
    b8 = LabelEncoder()
    b9 = b8.fit_transform(b5)
    print("\nClass Labels:")
    print(np.unique(b5))
    X_train, X_test, y_train, b10 = train_test_split(b7, b9, test_size=0.1, random_state=0)
    return X_train, X_test, y_train, b10, b8
def fonk4(X_test, b10, b8):
    b11 = TSNE(n_components=2, random_state=0)
    b12 = b11.fit_transform(X_test)
    b13 = ['s', 'd', 'o', '^', 'v']
    b14 = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
    b15 = dict(zip(np.unique(b10), b14))
    plt.figure(b16 = (10, 8))
    for idx, class_label in enumerate(np.unique(b10)):
        plt.scatter(b12[b10 = = class_label, 0], b12[b10 == class_label, 1],
                    b17 = b15[class_label], marker=b13[idx],
                    b18 = b8.inverse_transform([class_label])[0])
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.legend(b19 = 'upper left')
    plt.title('t-SNE Visualization of Test Data')
    plt.show()
def fonk5():
    b20 = "https:
    b1 = fonk1(b20)
    b3 = fonk2(b1)
    X_train, X_test, y_train, b10, b8 = fonk3(b3)
    fonk4(X_test, b10, b8)
if b21 = = "__main__":
    fonk5()