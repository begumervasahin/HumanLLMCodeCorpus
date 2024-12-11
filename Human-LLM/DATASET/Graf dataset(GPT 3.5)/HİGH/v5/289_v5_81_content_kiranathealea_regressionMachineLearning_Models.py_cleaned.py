from sklearn.metrics import mean_squared_error, r2_score
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