import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
wagedf = pd.read_csv(
    filepath_or_buffer="https:
    index_col=0
)
class TruncatedSpline:
    def __init__(self, degree=3):
        self.degree = degree
    def fit(self, X, y, knots):
        if type(X) != pd.DataFrame:
            X = pd.DataFrame(data=X)
        self.cols = list(knots.keys())
        self.truncs = {}
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
testdf = pd.get_dummies(wagedf[["age", "race", "wage"]])
a = TruncatedSpline(degree=3).fit(
    X=pd.get_dummies(wagedf[["age", "race"]]),
    y=testdf["wage"],
    knots={"age": [40, 60]}
)
transformed_df = a.transform(testdf)
pipe = make_pipeline(TruncatedSpline(), LinearRegression())
pipe.fit(
    pd.get_dummies(wagedf[["age", "race"]]),
    wagedf["wage"],
    truncatedspline__knots={"age": [30, 40, 50, 60, 70]}
)
print(pipe.named_steps['truncatedspline'])
predicted_wages_simple = LinearRegression().fit(
    pd.get_dummies(wagedf[["age", "race"]]),
    wagedf["wage"]
).predict(pd.get_dummies(wagedf[["age", "race"]]))
sns.scatterplot(x=wagedf["age"], y=wagedf["wage"], s=10)
sns.lineplot(x=wagedf["age"], y=predicted_wages_simple)
predicted_wages_pipe = pipe.predict(pd.get_dummies(wagedf[["age", "race"]]))
sns.scatterplot(x=wagedf["age"], y=wagedf["wage"], s=10)
sns.lineplot(x=wagedf["age"], y=predicted_wages_pipe)