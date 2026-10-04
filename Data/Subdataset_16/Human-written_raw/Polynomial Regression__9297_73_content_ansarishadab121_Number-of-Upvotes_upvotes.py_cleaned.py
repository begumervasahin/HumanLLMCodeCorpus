
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
pip install -U scikit-learn
from google.colab import files
b1 = files.upload()
import pandas as pd
import io
b2 = pd.read_csv(io.StringIO(b1['train_NIR5Yl1.csv'].decode('utf-8')))
from google.colab import files
b1 = files.upload()
import pandas as pd
import io
b3 = pd.read_csv(io.StringIO(b1['test_8i3B3FC.csv'].decode('utf-8')))
b2.head()
b3.head()
b2.dtypes
b2.describe()
b2.columns
b2.shape,b3.shape
b2['Tag'].value_counts()
sns.distplot(b2['Answers']);
plt.show()
sns.distplot(b2['Views']);
plt.show()
b2.isnull().sum()
sns.distplot(b2['Upvotes']);
plt.show()
b2 = b2.drop(b2[b2.Views > 3000000].b21)
b4 = LabelEncoder()
b2['Tag'] = b4.fit_transform(b2['Tag'])
b2.drop(['ID','Username'], b5 = 1,inplace =True)
b6 = b2['Upvotes']
from sklearn.preprocessing import Binarizer
b7 = Binarizer(threshold=7)
b8 = b7.transform([b2['Answers']])[0]
b2['b8'] = b8
b2.head()
b9 = [x for x in b2.columns if x not in ['Upvotes']]
b12, b13, y_train, b10 = train_test_split(b2[b9], b6,test_size = 0.22,random_state =205)
b11 = StandardScaler()
b12 = b11.fit_transform(b12)
b13 = b11.transform(b13)
b14 = PolynomialFeatures(degree = 4,interaction_only=False, include_bias=True)
b15 = b14.fit_transform(b12)
b14.fit(b12, y_train)
b16 = linear_model.LassoLars(alpha=0.021,max_iter=150)
b16.fit(b15, y_train)
b17 = b16.predict(b14.fit_transform(b13))
print(r2_score(b10, b17))
b18 = b3['ID']
b3.drop(['ID','Username'], b5 = 1,inplace =True)
b4 = LabelEncoder()
b3['Tag'] = b4.fit_transform(b3['Tag'])
from sklearn.preprocessing import Binarizer
b7 = Binarizer(threshold=7)
b8 = b7.transform([b3['Answers']])[0]
b3['b8'] = b8
b3 = b11.fit_transform(b3)
b19 = b16.predict(b14.fit_transform(b3))
b19 = abs(b19)
b20 = pd.DataFrame({'ID': b18,
                           'Upvotes':b19
                           })
b20.to_csv("linearregr.csv",b21 = False)
from google.colab import files
files.download('linearregr.csv')