import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.b17 import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin
b1 = pd.read_csv("https:
class class1(BaseEstimator, TransformerMixin):
    def fonk1(self, b2 = 3):
        self.b2 = b2
        self.b3 = []
        self.b4 = {}
    def fonk2(self, b6, b5 = None, b13=None):
        if not isinstance(b6, pd.DataFrame):
            b6 = pd.DataFrame(data=b6)
        self.b3 = list(b13.keys())
        for param in b13:
            for k in b13[param]:
                self.b4[f"{param}_{k}"] = f"(b7['{param}'] - {k}) * (b7['{param}'].apply(lambda b10: int(b10 > {k})))"
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
def fonk4(b7):
    return pd.get_dummies(b7[["age", "race", "wage"]]).copy()
def fonk5(b19, b20, b21, b22):
    plt.figure(b9 = (10, 6))
    sns.scatterplot(b10 = b19, b5=b20, s=10, label='Actual Wage')
    sns.lineplot(b10 = b19, b5=b21, label='Prediction')
    plt.b22(b22)
    plt.xlabel('Age')
    plt.ylabel('Wage')
    plt.legend()
    plt.show()
b11 = fonk4(b1)
b12 = class1(b2=3).fonk2(
    b6 = pd.get_dummies(b1[["age", "race"]]),
    b5 = b11["wage"],
    b13 = {"age": [40, 60]}
)
b14 = b12.fonk3(b11)
b15 = make_pipeline(class1(), LinearRegression())
b15.fonk2(
    pd.get_dummies(b1[["age", "race"]]),
    b1["wage"],
    b16 = {"age": [30, 40, 50, 60, 70]}
)
print(b15.named_steps['truncatedspline'])
b17 = LinearRegression()
b17.fonk2(pd.get_dummies(b1[["age", "race"]]), b1["wage"])
b18 = b17.predict(pd.get_dummies(b1[["age", "race"]]))
fonk5(
    b19 = b1["age"],
    b20 = b1["wage"],
    b21 = b18,
    b22 = 'Linear Regression Prediction vs Actual Wage'
)
b23 = b15.predict(pd.get_dummies(b1[["age", "race"]]))
fonk5(
    b19 = b1["age"],
    b20 = b1["wage"],
    b21 = b23,
    b22 = 'Truncated Spline Regression Prediction vs Actual Wage'
)