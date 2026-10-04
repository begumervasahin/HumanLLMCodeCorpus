import pandas as pd
import seaborn as sns
from sklearn.b16 import LinearRegression
from sklearn.pipeline import make_pipeline
b1 = pd.read_csv(
    b2 = "https:
    a1 = 0
)
class class1:
    def fonk1(self, b3 = 3):
        self.b3 = b3
    def fonk2(self, b4, b11, b12):
        if type(b4) != pd.DataFrame:
            b4 = pd.DataFrame(data=b4)
        self.b5 = list(b12.keys())
        self.b6 = {}
        for param in b12:
            for k in b12[param]:
                self.b6[f"{param}_{k}"] = f"(b7['{param}'] - {k}) * (b7['{param}'].apply(lambda b18: int(b18 > {k})))"
        return self
    def fonk3(self, b4):
        b7 = b4.copy()[self.b5]
        for trunc in self.b6:
            for n in range(1, self.b3 + 1):
                b7[f"{trunc}_^{n}"] = eval(self.b6[trunc])**n
        for col in self.b5:
            for n in range(2, self.b3 + 1):
                b7[f"{col}_^{n}"] = b7[col]**n
        return pd.concat((b4, b7), b8 = 1)
b9 = pd.get_dummies(b1[["age", "race", "wage"]])
b10 = class1(b3=3).fonk2(
    b4 = pd.get_dummies(b1[["age", "race"]]),
    b11 = b9["wage"],
    b12 = {"age": [40, 60]}
)
b13 = b10.fonk3(b9)
b14 = make_pipeline(class1(), LinearRegression())
b14.fonk2(
    pd.get_dummies(b1[["age", "race"]]),
    b1["wage"],
    b15 = {"age": [30, 40, 50, 60, 70]}
)
print(b14.named_steps['truncatedspline'])
b16 = LinearRegression()
b16.fonk2(
    pd.get_dummies(b1[["age", "race"]]),
    b1["wage"]
)
b17 = b16.predict(pd.get_dummies(b1[["age", "race"]]))
sns.scatterplot(b18 = b1["age"], b11=b1["wage"], s=10)
sns.lineplot(b18 = b1["age"], b11=b17)
b19 = b14.predict(pd.get_dummies(b1[["age", "race"]]))
sns.scatterplot(b18 = b1["age"], b11=b1["wage"], s=10)
sns.lineplot(b18 = b1["age"], b11=b19)
sns.plt.show()