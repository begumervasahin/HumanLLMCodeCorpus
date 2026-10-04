import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, Binarizer, PolynomialFeatures
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('train_NIR5Yl1.csv')
test = pd.read_csv('test_8i3B3FC.csv')
print(train.head())
print(test.head())
print(train.dtypes)
print(train.describe())
print(train.columns)
print(train.shape, test.shape)
print(train['Tag'].value_counts())
sns.distplot(train['Answers'])
plt.show()
sns.distplot(train['Views'])
plt.show()
sns.distplot(train['Upvotes'])
plt.show()
train = train.drop(train[train.Views > 3000000].index)
labelencoder_X = LabelEncoder()
train['Tag'] = labelencoder_X.fit_transform(train['Tag'])
train.drop(['ID', 'Username'], axis=1, inplace=True)
target = train['Upvotes']
train['pd_watched'] = Binarizer(threshold=7).fit_transform(train[['Answers']])
feature_names = [x for x in train.columns if x not in ['Upvotes']]
x_train, x_val, y_train, y_val = train_test_split(train[feature_names], target, test_size=0.22, random_state=205)
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_val = sc_X.transform(x_val)
poly_reg = PolynomialFeatures(degree=4, interaction_only=False, include_bias=True)
X_poly = poly_reg.fit_transform(x_train)
poly_reg.fit(x_train, y_train)
lin_reg_1 = linear_model.LassoLars(alpha=0.021, max_iter=150)
lin_reg_1.fit(X_poly, y_train)
pred_val = lin_reg_1.predict(poly_reg.transform(x_val))
print(r2_score(y_val, pred_val))
ids = test['ID']
test.drop(['ID', 'Username'], axis=1, inplace=True)
test['Tag'] = labelencoder_X.transform(test['Tag'])
test['pd_watched'] = Binarizer(threshold=7).fit_transform(test[['Answers']])
test = sc_X.transform(test)
pred_test = lin_reg_1.predict(poly_reg.transform(test))
pred_test = abs(pred_test)
submission = pd.DataFrame({'ID': ids, 'Upvotes': pred_test})
submission.to_csv("linearregr.csv", index=False)
print("Submission file 'linearregr.csv' created successfully.")