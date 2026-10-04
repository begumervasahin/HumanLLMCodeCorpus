
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, Binarizer, PolynomialFeatures
from sklearn import linear_model
import seaborn as sns
import matplotlib.pyplot as plt
!pip install -U scikit-learn
from google.colab import files
b1 = files.upload()
b2 = pd.read_csv(io.StringIO(b1['train_NIR5Yl1.csv'].decode('utf-8')))
b1 = files.upload()
b3 = pd.read_csv(io.StringIO(b1['test_8i3B3FC.csv'].decode('utf-8')))
print(b2.head())
print(b3.head())
print(b2.dtypes)
print(b2.describe())
print(b2.columns)
print(b2.shape, b3.shape)
print(b2['Tag'].value_counts())
sns.distplot(b2['Answers'])
plt.show()
sns.distplot(b2['Views'])
plt.show()
sns.distplot(b2['Upvotes'])
plt.show()
print(b2.isnull().sum())
b2 = b2[b2['Views'] <= 3000000]
b4 = LabelEncoder()
b2['Tag'] = b4.fit_transform(b2['Tag'])
b2.drop(['ID', 'Username'], b5 = 1, inplace=True)
b6 = b2['Upvotes']
b7 = Binarizer(threshold=7)
b2['pd_watched'] = b7.transform([b2['Answers']])[0]
b8 = [x for x in b2.columns if x not in ['Upvotes']]
b11, b12, y_train, b9 = train_test_split(b2[b8], b6, test_size=0.22, random_state=205)
b10 = StandardScaler()
b11 = b10.fit_transform(b11)
b12 = b10.transform(b12)
b13 = PolynomialFeatures(degree=4, interaction_only=False, include_bias=True)
b14 = b13.fit_transform(b11)
b15 = linear_model.LassoLars(alpha=0.021, max_iter=150)
b15.fit(b14, y_train)
b16 = b15.predict(b13.transform(b12))
print(r2_score(b9, b16))
b17 = b3['ID']
b3.drop(['ID', 'Username'], b5 = 1, inplace=True)
b3['Tag'] = b4.transform(b3['Tag'])
b3['pd_watched'] = b7.transform([b3['Answers']])[0]
b3 = b10.transform(b3)
b18 = b15.predict(b13.transform(b3))
b18 = abs(b18)
b19 = pd.DataFrame({'ID': b17, 'Upvotes': b18})
b19.to_csv("linearregr.csv", b20 = False)
files.download('linearregr.csv')