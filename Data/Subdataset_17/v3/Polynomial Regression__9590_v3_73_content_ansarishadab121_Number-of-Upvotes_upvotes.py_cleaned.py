import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, Binarizer, PolynomialFeatures
from sklearn.linear_model import LassoLars
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('train_NIR5Yl1.csv')
test = pd.read_csv('test_8i3B3FC.csv')
def display_basic_info(df, name):
    print(f"{name} Head:\n", df.head())
    print(f"{name} Data Types:\n", df.dtypes)
    print(f"{name} Description:\n", df.describe())
    print(f"{name} Columns:\n", df.columns)
display_basic_info(train, "Training Data")
display_basic_info(test, "Test Data")
print("Shapes of Training and Test Datasets:", train.shape, test.shape)
print("Value Counts of 'Tag' in Training Data:\n", train['Tag'].value_counts())
def plot_distribution(column, title):
    sns.distplot(column)
    plt.title(title)
    plt.show()
plot_distribution(train['Answers'], 'Distribution of Answers')
plot_distribution(train['Views'], 'Distribution of Views')
plot_distribution(train['Upvotes'], 'Distribution of Upvotes')
train = train[train['Views'] <= 3000000]
labelencoder_X = LabelEncoder()
train['Tag'] = labelencoder_X.fit_transform(train['Tag'])
train.drop(['ID', 'Username'], axis=1, inplace=True)
target = train['Upvotes']
features = train.drop(columns=['Upvotes'])
binarizer = Binarizer(threshold=7)
features['pd_watched'] = binarizer.fit_transform(features[['Answers']])
x_train, x_val, y_train, y_val = train_test_split(features, target, test_size=0.22, random_state=205)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_val = scaler.transform(x_val)
poly = PolynomialFeatures(degree=4)
x_train_poly = poly.fit_transform(x_train)
lasso_model = LassoLars(alpha=0.021, max_iter=150)
lasso_model.fit(x_train_poly, y_train)
x_val_poly = poly.transform(x_val)
pred_val = lasso_model.predict(x_val_poly)
print("R^2 Score on Validation Set:", r2_score(y_val, pred_val))
test_ids = test['ID']
test.drop(['ID', 'Username'], axis=1, inplace=True)
test['Tag'] = labelencoder_X.transform(test['Tag'])
test['pd_watched'] = binarizer.transform(test[['Answers']])
test = scaler.transform(test)
test_poly = poly.transform(test)
pred_test = lasso_model.predict(test_poly)
pred_test = np.abs(pred_test)
submission = pd.DataFrame({'ID': test_ids, 'Upvotes': pred_test})
submission.to_csv("linearregr.csv", index=False)
print("Submission file 'linearregr.csv' created successfully.")