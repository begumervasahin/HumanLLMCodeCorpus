import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin
wagedf = pd.read_csv("https:
class TruncatedSpline(BaseEstimator, TransformerMixin):
    def __init__(self, degree=3):
        self.degree = degree
        self.cols = []
        self.truncs = {}
    def fit(self, X, y=None, knots=None):
        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(data=X)
        self.cols = list(knots.keys())
        for param in knots:
            for k in knots[param]:
                self.truncs[f"{param}_{k}"] = f"(df['{param}'] - {k}) * (df['{param}'].apply(lambda x: int(x > {k})))"
        return self
    def transform(self, X):
        df = X.copy()[self.cols]
        for trunc in self.truncs:
            for n in range(1, self.degree + 1):
                df[f"{trunc}_^{n}"] = eval(self.truncs[trunc])**n
        for col in self.cols:
            for n in range(2, self.degree + 1):
                df[f"{col}_^{n}"] = df[col]**n
        return pd.concat((X, df), axis=1)
testdf = pd.get_dummies(wagedf[["age", "race", "wage"]]).copy()
spline_transformer = TruncatedSpline(degree=3).fit(X=pd.get_dummies(wagedf[["age", "race"]]), y=testdf["wage"], knots={"age": [40, 60]})
transformed_df = spline_transformer.transform(testdf)
pipe = make_pipeline(TruncatedSpline(), LinearRegression())
pipe.fit(pd.get_dummies(wagedf[["age", "race"]]), wagedf["wage"], truncatedspline__knots={"age": [30, 40, 50, 60, 70]})
print(pipe.named_steps['truncatedspline'])
linear_model = LinearRegression()
linear_model.fit(pd.get_dummies(wagedf[["age", "race"]]), wagedf["wage"])
predicted_wages_linear = linear_model.predict(pd.get_dummies(wagedf[["age", "race"]]))
plt.figure(figsize=(10, 6))
sns.scatterplot(x=wagedf["age"], y=wagedf["wage"], s=10, label='Actual Wage')
sns.lineplot(x=wagedf["age"], y=predicted_wages_linear, label='Linear Regression Prediction')
plt.title('Linear Regression Prediction vs Actual Wage')
plt.xlabel('Age')
plt.ylabel('Wage')
plt.legend()
plt.show()
predicted_wages_pipe = pipe.predict(pd.get_dummies(wagedf[["age", "race"]]))
plt.figure(figsize=(10, 6))
sns.scatterplot(x=wagedf["age"], y=wagedf["wage"], s=10, label='Actual Wage')
sns.lineplot(x=wagedf["age"], y=predicted_wages_pipe, label='Pipeline Prediction')
plt.title('Truncated Spline Regression Prediction vs Actual Wage')
plt.xlabel('Age')
plt.ylabel('Wage')
plt.legend()
plt.show()