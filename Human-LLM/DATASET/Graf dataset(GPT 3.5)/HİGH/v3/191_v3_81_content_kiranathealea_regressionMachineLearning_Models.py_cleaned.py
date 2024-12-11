from sklearn.metrics import mean_squared_error, r2_score
from sklearn.b10 import LinearRegression
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
    def fonk2(self, x, y):
        self.b1.fit(x, y)
        b6 = self.b1.predict(x)
        self.b2 = self.b1.b2
        self.b3 = self.b1.coef_
        self.b4 = mean_squared_error(y, b6, squared=False)
        self.b5 = r2_score(y, b6)
    def fonk3(self):
        print("Intercept:", self.b2)
        print("Coefficients:", self.b3)
        print("RMSE:", self.b4)
        print("R2 Score:", self.b5)
if b7 = = "__main__":
    b8 = [[1], [2], [3], [4], [5]]
    b9 = [2, 4, 5, 4, 5]
    b1 = LinearRegression()
    b10 = class1(b1)
    b10.fonk2(b8, b9)
    b10.fonk3()