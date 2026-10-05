import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
train_data = pd.read_csv('train.dat', header=None, sep=' ', quoting=3)
train_labels = pd.read_csv('train.labels', header=None, sep=' ', quoting=3)
test_data = pd.read_csv('test.dat', header=None, sep=' ', quoting=3)
X_train = train_data.iloc[:, :-1]
y_train = train_labels.iloc[:, 0]
X_test = test_data
X_train_standardized = X_train - np.mean(X_train, axis=0)
X_test_standardized = X_test - np.mean(X_test, axis=0)
pca = PCA(n_components=28)
X_train_pca = pca.fit_transform(X_train_standardized)
X_test_pca = pca.transform(X_test_standardized)
xgb_classifier = XGBClassifier(
    learning_rate=0.3,
    n_estimators=2000,
    max_depth=7,
    min_child_weight=1,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    objective='binary:logistic',
    nthread=4,
    scale_pos_weight=1,
    seed=27
)
xgb_classifier.fit(X_train_pca, y_train)
y_pred = xgb_classifier.predict(X_test_pca)
output_df = pd.DataFrame(data=y_pred)
output_df.to_csv("output.dat", index=False, quoting=3, header=None)