from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
class LinearModel:
    def __init__(self, model):
        self.model = model
    def compute_metrics(self, x, y):
        self.model.fit(x, y)
        y_predicted = self.model.predict(x)
        self.intercept_ = self.model.intercept_
        self.coeffs_ = self.model.coef_
        self.rmse_ = mean_squared_error(y, y_predicted, squared=False)
        self.r2_ = r2_score(y, y_predicted)
        return self
if __name__ == "__main__":
    x_train = [[1], [2], [3], [4], [5]]
    y_train = [2, 4, 5, 4, 5]
    model = LinearRegression()
    linear_model = LinearModel(model)
    linear_model.compute_metrics(x_train, y_train)
    print("Intercept:", linear_model.intercept_)
    print("Coefficients:", linear_model.coeffs_)
    print("RMSE:", linear_model.rmse_)
    print("R2 Score:", linear_model.r2_)