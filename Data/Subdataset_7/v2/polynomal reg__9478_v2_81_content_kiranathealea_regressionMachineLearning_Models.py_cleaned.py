from sklearn.metrics import mean_squared_error, r2_score
from sklearn.b10 import LinearRegression
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, x, y):
        self.b1.fit(x, y)
        b2 = self.b1.predict(x)
        self.b3 = self.b1.b3
        self.b4 = self.b1.coef_
        self.b5 = mean_squared_error(y, b2, squared=False)
        self.b6 = r2_score(y, b2)
        return self
if b7 = = "__main__":
    b8 = [[1], [2], [3], [4], [5]]
    b9 = [2, 4, 5, 4, 5]
    b1 = LinearRegression()
    b10 = class1(b1)
    b10.fonk2(b8, b9)
    print("Intercept:", b10.b3)
    print("Coefficients:", b10.b4)
    print("RMSE:", b10.b5)
    print("R2 Score:", b10.b6)