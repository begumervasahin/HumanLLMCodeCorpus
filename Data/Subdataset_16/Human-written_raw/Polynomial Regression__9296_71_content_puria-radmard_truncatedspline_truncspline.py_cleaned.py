from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
import pandas as pd
import seaborn as sns
b1 = pd.read_csv(index_col = 0, filepath_or_buffer = "https:
class class1:
    def fonk1(self, b2 = 3):
        self.b2 = b2
    def fonk2(self, b3, y, knots):
        """
        knots comes in the form {"Parameter1": [k1, k2, k3], "Parameter2": [k4, k5, k6]}
        where Parameters are the model predictors, and k
        exist for their respective predictor.
        If no knots are used but the parameter is still to be used in the regression,
        simply pass {... , Parameterj:[] ,  ...}
        """
        if type(b3) != pd.DataFrame:
            b3 = pd.DataFrame(data = b3)
        self.b4 = list(knots.keys())
        self.b5 = {}
        for param in knots:
            for k in knots[param]:
                self.b5["{}_{}".format(param, k)] = .format(
                    param, k, param, k)
        return self
    def fonk3(self, b3):
        b6 = b3.copy()[self.b4]
        for trunc in self.b5:
            for n in range(1, self.b2 + 1):
                b6["{}_^{}".format(trunc, n)] = eval(self.b5[trunc])**n
        for col in self.b4:
            for n in range(2, self.b2 + 1):
                b6["{}_^{}".format(col, n)] = b6[col]**n
        return (pd.concat((b3, b6), b7 = 1))
b8 = pd.get_dummies(b1[["age", "race", "wage"]]).copy()
b8.head()
b9 = class1(b2 = 3).fonk2(b3 = pd.get_dummies(b1[["age", "race"]]), y = b8["wage"],  knots = {"age": [40, 60]})
b9.fonk3(b8)
b10 = make_pipeline(class1(), LinearRegression())
b10.fonk2(pd.get_dummies(b1[["age", "race"]]), b1["wage"], b11 = {"age": [30, 40, 50, 60, 70]})
b10.named_steps['truncatedspline']
b12 = LinearRegression().fonk2(pd.get_dummies(b1[["age", "race"]]),
                                         b1["wage"]).predict(pd.get_dummies(b1[["age", "race"]]))
sns.scatterplot(b1["age"], b1["wage"], b13 = 10)
sns.lineplot(b1["age"], b12)
b12 = b10.predict(pd.get_dummies(b1[["age", "race"]]))
sns.scatterplot(b1["age"], b1["wage"], b13 = 10)
sns.lineplot(b1["age"], b12)