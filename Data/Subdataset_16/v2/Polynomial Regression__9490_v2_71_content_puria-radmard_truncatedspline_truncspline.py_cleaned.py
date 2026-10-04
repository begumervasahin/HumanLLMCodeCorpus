import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.b14 import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin
b1 = pd.read_csv("https:
class class1(BaseEstimator, TransformerMixin):
    def fonk1(self, b2 = 3):
        self.b2 = b2
        self.b3 = []
        self.b4 = {}
    def fonk2(self, b6, b5 = None, knots=None):
        if not isinstance(b6, pd.DataFrame):
            b6 = pd.DataFrame(data=b6)
        self.b3 = list(knots.keys())
        for param in knots:
            for k in knots[param]:
                self.b4[f"{param}_{k}"] = f"(b7['{param}'] - {k}) * (b7['{param}'].apply(lambda b17: int(b17 > {k})))"
        return self
    def fonk3(self, b6):
        b7 = b6.copy()[self.b3]
        for trunc in self.b4:
            for n in range(1, self.b2 + 1):
                b7[f"{trunc}_^{n}"] = eval(self.b4[trunc])**n
        for col in self.b3:
            for n in range(2, self.b2 + 1):
                b7[f"{col}_^{n}"] = b7[col]**n
        return pd.concat((b6, b7), b8 = 1)
b9 = pd.get_dummies(b1[["age", "race", "wage"]]).copy()
b10 = class1(b2=3).fonk2(b6=pd.get_dummies(b1[["age", "race"]]), b5=b9["wage"], knots={"age": [40, 60]})
b11 = b10.fonk3(b9)
b12 = make_pipeline(class1(), LinearRegression())
b12.fonk2(pd.get_dummies(b1[["age", "race"]]), b1["wage"], b13 = {"age": [30, 40, 50, 60, 70]})
print(b12.named_steps['truncatedspline'])
b14 = LinearRegression()
b14.fonk2(pd.get_dummies(b1[["age", "race"]]), b1["wage"])
b15 = b14.predict(pd.get_dummies(b1[["age", "race"]]))
plt.figure(b16 = (10, 6))
sns.scatterplot(b17 = b1["age"], b5=b1["wage"], s=10, label='Actual Wage')
sns.lineplot(b17 = b1["age"], b5=b15, label='Linear Regression Prediction')
plt.title('Linear Regression Prediction vs Actual Wage')
plt.xlabel('Age')
plt.ylabel('Wage')
plt.legend()
plt.show()
b18 = b12.predict(pd.get_dummies(b1[["age", "race"]]))
plt.figure(b16 = (10, 6))
sns.scatterplot(b17 = b1["age"], b5=b1["wage"], s=10, label='Actual Wage')
sns.lineplot(b17 = b1["age"], b5=b18, label='Pipeline Prediction')
plt.title('Truncated Spline Regression Prediction vs Actual Wage')
plt.xlabel('Age')
plt.ylabel('Wage')
plt.legend()
plt.show()