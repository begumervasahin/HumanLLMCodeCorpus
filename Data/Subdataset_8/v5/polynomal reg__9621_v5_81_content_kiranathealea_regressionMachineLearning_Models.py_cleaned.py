from sklearn.metrics import mean_squared_error, r2_score
class LinearModel:
    def __init__(self, model):
        self.model = model
    def compute_metrics(self, x, y):
        self.model.fit(x, y)
        y_pred = self.model.predict(x)
        self.intercept_ = self.model.intercept_
        self.coeffs_ = self.model.coef_
        self.rmse_ = mean_squared_error(y, y_pred, squared=False)
        self.r2_ = r2_score(y, y_pred)
        return self