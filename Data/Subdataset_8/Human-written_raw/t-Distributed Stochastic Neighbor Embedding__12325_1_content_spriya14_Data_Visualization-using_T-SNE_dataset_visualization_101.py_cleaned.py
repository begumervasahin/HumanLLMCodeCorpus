1. Repository: spriya14/Data_Visualization-using_T-SNE
   File: dataset_visualization_101.py
   URL: https:
   Code Content:
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import sklearn as sklearn
import matplotlib.pyplot as mlt
import io
from sklearn.model_selection import train_test_split
import io
dataframe_all = pd.read_csv("https:
dataframe_all.head()
num_rows = dataframe_all.shape[0]
num_rows
count_null = dataframe_all.isnull().sum()
counter_without_null = count_null[count_null == 0]
dataframe_all = dataframe_all[counter_without_null.keys()]
dataframe_all = dataframe_all.ix[:,7:]
all_columns=dataframe_all.columns
x = dataframe_all.ix[:,:-1].values
standard_scaler = StandardScaler()
x_std = standard_scaler.fit_transform(x)
y = dataframe_all.ix[:,-1].values
class_label = np.unique(y)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
class_label
test_percentage = 0.1
x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size = test_percentage, random_state = 0)
from sklearn.manifold import TSNE
tsne = TSNE()
tsne1 = TSNE(n_components = 2, random_state =0)
x_test_2d = tsne1.fit_transform(x_test)
markers=('s', 'd', 'o', '^', 'v')
color_map = {0:'red', 1:'blue', 2:'lightgreen', 3:'purple', 4:'cyan'}
mlt.figure()
for idx, cl in enumerate(np.unique(y_test)):
    mlt.scatter(x=x_test_2d[y_test==cl,0], y=x_test_2d[y_test==cl,1], c=color_map[idx], marker=markers[idx], label=cl)
mlt.xlabel('X in t-SNE')
mlt.ylabel('Y in t-SNE')
mlt.legend(loc='upper left')
mlt.title('t-SNE visualization of test data')
mlt.show()
   README Content:
Visualization of data using t-distributed stochastic neighbor embedding plots to a huge dataset.
**Overview Of Data**:
The human activities dataset contains 5 classes (sitting-down, standing-up, standing, walking, and sitting) collected on 8 hours of activities of 4 healthy subjects. The dataset is downloaded from the link mentioned below.
The code downloads the data, cleans it , creates feature vector and then uses T-SNE to reduce dimensionality of the feature vector to just 2, and matplotlib was then used to visualize the data.
**Dependencies** :
* pandas(http:
* numpy (http:
* scikit-learn (http:
* matplotlib (http:
Install dependencies via '[pip](https:
**Dataset Link** - https:
_***How To Run?***_
        Just Type the following command in your Terminal:
                >git clone https:
                >cd Data_Visualization-101
                >python dataset_visualization_101.py
