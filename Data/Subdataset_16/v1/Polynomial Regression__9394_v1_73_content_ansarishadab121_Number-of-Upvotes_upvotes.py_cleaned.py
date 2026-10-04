import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, Binarizer, PolynomialFeatures
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
b1 = pd.read_csv('train_NIR5Yl1.csv')
b2 = pd.read_csv('test_8i3B3FC.csv')
print(b1.head())
print(b2.head())
print(b1.dtypes)
print(b1.describe())
print(b1.columns)
print(b1.shape, b2.shape)
print(b1['Tag'].value_counts())
sns.distplot(b1['Answers'])
plt.show()
sns.distplot(b1['Views'])
plt.show()
sns.distplot(b1['Upvotes'])
plt.show()
b1 = b1.drop(b1[b1.Views > 3000000].b19)
b3 = LabelEncoder()
b1['Tag'] = b3.fit_transform(b1['Tag'])
b1.drop(['ID', 'Username'], b4 = 1, inplace=True)
b5 = b1['Upvotes']
b1['pd_watched'] = Binarizer(b6 = 7).fit_transform(b1[['Answers']])
b7 = [x for x in b1.columns if x not in ['Upvotes']]
b10, b11, y_train, b8 = train_test_split(b1[b7], b5, test_size=0.22, random_state=205)
b9 = StandardScaler()
b10 = b9.fit_transform(b10)
b11 = b9.transform(b11)
b12 = PolynomialFeatures(degree=4, interaction_only=False, include_bias=True)
b13 = b12.fit_transform(b10)
b12.fit(b10, y_train)
b14 = linear_model.LassoLars(alpha=0.021, max_iter=150)
b14.fit(b13, y_train)
b15 = b14.predict(b12.transform(b11))
print(r2_score(b8, b15))
b16 = b2['ID']
b2.drop(['ID', 'Username'], b4 = 1, inplace=True)
b2['Tag'] = b3.transform(b2['Tag'])
b2['pd_watched'] = Binarizer(b6 = 7).fit_transform(b2[['Answers']])
b2 = b9.transform(b2)
b17 = b14.predict(b12.transform(b2))
b17 = abs(b17)
b18 = pd.DataFrame({'ID': b16, 'Upvotes': b17})
b18.to_csv("linearregr.csv", b19 = False)
print("Submission file 'linearregr.csv' created successfully.")