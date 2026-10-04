
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
def fonk1(file_description):
    b1 = files.upload()
    b2 = next(iter(b1))
    return pd.read_csv(io.StringIO(b1[b2].decode('utf-8')))
b3 = fonk1('train_NIR5Yl1.csv')
b4 = fonk1('test_8i3B3FC.csv')
def fonk2(df):
    print(df.head())
    print(df.dtypes)
    print(df.describe())
    print(df.columns)
    print(df.shape)
    print(df['Tag'].value_counts())
fonk2(b3)
fonk2(b4)
def fonk3(df, columns):
    for col in columns:
        sns.distplot(df[col])
        plt.show()
fonk3(b3, ['Answers', 'Views', 'Upvotes'])
print(b3.isnull().sum())
b3 = b3[b3['Views'] <= 3000000]
b5 = LabelEncoder()
b3['Tag'] = b5.fit_transform(b3['Tag'])
b3.drop(['ID', 'Username'], b6 = 1, inplace=True)
b7 = b3['Upvotes']
b8 = Binarizer(threshold=7)
b3['pd_watched'] = b8.transform([b3['Answers']])[0]
b9 = [x for x in b3.columns if x not in ['Upvotes']]
b12, b13, y_train, b10 = train_test_split(b3[b9], b7, test_size=0.22, random_state=205)
b11 = StandardScaler()
b12 = b11.fit_transform(b12)
b13 = b11.transform(b13)
b14 = PolynomialFeatures(degree=4, interaction_only=False, include_bias=True)
b15 = b14.fit_transform(b12)
b16 = linear_model.LassoLars(alpha=0.021, max_iter=150)
b16.fit(b15, y_train)
b17 = b16.predict(b14.transform(b13))
print(f"R2 Score: {r2_score(b10, b17)}")
def fonk4(b19):
    b18 = b19['ID']
    b19.drop(['ID', 'Username'], b6 = 1, inplace=True)
    b19['Tag'] = b5.transform(b19['Tag'])
    b19['pd_watched'] = b8.transform([b19['Answers']])[0]
    b19 = b11.transform(b19)
    return b19, b18
b4, b18 = fonk4(b4)
b20 = b16.predict(b14.transform(b4))
b20 = np.abs(b20)
b21 = pd.DataFrame({'ID': b18, 'Upvotes': b20})
b21.to_csv("linearregr.csv", b22 = False)
files.download('linearregr.csv')