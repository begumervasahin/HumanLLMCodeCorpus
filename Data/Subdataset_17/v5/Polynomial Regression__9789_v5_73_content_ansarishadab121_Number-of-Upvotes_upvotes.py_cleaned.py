
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, Binarizer, PolynomialFeatures
from sklearn import linear_model
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
import io
!pip install -U scikit-learn
def upload_and_read_csv(file_description):
    uploaded = files.upload()
    file_name = next(iter(uploaded))
    return pd.read_csv(io.StringIO(uploaded[file_name].decode('utf-8')))
train = upload_and_read_csv('train_NIR5Yl1.csv')
test = upload_and_read_csv('test_8i3B3FC.csv')
def display_basic_info(df):
    print(df.head())
    print(df.dtypes)
    print(df.describe())
    print(df.columns)
    print(df.shape)
    print(df['Tag'].value_counts())
display_basic_info(train)
display_basic_info(test)
def visualize_distributions(df, columns):
    for col in columns:
        sns.distplot(df[col])
        plt.show()
visualize_distributions(train, ['Answers', 'Views', 'Upvotes'])
print(train.isnull().sum())
train = train[train['Views'] <= 3000000]
labelencoder_X = LabelEncoder()
train['Tag'] = labelencoder_X.fit_transform(train['Tag'])
train.drop(['ID', 'Username'], axis=1, inplace=True)
target = train['Upvotes']
bn = Binarizer(threshold=7)
train['pd_watched'] = bn.transform([train['Answers']])[0]
feature_names = [x for x in train.columns if x not in ['Upvotes']]
x_train, x_val, y_train, y_val = train_test_split(train[feature_names], target, test_size=0.22, random_state=205)
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_val = sc_X.transform(x_val)
poly_reg = PolynomialFeatures(degree=4, interaction_only=False, include_bias=True)
X_poly = poly_reg.fit_transform(x_train)
lin_reg_1 = linear_model.LassoLars(alpha=0.021, max_iter=150)
lin_reg_1.fit(X_poly, y_train)
pred_val = lin_reg_1.predict(poly_reg.transform(x_val))
print(f"R2 Score: {r2_score(y_val, pred_val)}")
def preprocess_test_data(test_df):
    ids = test_df['ID']
    test_df.drop(['ID', 'Username'], axis=1, inplace=True)
    test_df['Tag'] = labelencoder_X.transform(test_df['Tag'])
    test_df['pd_watched'] = bn.transform([test_df['Answers']])[0]
    test_df = sc_X.transform(test_df)
    return test_df, ids
test, ids = preprocess_test_data(test)
pred_test = lin_reg_1.predict(poly_reg.transform(test))
pred_test = np.abs(pred_test)
submission = pd.DataFrame({'ID': ids, 'Upvotes': pred_test})
submission.to_csv("linearregr.csv", index=False)
files.download('linearregr.csv')