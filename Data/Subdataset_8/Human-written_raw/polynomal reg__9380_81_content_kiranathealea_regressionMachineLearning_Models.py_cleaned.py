from sklearn.metrics import mean_squared_error, r2_score
class LinearModel:
    def __init__(self, model):
        self.model = model
    def compute_metrics(self, x, y):
        self.model.fit(x, y)
        y_predicted = self.model.predict(x)
        self.intercept_ = self.model.intercept_
        self.coef_ = self.model.coef_
        self.rmse_ = mean_squared_error(y, y_predicted)
        self.r2_ = r2_score(y, y_predicted)
        return self