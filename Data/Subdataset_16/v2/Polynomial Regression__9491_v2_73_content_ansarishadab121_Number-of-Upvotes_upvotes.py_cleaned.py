import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, Binarizer, PolynomialFeatures
from sklearn.linear_model import LassoLars
import matplotlib.pyplot as plt
import seaborn as sns
b1 = pd.read_csv('train_NIR5Yl1.csv')
b2 = pd.read_csv('test_8i3B3FC.csv')
print("Training Data Head:\n", b1.head())
print("Test Data Head:\n", b2.head())
print("Training Data Types:\n", b1.dtypes)
print("Training Data Description:\n", b1.describe())
print("Training Data Columns:\n", b1.columns)
print("Shapes of Training and Test Datasets:", b1.shape, b2.shape)
print("Value Counts of 'Tag' in Training Data:\n", b1['Tag'].value_counts())
sns.distplot(b1['Answers'])
plt.title('Distribution of Answers')
plt.show()
sns.distplot(b1['Views'])
plt.title('Distribution of Views')
plt.show()
sns.distplot(b1['Upvotes'])
plt.title('Distribution of Upvotes')
plt.show()
b1 = b1[b1['Views'] <= 3000000]
b3 = LabelEncoder()
b1['Tag'] = b3.fit_transform(b1['Tag'])
b1.drop(['ID', 'Username'], b4 = 1, inplace=True)
b5 = b1['Upvotes']
b6 = b1.drop(columns=['Upvotes'])
b7 = Binarizer(threshold=7)
b6['pd_watched'] = b7.fit_transform(b6[['Answers']])
b10, b11, y_train, b8 = train_test_split(b6, b5, test_size=0.22, random_state=205)
b9 = StandardScaler()
b10 = b9.fit_transform(b10)
b11 = b9.transform(b11)
b12 = PolynomialFeatures(degree=4)
b13 = b12.fit_transform(b10)
b14 = LassoLars(alpha=0.021, max_iter=150)
b14.fit(b13, y_train)
b15 = b12.transform(b11)
b16 = b14.predict(b15)
print("R^2 Score on Validation Set:", r2_score(b8, b16))
b17 = b2['ID']
b2.drop(['ID', 'Username'], b4 = 1, inplace=True)
b2['Tag'] = b3.transform(b2['Tag'])
b2['pd_watched'] = b7.transform(b2[['Answers']])
b2 = b9.transform(b2)
b18 = b12.transform(b2)
b19 = b14.predict(b18)
b19 = np.abs(b19)
b20 = pd.DataFrame({'ID': b17, 'Upvotes': b19})
b20.to_csv("linearregr.csv", b21 = False)
print("Submission file 'linearregr.csv' created successfully.")