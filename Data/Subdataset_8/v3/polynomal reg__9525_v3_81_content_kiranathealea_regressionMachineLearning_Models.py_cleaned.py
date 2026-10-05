from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
class LinearModel:
    def __init__(self, model):
        self.model = model
        self.intercept_ = None
        self.coeffs_ = None
        self.rmse_ = None
        self.r2_ = None
    def train_and_compute_metrics(self, x, y):
        self.model.fit(x, y)
        y_predicted = self.model.predict(x)
        self.intercept_ = self.model.intercept_
        self.coeffs_ = self.model.coef_
        self.rmse_ = mean_squared_error(y, y_predicted, squared=False)
        self.r2_ = r2_score(y, y_predicted)
    def print_metrics(self):
        print("Intercept:", self.intercept_)
        print("Coefficients:", self.coeffs_)
        print("RMSE:", self.rmse_)
        print("R2 Score:", self.r2_)
if __name__ == "__main__":
    x_train = [[1], [2], [3], [4], [5]]
    y_train = [2, 4, 5, 4, 5]
    model = LinearRegression()
    linear_model = LinearModel(model)
    linear_model.train_and_compute_metrics(x_train, y_train)
    linear_model.print_metrics()